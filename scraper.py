#!/usr/bin/env python3
"""
KCLS Meeting Room Scraper.

Fetches room availability from the public LibCal scheduling grid at rooms.kcls.org
and appends inferred booking blocks to data/bookings/bookings.csv.

The public grid endpoint (/spaces/availability/grid) returns 30-minute time slots.
Slots with ``className == ""`` are blocked/booked; slots with
``className == "s-lc-eq-checkout"`` are available.  Consecutive blocked slots are
merged into booking blocks and stored as rows in the CSV.

Usage:
  uv run scraper.py
  uv run scraper.py --days 14
  uv run scraper.py --days 7 --libraries redmond,sammamish
"""

import argparse
import csv
import json
import logging
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import requests
import requests.exceptions

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Library configuration
# ---------------------------------------------------------------------------
LIBRARIES: dict[str, dict] = {
    "redmond": {
        "lid": 2392,
        "gid": 4468,
        "slug": "redmond",
        "phone": "425-885-1861",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "East Meeting Room 1": 17228,  # cap 66
            "East Meeting Room 2": 17229,  # cap 75
            "Conference Room": 17230,      # cap 10
        },
    },
    "sammamish": {
        "lid": 2397,
        "gid": 4481,
        "slug": "sammamish",
        "phone": "425-392-3130",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room": 17254,   # cap 72, gid=4481 (library default)
            "Sunset Room": 134490,   # cap TBD, gid=33944 (different group)
        },
        "space_gids": {
            134490: 33944,  # Sunset Room belongs to a different group
        },
    },
    "woodinville": {
        "lid": 2406,
        "gid": 4484,
        "slug": "woodinville",
        "phone": "425-788-0733",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room": 17258,  # cap 50
        },
    },
    "kingsgate": {
        "lid": None,
        "gid": None,
        "slug": "kingsgate",
        "phone": "425-821-7686",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room 1": 17223,  # cap 100
        },
    },
    "issaquah": {
        "lid": None,
        "gid": None,
        "slug": "issaquah",
        "phone": None,
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room": 17233,  # cap 35
        },
    },
    "bellevue": {
        "lid": 2360,
        "gid": None,
        "slug": "bellevue",
        "phone": "425-450-1765",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {},  # Space IDs to be discovered via probe_spaces.py
    },
}

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
BASE_URL = "https://rooms.kcls.org"
GRID_API = BASE_URL + "/spaces/availability/grid"

DATA_DIR = Path("data")
BOOKINGS_DIR = DATA_DIR / "bookings"
CSV_PATH = BOOKINGS_DIR / "bookings.csv"
LAST_RUN_PATH = BOOKINGS_DIR / "last_run.json"

CSV_COLUMNS = [
    "fetch_date",
    "booking_date",
    "day_of_week",
    "library",
    "space_name",
    "space_id",
    "booking_id",
    "title",
    "start_time",
    "end_time",
    "duration_hrs",
    "created_date",
    "lead_days",
    "source",
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": BASE_URL + "/",
}

REQUEST_DELAY = 0.5    # seconds between API calls
BACKOFF_DELAY = 30.0   # seconds to wait after a 429

# Available slots carry className="s-lc-eq-checkout".
# Booked/blocked slots have NO className key at all.
_CLASS_AVAILABLE = "s-lc-eq-checkout"


def _slot_is_booked(slot: dict) -> bool:
    """Return True when a grid slot is booked (blocked/unavailable).

    The grid API omits the ``className`` key entirely for booked slots.
    Available slots carry ``className == "s-lc-eq-checkout"``.

    Args:
        slot: Raw slot dict from the grid API.

    Returns:
        ``True`` if the slot is booked.
    """
    return "className" not in slot


# ---------------------------------------------------------------------------
# Grid API
# ---------------------------------------------------------------------------


