#!/usr/bin/env python3
"""
KCLS Meeting Room Scraper.

Fetches confirmed bookings from the LibCal JSON API at rooms.kcls.org
and appends new records to data/bookings/bookings.csv.

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

try:
    from playwright.sync_api import sync_playwright as _sync_playwright
    from playwright.sync_api import Browser, Page

    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Library configuration
# Phase 1: confirmed branches with known space IDs.
# lid=None means the library ID hasn't been verified yet (space IDs are enough
# to call the bookings API; lid is only needed for the /r/accessible view).
# ---------------------------------------------------------------------------
LIBRARIES: dict[str, dict] = {
    "redmond": {
        "lid": 2392,
        "slug": "redmond",
        "phone": "425-885-1861",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "East Meeting Room 1": 17228,  # cap 66
            "East Meeting Room 2": 17229,  # cap 75
            "Conference Room": 17230,  # cap 10
        },
    },
    "sammamish": {
        "lid": 2397,
        "slug": "sammamish",
        "phone": "425-392-3130",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room": 17254,  # cap 72
            "Sunset Room": 134490,  # cap TBD
        },
    },
    "woodinville": {
        "lid": 2406,
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
        "slug": "kingsgate",
        "phone": "425-821-7686",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room 1": 17223,  # cap 100, piano, sound system
        },
    },
    "issaquah": {
        "lid": None,
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
        "slug": "bellevue",
        "phone": "425-450-1765",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            # Space IDs to be discovered via probe_spaces.py
        },
    },
}

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
BASE_URL = "https://rooms.kcls.org"
BOOKINGS_API = BASE_URL + "/api/1.1/space/bookings"
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
    "Accept": "application/json",
}

REQUEST_DELAY = 0.5  # seconds between API calls
BACKOFF_DELAY = 30.0  # seconds to wait after a 429


# ---------------------------------------------------------------------------
# API fetching
# ---------------------------------------------------------------------------


def fetch_bookings_api(space_id: int, date_str: str) -> list[dict]:
    """Fetch confirmed bookings for a single space on a single date.

    Args:
        space_id: LibCal space identifier.
        date_str: Target date in ``YYYY-MM-DD`` format.

    Returns:
        List of raw booking dicts from the API, or ``[]`` on failure.
    """
    params = {"ids": space_id, "dates": date_str, "limit": 500}
    try:
        resp = requests.get(BOOKINGS_API, params=params, headers=HEADERS, timeout=15)
        if resp.status_code == 429:
            logger.warning("Rate limited on space %s / %s, backing off %.0fs", space_id, date_str, BACKOFF_DELAY)
            time.sleep(BACKOFF_DELAY)
            resp = requests.get(BOOKINGS_API, params=params, headers=HEADERS, timeout=15)
        if resp.status_code != 200:
            logger.warning("HTTP %s for space %s / %s", resp.status_code, space_id, date_str)
            return []
        data = resp.json()
        bookings = data.get("bookings", [])
        return bookings if isinstance(bookings, list) else []
    except requests.exceptions.Timeout:
        logger.exception("Timeout fetching space %s / %s", space_id, date_str)
        return []
    except requests.exceptions.ConnectionError:
        logger.exception("Connection error fetching space %s / %s", space_id, date_str)
        return []
    except (requests.exceptions.RequestException, ValueError):
        logger.exception("Request error fetching space %s / %s", space_id, date_str)
        return []


def fetch_bookings_playwright(space_id: int, date_str: str) -> list[dict]:
    """Scrape the confirmed bookings page via headless Chromium (fallback).

    Only called when the API returns ``[]`` for a space expected to have bookings.
    Requires the ``playwright`` package with Chromium installed.

    Args:
        space_id: LibCal space identifier.
        date_str: Target date in ``YYYY-MM-DD`` format.

    Returns:
        List of booking dicts with the same shape as the API response, or ``[]``.
    """
    if not PLAYWRIGHT_AVAILABLE:
        logger.warning("Playwright not installed — skipping fallback for space %s", space_id)
        return []

    url = f"{BASE_URL}/space/{space_id}/confirmed?d={date_str}"
    rows: list[dict] = []
    try:
        with _sync_playwright() as p:
            browser: Browser = p.chromium.launch(headless=True)
            page: Page = browser.new_page()
            page.goto(url, timeout=30000)
            page.wait_for_selector("table", timeout=10000)
            for tr in page.query_selector_all("table tbody tr"):
                cells = [td.inner_text().strip() for td in tr.query_selector_all("td")]
                if len(cells) < 3:
                    continue
                rows.append(
                    {
                        "bookId": f"pw_{space_id}_{date_str}_{len(rows)}",
                        "eid": space_id,
                        "fromDate": f"{date_str} 00:00:00",
                        "toDate": f"{date_str} 00:00:00",
                        "created": None,
                        "title": cells[-1] if cells else "",
                        "status": "Confirmed",
                        "_playwright_raw": cells,
                    }
                )
            browser.close()
    except (OSError, TimeoutError):
        logger.exception("Playwright error for space %s / %s", space_id, date_str)
    return rows


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------


def _parse_dt(s: str | None) -> datetime | None:
    """Parse a datetime string in common LibCal formats.

    Args:
        s: Datetime string, or ``None``.

    Returns:
        Parsed ``datetime``, or ``None`` if unparseable.
    """
    if not s:
        return None
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    return None


def normalize_booking(
    raw: dict,
    library: str,
    space_name: str,
    space_id: int,
    fetch_date: date,
) -> dict | None:
    """Map a raw API booking dict to the standard CSV schema.

    Args:
        raw: Raw booking dict from the LibCal API.
        library: Normalized branch name (lowercase, no spaces).
        space_name: Human-readable room name.
        space_id: LibCal space ID.
        fetch_date: Date this record was scraped.

    Returns:
        Normalized record dict, or ``None`` if the record is malformed or not Confirmed.
    """
    status = raw.get("status", "")
    if status and status.lower() != "confirmed":
        return None

    booking_id = raw.get("bookId") or raw.get("id")
    if not booking_id:
        return None

    from_dt = _parse_dt(raw.get("fromDate"))
    to_dt = _parse_dt(raw.get("toDate"))
    if not from_dt:
        return None

    booking_date = from_dt.date()
    duration_hrs: float | None = None
    if to_dt is not None:
        duration_hrs = round((to_dt - from_dt).total_seconds() / 3600.0, 4)

    created_dt = _parse_dt(raw.get("created"))
    created_date = created_dt.date() if created_dt else None
    lead_days: int | None = (booking_date - created_date).days if created_date is not None else None

    return {
        "fetch_date": fetch_date.isoformat(),
        "booking_date": booking_date.isoformat(),
        "day_of_week": booking_date.strftime("%A"),
        "library": library,
        "space_name": space_name,
        "space_id": space_id,
        "booking_id": str(booking_id),
        "title": (raw.get("title") or "").strip(),
        "start_time": from_dt.strftime("%H:%M"),
        "end_time": to_dt.strftime("%H:%M") if to_dt else "",
        "duration_hrs": duration_hrs,
        "created_date": created_date.isoformat() if created_date else "",
        "lead_days": lead_days if lead_days is not None else "",
        "source": "api",
    }


# ---------------------------------------------------------------------------
# CSV I/O
# ---------------------------------------------------------------------------


def load_existing_ids(csv_path: Path) -> set[str]:
    """Return the set of booking_ids already present in the CSV.

    Args:
        csv_path: Path to the bookings CSV file.

    Returns:
        Set of booking ID strings. Empty set if the file does not exist.
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


