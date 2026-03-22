#!/usr/bin/env python3
"""
KCLS Meeting Room Availability Checker
Real-time slot checker: queries the LibCal API and shows open time windows.

Usage:
  python check_availability.py --date 2026-04-05
  python check_availability.py --date 2026-04-05 --library redmond
  python check_availability.py --saturdays --weeks 4
  python check_availability.py --saturdays --weeks 4 --min-hours 2
"""

import argparse
import json
import time
from datetime import date, datetime, timedelta
from pathlib import Path

from scraper import LIBRARIES, fetch_bookings_api, REQUEST_DELAY

AVAIL_DIR = Path("data") / "availability"


# ---------------------------------------------------------------------------
# Time interval helpers
# ---------------------------------------------------------------------------

def _hhmm_to_mins(hhmm: str) -> int:
    """'11:30' → 690"""
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m


def _mins_to_hhmm(mins: int) -> str:
    """690 → '11:30'"""
    return f"{mins // 60}:{mins % 60:02d}"


def _mins_to_ampm(mins: int) -> str:
    """690 → '11:30am'"""
    h = mins // 60
    m = mins % 60
    suffix = "am" if h < 12 else "pm"
    if h == 0:
        h = 12
    elif h > 12:
        h -= 12
    return f"{h}:{m:02d}{suffix}" if m else f"{h}{suffix}"


def compute_open_slots(
    bookings: list[dict],
    open_hhmm: str,
    close_hhmm: str,
    min_hours: float = 0,
) -> list[tuple[int, int]]:
    """
    Given a list of confirmed bookings (each with 'start_time'/'end_time' as HH:MM)
    and library open/close times, return a list of free (start_min, end_min) windows
    that are at least min_hours long.
    """
    open_min  = _hhmm_to_mins(open_hhmm)
    close_min = _hhmm_to_mins(close_hhmm)

    # Build list of booked intervals, clipped to open hours
    booked: list[tuple[int, int]] = []
    for b in bookings:
        try:
            bs = _hhmm_to_mins(b.get("start_time", "00:00"))
            be = _hhmm_to_mins(b.get("end_time",   "00:00"))
        except (ValueError, AttributeError):
            continue
        bs = max(bs, open_min)
        be = min(be, close_min)
        if be > bs:
            booked.append((bs, be))

    # Sort and merge overlapping booked intervals
    booked.sort()
    merged: list[tuple[int, int]] = []
    for interval in booked:
        if merged and interval[0] <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        else:
            merged.append(list(interval))

    # Free windows = gaps between booked intervals
    free: list[tuple[int, int]] = []
    cursor = open_min
    for bs, be in merged:
        if bs > cursor:
            free.append((cursor, bs))
        cursor = max(cursor, be)
    if cursor < close_min:
        free.append((cursor, close_min))

    # Filter by minimum duration
    min_mins = int(min_hours * 60)
    return [(s, e) for s, e in free if e - s >= min_mins]


def format_slot(start_min: int, end_min: int) -> str:
    return f"{_mins_to_ampm(start_min)}–{_mins_to_ampm(end_min)}"


# ---------------------------------------------------------------------------
# Per-date availability fetch
# ---------------------------------------------------------------------------

def get_availability_for_date(
    target_date: date,
    libraries_filter: str = "all",
    min_hours: float = 0,
) -> dict:
    """
    Returns:
      {library: {space_name: [open_slot_strings]}}
    """
    if libraries_filter == "all":
        scope = LIBRARIES
    else:
        keys = [k.strip() for k in libraries_filter.split(",")]
        scope = {k: LIBRARIES[k] for k in keys if k in LIBRARIES}

    date_str = target_date.isoformat()
    results: dict = {}

    for lib_name, lib_cfg in scope.items():
        spaces = lib_cfg.get("spaces", {})
        if not spaces:
            continue

        # Determine open hours for this day of week
        dow = target_date.strftime("%A")
        if dow == "Saturday":
            open_h, close_h = lib_cfg.get("saturday_hours", ("11:00", "18:00"))
        elif dow == "Sunday":
            if not lib_cfg.get("sunday_open", False):
                continue
            open_h, close_h = lib_cfg.get("sunday_hours", ("11:00", "18:00"))
        else:
            # Default weekday hours — most branches 10am–6pm or 12pm–8pm
            open_h, close_h = lib_cfg.get("weekday_hours", ("10:00", "18:00"))

        lib_slots: dict = {}
        for space_name, space_id in spaces.items():
            if not space_id:
                continue
            time.sleep(REQUEST_DELAY)
            raw = fetch_bookings_api(space_id, date_str)
            # Normalize to {start_time, end_time} dicts
            bookings_simple = []
            for b in raw:
                st = b.get("fromDate", "")
                et = b.get("toDate", "")
                # Extract HH:MM from "YYYY-MM-DD HH:MM:SS"
                if len(st) >= 16:
                    bookings_simple.append({
                        "start_time": st[11:16],
                        "end_time":   et[11:16] if len(et) >= 16 else close_h,
                    })
            slots = compute_open_slots(bookings_simple, open_h, close_h, min_hours)
            lib_slots[space_name] = [format_slot(s, e) for s, e in slots]

        if lib_slots:
            results[lib_name] = lib_slots

    return results


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