def _discover_gid(lid: int, space_id: int) -> int | None:
    """Fetch the group ID (gid) for a space by loading its booking page.

    The grid endpoint requires a gid.  When gid is unknown we can parse it
    from the inline ``springyPage`` JS object on the space's public page.

    Args:
        lid: Library ID.
        space_id: LibCal space identifier.

    Returns:
        Group ID integer, or ``None`` if it could not be determined.
    """
    import re

    url = f"{BASE_URL}/space/{space_id}"
    try:
        resp = requests.get(url, headers={"User-Agent": HEADERS["User-Agent"]}, timeout=10)
        if resp.status_code != 200:
            return None
        m = re.search(r"groupId\s*:\s*(\d+)", resp.text)
        return int(m.group(1)) if m else None
    except requests.exceptions.RequestException:
        logger.exception("Could not discover gid for space %s", space_id)
        return None


def fetch_grid_slots(
    lid: int,
    gid: int,
    space_id: int,
    start_date: date,
    end_date: date,
) -> list[dict]:
    """Fetch raw 30-minute time slots from the public availability grid.

    Args:
        lid: Library ID.
        gid: Group ID for the space.
        space_id: LibCal space identifier.
        start_date: First date to fetch (inclusive).
        end_date: Last date to fetch (exclusive).

    Returns:
        List of slot dicts with keys ``start``, ``end``, ``itemId``, ``className``.
    """
    payload = {
        "lid": str(lid),
        "gid": str(gid),
        "eid[]": str(space_id),
        "start": f"{start_date.isoformat()}T00:00:00",
        "end": f"{end_date.isoformat()}T00:00:00",
        "pageIndex": "0",
        "pageSize": "18",
        "accessible": "0",
        "powered": "0",
        "isEquipment": "0",
        "isSeatBooking": "0",
    }
    try:
        resp = requests.post(GRID_API, data=payload, headers=HEADERS, timeout=20)
        if resp.status_code == 429:
            logger.warning("Rate limited for space %s, backing off %.0fs", space_id, BACKOFF_DELAY)
            time.sleep(BACKOFF_DELAY)
            resp = requests.post(GRID_API, data=payload, headers=HEADERS, timeout=20)
        if resp.status_code != 200:
            logger.warning("HTTP %s from grid API for space %s", resp.status_code, space_id)
            return []
        data = resp.json()
        slots = data.get("slots", [])
        return slots if isinstance(slots, list) else []
    except requests.exceptions.Timeout:
        logger.exception("Timeout fetching grid for space %s", space_id)
        return []
    except requests.exceptions.ConnectionError:
        logger.exception("Connection error fetching grid for space %s", space_id)
        return []
    except (requests.exceptions.RequestException, ValueError):
        logger.exception("Request error fetching grid for space %s", space_id)
        return []


# ---------------------------------------------------------------------------
# Slot → booking inference
# ---------------------------------------------------------------------------


def _parse_slot_dt(s: str) -> datetime | None:
    """Parse a ``YYYY-MM-DD HH:MM:SS`` slot timestamp.

    Args:
        s: Slot datetime string.

    Returns:
        Parsed ``datetime``, or ``None`` on parse failure.
    """
    try:
        return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None


