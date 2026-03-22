#!/usr/bin/env python3
"""
KCLS Meeting Room Scraper
Fetches confirmed bookings from the LibCal JSON API at rooms.kcls.org
and appends new records to data/bookings/bookings.csv.

Usage:
  python scraper.py
  python scraper.py --days 14
  python scraper.py --days 7 --libraries redmond,sammamish
"""

import argparse
import csv
import json
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Library configuration
# Phase 1: confirmed branches with known space IDs.
# lid=None means the library ID hasn't been verified yet (space IDs are enough
# to call the bookings API; lid is only needed for the /r/accessible view).
# ---------------------------------------------------------------------------
LIBRARIES: dict = {
    "redmond": {
        "lid": 2392,
        "slug": "redmond",
        "phone": "425-885-1861",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "East Meeting Room 1": 17228,   # cap 66
            "East Meeting Room 2": 17229,   # cap 75
            "Conference Room":     17230,   # cap 10
        },
    },
    "sammamish": {
        "lid": 2397,
        "slug": "sammamish",
        "phone": "425-392-3130",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room": 17254,     # cap 72
            "Sunset Room":  134490,    # cap TBD
        },
    },
    "woodinville": {
        "lid": 2406,
        "slug": "woodinville",
        "phone": "425-788-0733",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room": 17258,     # cap 50
        },
    },
    "kingsgate": {
        "lid": None,
        "slug": "kingsgate",
        "phone": "425-821-7686",
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room 1": 17223,   # cap 100, piano, sound system
        },
    },
    "issaquah": {
        "lid": None,
        "slug": "issaquah",
        "phone": None,
        "saturday_hours": ("11:00", "18:00"),
        "sunday_open": True,
        "spaces": {
            "Meeting Room": 17233,     # cap 35
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

REQUEST_DELAY = 0.5   # seconds between API calls
BACKOFF_DELAY = 30.0  # seconds to wait after a 429


# ---------------------------------------------------------------------------
# API fetching
# ---------------------------------------------------------------------------

def fetch_bookings_api(space_id: int, date_str: str) -> list[dict]:
    """
    Fetch confirmed bookings for a single space on a single date.
    Returns a list of raw booking dicts from the API, or [] on failure.
    date_str: "YYYY-MM-DD"
    """
    params = {
        "ids": space_id,
        "dates": date_str,
        "limit": 500,
    }
    try:
        resp = requests.get(
            BOOKINGS_API, params=params, headers=HEADERS, timeout=15
        )
        if resp.status_code == 429:
            print(f"    [429] Rate limited on space {space_id} / {date_str}, backing off {BACKOFF_DELAY}s")
            time.sleep(BACKOFF_DELAY)
            resp = requests.get(
                BOOKINGS_API, params=params, headers=HEADERS, timeout=15
            )
        if resp.status_code != 200:
            print(f"    [HTTP {resp.status_code}] space {space_id} / {date_str}")
            return []
        data = resp.json()
        bookings = data.get("bookings", [])
        if not isinstance(bookings, list):
            return []
        return bookings
    except Exception as e:
        print(f"    [ERROR] space {space_id} / {date_str}: {e}")
        return []


def fetch_bookings_playwright(space_id: int, date_str: str) -> list[dict]:
    """
    Fallback: scrape the confirmed bookings page via headless Chromium.
    Returns a list of booking dicts with the same keys as the API response.
    Only called when the API returns [] for a space that should have bookings.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("    [WARN] Playwright not installed — skipping fallback")
        return []

    url = f"{BASE_URL}/space/{space_id}/confirmed?d={date_str}"
    rows = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=30000)
            page.wait_for_selector("table", timeout=10000)
            # Each confirmed-bookings table row: Date | Time | Room | Event
            for tr in page.query_selector_all("table tbody tr"):
                cells = [td.inner_text().strip() for td in tr.query_selector_all("td")]
                if len(cells) < 3:
                    continue
                # Best-effort parsing — fields vary by LibCal version
                rows.append({
                    "bookId": f"pw_{space_id}_{date_str}_{len(rows)}",
                    "eid": space_id,
                    "fromDate": f"{date_str} 00:00:00",
                    "toDate":   f"{date_str} 00:00:00",
                    "created":  None,
                    "title":    cells[-1] if cells else "",
                    "status":   "Confirmed",
                    "_playwright_raw": cells,
                })
            browser.close()
    except Exception as e:
        print(f"    [Playwright ERROR] space {space_id} / {date_str}: {e}")
    return rows


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------

def _parse_dt(s: str | None) -> datetime | None:
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
    """
    Map a raw API booking dict to the standard CSV schema.
    Returns None if the record is malformed / not Confirmed.
    """
    status = raw.get("status", "")
    if status and status.lower() != "confirmed":
        return None

    booking_id = raw.get("bookId") or raw.get("id")
    if not booking_id:
        return None

    from_dt = _parse_dt(raw.get("fromDate"))
    to_dt   = _parse_dt(raw.get("toDate"))
    if not from_dt:
        return None

    booking_date = from_dt.date()
    duration_hrs: float | None = None
    if from_dt and to_dt:
        delta = (to_dt - from_dt).total_seconds() / 3600.0
        duration_hrs = round(delta, 4)

    created_dt = _parse_dt(raw.get("created"))
    created_date = created_dt.date() if created_dt else None
    lead_days: int | None = None
    if created_date is not None:
        lead_days = (booking_date - created_date).days

    title = (raw.get("title") or "").strip()

    return {
        "fetch_date":   fetch_date.isoformat(),
        "booking_date": booking_date.isoformat(),
        "day_of_week":  booking_date.strftime("%A"),
        "library":      library,
        "space_name":   space_name,
        "space_id":     space_id,
        "booking_id":   str(booking_id),
        "title":        title,
        "start_time":   from_dt.strftime("%H:%M") if from_dt else "",
        "end_time":     to_dt.strftime("%H:%M") if to_dt else "",
        "duration_hrs": duration_hrs,
        "created_date": created_date.isoformat() if created_date else "",
        "lead_days":    lead_days if lead_days is not None else "",
        "source":       "api",
    }


# ---------------------------------------------------------------------------
# CSV I/O
# ---------------------------------------------------------------------------

def load_existing_ids(csv_path: Path) -> set[str]:
    """Return the set of booking_ids already in the CSV."""
    if not csv_path.exists():
        return set()
    ids = set()
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            bid = row.get("booking_id", "").strip()
            if bid:
                ids.add(bid)
    return ids


def append_to_csv(records: list[dict], csv_path: Path) -> int:
    """
    Append records whose booking_id is not already in the CSV.
    Creates the CSV with headers if it doesn't exist.
    Returns count of newly written rows.
    """
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    existing_ids = load_existing_ids(csv_path)

    new_records = [r for r in records if r["booking_id"] not in existing_ids]
    if not new_records:
        return 0

    write_header = not csv_path.exists()
    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
        if write_header:
            writer.writeheader()
        for record in new_records:
            writer.writerow({col: record.get(col, "") for col in CSV_COLUMNS})

    return len(new_records)


# ---------------------------------------------------------------------------
# Main scrape loop
# ---------------------------------------------------------------------------

def run_scrape(days: int = 28, libraries_filter: str = "all") -> dict:
    """
    Scrape all configured libraries/spaces for the next `days` days.
    Returns a run-metadata dict for last_run.json.
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
            print(f"[WARN] Unknown libraries: {missing}")

    all_records: list[dict] = []
    errors: list[str] = []
    fetch_date = today

    for lib_name, lib_cfg in scope.items():
        spaces = lib_cfg.get("spaces", {})
        if not spaces:
            print(f"[SKIP] {lib_name}: no space IDs configured")
            continue

        print(f"\n=== {lib_name} ===")
        for space_name, space_id in spaces.items():
            if not space_id:
                print(f"  [SKIP] {space_name}: space_id unknown")
                continue
            print(f"  {space_name} (id={space_id})")

            for target_date in date_range:
                date_str = target_date.isoformat()
                time.sleep(REQUEST_DELAY)

                raw_bookings = fetch_bookings_api(space_id, date_str)
                if not raw_bookings:
                    continue  # no bookings on that day — normal

                for raw in raw_bookings:
                    norm = normalize_booking(raw, lib_name, space_name, space_id, fetch_date)
                    if norm:
                        all_records.append(norm)

    new_written = append_to_csv(all_records, CSV_PATH)
    print(f"\nFetched {len(all_records)} records total; {new_written} new rows written.")

    run_meta = {
        "run_date":         today.isoformat(),
        "run_time":         datetime.utcnow().strftime("%H:%M:%S"),
        "range_start":      today.isoformat(),
        "range_end":        (today + timedelta(days)).isoformat(),
        "total_fetched":    len(all_records),
        "new_written":      new_written,
        "libraries_scraped": list(scope.keys()),
        "errors":           errors,
    }
    BOOKINGS_DIR.mkdir(parents=True, exist_ok=True)
    LAST_RUN_PATH.write_text(json.dumps(run_meta, indent=2))
    return run_meta


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="KCLS meeting room scraper")
    parser.add_argument(
        "--days",
        type=int,
        default=28,
        help="Number of days ahead to scrape (default: 28)",
    )
    parser.add_argument(
        "--libraries",
        default="all",
        help='Comma-separated library names or "all" (default: all)',
    )
    args = parser.parse_args()
    run_scrape(days=args.days, libraries_filter=args.libraries)


if __name__ == "__main__":
    main()