def run_scrape(days: int = 28, libraries_filter: str = "all") -> dict:
    """Scrape all configured libraries/spaces for the next ``days`` days.

    Args:
        days: Number of days ahead to scrape (inclusive of today).
        libraries_filter: Comma-separated library names, or ``"all"``.

    Returns:
        Run-metadata dict written to ``last_run.json``.
    """
    today = date.today()
    date_range = [today + timedelta(d) for d in range(days + 1)]

    if libraries_filter == "all":
        scope = LIBRARIES
    else:
        keys = [k.strip() for k in libraries_filter.split(",")]
        scope = {k: v for k, v in LIBRARIES.items() if k in keys}
        missing = [k for k in keys if k not in LIBRARIES]
        if missing:
            logger.warning("Unknown libraries: %s", missing)

    all_records: list[dict] = []
    errors: list[str] = []
    fetch_date = today

    for lib_name, lib_cfg in scope.items():
        spaces: dict[str, int | None] = lib_cfg.get("spaces", {})
        if not spaces:
            logger.info("Skipping %s: no space IDs configured", lib_name)
            continue

        logger.info("Scraping %s", lib_name)
        for space_name, space_id in spaces.items():
            if not space_id:
                logger.warning("Skipping %s/%s: space_id unknown", lib_name, space_name)
                continue
            logger.debug("  %s (id=%s)", space_name, space_id)

            for target_date in date_range:
                date_str = target_date.isoformat()
                time.sleep(REQUEST_DELAY)

                raw_bookings = fetch_bookings_api(space_id, date_str)
                for raw in raw_bookings:
                    norm = normalize_booking(raw, lib_name, space_name, space_id, fetch_date)
                    if norm:
                        all_records.append(norm)

    new_written = append_to_csv(all_records, CSV_PATH)
    logger.info("Fetched %d records; %d new rows written.", len(all_records), new_written)

    run_meta = {
        "run_date": today.isoformat(),
        "run_time": datetime.utcnow().strftime("%H:%M:%S"),
        "range_start": today.isoformat(),
        "range_end": (today + timedelta(days)).isoformat(),
        "total_fetched": len(all_records),
        "new_written": new_written,
        "libraries_scraped": list(scope.keys()),
        "errors": errors,
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