def infer_bookings_from_slots(
    slots: list[dict],
    library: str,
    space_name: str,
    space_id: int,
    fetch_date: date,
) -> list[dict]:
    """Convert consecutive blocked 30-min slots into booking block records.

    Slots with an empty ``className`` are treated as booked.  Adjacent blocked
    slots on the same date are merged into a single booking record.

    Args:
        slots: Raw slot dicts from :func:`fetch_grid_slots`.
        library: Normalized branch name.
        space_name: Human-readable room name.
        space_id: LibCal space ID.
        fetch_date: Date this data was scraped.

    Returns:
        List of normalized booking records (one per contiguous blocked window).
    """
    # Collect blocked slots and sort by start time
    blocked = [sl for sl in slots if _slot_is_booked(sl)]
    if not blocked:
        return []

    blocked.sort(key=lambda x: x.get("start", ""))

    records: list[dict] = []
    block_start: datetime | None = None
    block_end: datetime | None = None

    def _flush(bs: datetime, be: datetime) -> None:
        booking_date = bs.date()
        duration_hrs = round((be - bs).total_seconds() / 3600.0, 4)
        # Synthetic ID: stable across runs for the same block
        booking_id = f"grid_{space_id}_{bs.strftime('%Y%m%d%H%M')}"
        records.append(
            {
                "fetch_date": fetch_date.isoformat(),
                "booking_date": booking_date.isoformat(),
                "day_of_week": booking_date.strftime("%A"),
                "library": library,
                "space_name": space_name,
                "space_id": space_id,
                "booking_id": booking_id,
                "title": "",
                "start_time": bs.strftime("%H:%M"),
                "end_time": be.strftime("%H:%M"),
                "duration_hrs": duration_hrs,
                "created_date": "",
                "lead_days": "",
                "source": "grid",
            }
        )

    for sl in blocked:
        sl_start = _parse_slot_dt(sl.get("start", ""))
        sl_end = _parse_slot_dt(sl.get("end", ""))
        if not sl_start or not sl_end:
            continue

        if block_start is None:
            block_start = sl_start
            block_end = sl_end
        elif sl_start == block_end and sl_start.date() == block_start.date():
            # Contiguous slot on the same day — extend the block
            block_end = sl_end
        else:
            # Gap or new day — flush the previous block
            _flush(block_start, block_end)  # type: ignore[arg-type]
            block_start = sl_start
            block_end = sl_end

    if block_start and block_end:
        _flush(block_start, block_end)

    return records


# ---------------------------------------------------------------------------
# CSV I/O
# ---------------------------------------------------------------------------


def load_existing_ids(csv_path: Path) -> set[str]:
    """Return the set of booking_ids already present in the CSV.

    Args:
        csv_path: Path to the bookings CSV file.

    Returns:
        Set of booking ID strings.  Empty set if the file does not exist.
    """
    if not csv_path.exists():
        return set()
    ids: set[str] = set()
    try:
        with csv_path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                bid = row.get("booking_id", "").strip()
                if bid:
                    ids.add(bid)
    except OSError:
        logger.exception("Failed to read existing IDs from %s", csv_path)
    return ids