def print_availability_table(avail: dict, target_date: date) -> None:
    """Print a formatted table of open slots."""
    if not avail:
        print(f"No open slots found for {target_date}.")
        return

    print(f"\nAvailability for {target_date} ({target_date.strftime('%A')})\n")
    print(f"{'Date':<12}{'Library':<18}{'Room':<28}{'Open slots'}")
    print("-" * 80)
    for lib_name, spaces in sorted(avail.items()):
        for space_name, slots in sorted(spaces.items()):
            if slots:
                slot_str = ", ".join(slots)
            else:
                slot_str = "(fully booked)"
            print(f"{str(target_date):<12}{lib_name:<18}{space_name:<28}{slot_str}")


def save_snapshot(avail: dict, target_date: date) -> None:
    """Save availability snapshot to data/availability/YYYY-MM-DD.json."""
    AVAIL_DIR.mkdir(parents=True, exist_ok=True)
    path = AVAIL_DIR / f"{target_date.isoformat()}.json"
    snapshot = {
        "snapshot_date": datetime.utcnow().date().isoformat(),
        "snapshot_time": datetime.utcnow().strftime("%H:%M:%S"),
        "query_date":    target_date.isoformat(),
        "spaces": {},
    }
    for lib_name, spaces in avail.items():
        lib_cfg = LIBRARIES.get(lib_name, {})
        for space_name, slots in spaces.items():
            space_id = lib_cfg.get("spaces", {}).get(space_name)
            snapshot["spaces"][str(space_id)] = {
                "library":    lib_name,
                "space_name": space_name,
                "open_slots": slots,
            }
    path.write_text(json.dumps(snapshot, indent=2))
    print(f"\nSnapshot saved to {path}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check real-time KCLS meeting room availability"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--date", help="Check a specific date (YYYY-MM-DD)")
    group.add_argument("--saturdays", action="store_true", help="Check upcoming Saturdays")

    parser.add_argument(
        "--weeks",
        type=int,
        default=4,
        help="Number of weeks ahead to check (with --saturdays, default: 4)",
    )
    parser.add_argument(
        "--library",
        default="all",
        help='Library name(s), comma-separated, or "all" (default: all)',
    )
    parser.add_argument(
        "--min-hours",
        type=float,
        default=0,
        help="Only show slots at least this many hours long (default: 0)",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Save availability snapshots to data/availability/",
    )
    args = parser.parse_args()

    if args.date:
        try:
            target = date.fromisoformat(args.date)
        except ValueError:
            print(f"Invalid date: {args.date}  (expected YYYY-MM-DD)")
            return
        avail = get_availability_for_date(target, args.library, args.min_hours)
        print_availability_table(avail, target)
        if args.save:
            save_snapshot(avail, target)

    else:  # --saturdays
        today = date.today()
        # Find next Saturday
        days_until_sat = (5 - today.weekday()) % 7
        if days_until_sat == 0:
            days_until_sat = 7
        first_sat = today + timedelta(days=days_until_sat)
        saturdays = [first_sat + timedelta(weeks=w) for w in range(args.weeks)]

        for sat in saturdays:
            avail = get_availability_for_date(sat, args.library, args.min_hours)
            print_availability_table(avail, sat)
            if args.save:
                save_snapshot(avail, sat)


if __name__ == "__main__":
    main()