def append_to_csv(records: list[dict], csv_path: Path) -> int:
    """Append records whose booking_id is not already in the CSV.

    Creates the CSV with headers if it does not exist.

    Args:
        records: Normalized booking records to write.
        csv_path: Path to the bookings CSV file.

    Returns:
        Count of newly written rows.
    """
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    existing_ids = load_existing_ids(csv_path)
    new_records = [r for r in records if r["booking_id"] not in existing_ids]
    if not new_records:
        return 0

    write_header = not csv_path.exists()
    try:
        with csv_path.open("a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            if write_header:
                writer.writeheader()
            for record in new_records:
                writer.writerow({col: record.get(col, "") for col in CSV_COLUMNS})
    except OSError:
        logger.exception("Failed to write to %s", csv_path)
        return 0

    return len(new_records)


# ---------------------------------------------------------------------------
# Main scrape loop
# ---------------------------------------------------------------------------

# Cache of discovered gid values so we only fetch once per (lid, space_id) pair
_gid_cache: dict[tuple[int, int], int | None] = {}


def _resolve_gid(lib_cfg: dict, space_id: int) -> int | None:
    """Return a usable gid for the space, discovering it if necessary.

    Args:
        lib_cfg: Library configuration dict from :data:`LIBRARIES`.
        space_id: LibCal space identifier.

    Returns:
        Group ID, or ``None`` if it could not be determined.
    """
    lid = lib_cfg.get("lid")
    if lid is None:
        return None

    # Per-space gid override takes priority over the library-level default
    space_gids: dict[int, int] = lib_cfg.get("space_gids", {})
    if space_id in space_gids:
        return space_gids[space_id]

    configured_gid: int | None = lib_cfg.get("gid")
    if configured_gid is not None:
        return configured_gid

    cache_key = (lid, space_id)
    if cache_key in _gid_cache:
        return _gid_cache[cache_key]

    logger.info("  Discovering gid for space %s (lid=%s)…", space_id, lid)
    gid = _discover_gid(lid, space_id)
    _gid_cache[cache_key] = gid
    if gid:
        logger.info("  Discovered gid=%s for space %s", gid, space_id)
    else:
        logger.warning("  Could not discover gid for space %s — skipping", space_id)
    return gid


def run_scrape(days: int = 28, libraries_filter: str = "all") -> dict:
    """Scrape all configured libraries/spaces for the next ``days`` days.

    Args:
        days: Number of days ahead to scrape (inclusive of today).
        libraries_filter: Comma-separated library names, or ``"all"``.

    Returns:
        Run-metadata dict written to ``last_run.json``.
    """
    today = date.today()
    end_date = today + timedelta(days + 1)   # exclusive end for grid API

    if libraries_filter == "all":
        scope = LIBRARIES
    else:
        keys = [k.strip() for k in libraries_filter.split(",")]
        scope = {k: v for k, v in LIBRARIES.items() if k in keys}
        missing = [k for k in keys if k not in LIBRARIES]
        if missing:
            logger.warning("Unknown libraries: %s", missing)

    all_records: list[dict] = []
    fetch_date = today

    for lib_name, lib_cfg in scope.items():
        spaces: dict[str, int | None] = lib_cfg.get("spaces", {})
        if not spaces:
            logger.info("Skipping %s: no space IDs configured", lib_name)
            continue

        lid = lib_cfg.get("lid")
        if lid is None:
            logger.warning("Skipping %s: lid unknown (needed for grid API)", lib_name)
            continue

        logger.info("Scraping %s", lib_name)
        for space_name, space_id in spaces.items():
            if not space_id:
                logger.warning("  Skipping %s/%s: space_id unknown", lib_name, space_name)
                continue

            gid = _resolve_gid(lib_cfg, space_id)
            if gid is None:
                logger.warning("  Skipping %s/%s: gid unknown", lib_name, space_name)
                continue

            logger.debug("  %s (space_id=%s, lid=%s, gid=%s)", space_name, space_id, lid, gid)
            time.sleep(REQUEST_DELAY)

            slots = fetch_grid_slots(lid, gid, space_id, today, end_date)
            logger.debug("  %s: %d total slots, %d blocked", space_name, len(slots),
                         sum(1 for sl in slots if _slot_is_booked(sl)))

            records = infer_bookings_from_slots(slots, lib_name, space_name, space_id, fetch_date)
            all_records.extend(records)
            logger.info("  %s: %d booking blocks inferred", space_name, len(records))

    new_written = append_to_csv(all_records, CSV_PATH)
    logger.info("Total booking blocks: %d; %d new rows written.", len(all_records), new_written)

    run_meta = {
        "run_date": today.isoformat(),
        "run_time": datetime.now().strftime("%H:%M:%S"),
        "range_start": today.isoformat(),
        "range_end": end_date.isoformat(),
        "total_fetched": len(all_records),
        "new_written": new_written,
        "libraries_scraped": list(scope.keys()),
    }
    BOOKINGS_DIR.mkdir(parents=True, exist_ok=True)
    try:
        LAST_RUN_PATH.write_text(json.dumps(run_meta, indent=2))
    except OSError:
        logger.exception("Failed to write %s", LAST_RUN_PATH)
    return run_meta


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Parse CLI arguments and run the scraper."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description="KCLS meeting room scraper")
    parser.add_argument("--days", type=int, default=28, help="Days ahead to scrape (default: 28)")
    parser.add_argument("--libraries", default="all", help='Comma-separated library names or "all"')
    args = parser.parse_args()
    run_scrape(days=args.days, libraries_filter=args.libraries)


if __name__ == "__main__":
    main()
