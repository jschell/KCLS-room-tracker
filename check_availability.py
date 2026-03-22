#!/usr/bin/env python3
"""
KCLS Meeting Room Availability Checker.

Real-time slot checker: queries the LibCal API and shows open time windows.

Usage:
  uv run check_availability.py --date 2026-04-05
  uv run check_availability.py --date 2026-04-05 --library redmond
  uv run check_availability.py --saturdays --weeks 4
  uv run check_availability.py --saturdays --weeks 4 --min-hours 2
"""

import argparse
import json
import logging
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import requests.exceptions

from scraper import LIBRARIES, REQUEST_DELAY, fetch_bookings_api

logger = logging.getLogger(__name__)

AVAIL_DIR = Path("data") / "availability"


# ---------------------------------------------------------------------------
# Time interval helpers
# ---------------------------------------------------------------------------


def _hhmm_to_mins(hhmm: str) -> int:
    """Convert an ``HH:MM`` string to minutes since midnight.

    Args:
        hhmm: Time string like ``"11:30"``.

    Returns:
        Integer minutes (e.g. 690 for ``"11:30"``).
    """
    h, m = map(int, hhmm.split(":"))
    return h * 60 + m


def _mins_to_ampm(mins: int) -> str:
    """Convert minutes since midnight to a human-readable am/pm string.

    Args:
        mins: Minutes since midnight.

    Returns:
        String like ``"11am"`` or ``"1:30pm"``.
    """
    h = mins // 60
    m = mins % 60
    suffix = "am" if h < 12 else "pm"
    display_h = 12 if h in (0, 12) else h % 12
    return f"{display_h}:{m:02d}{suffix}" if m else f"{display_h}{suffix}"


def compute_open_slots(
    bookings: list[dict],
    open_hhmm: str,
    close_hhmm: str,
    min_hours: float = 0,
) -> list[tuple[int, int]]:
    """Compute open time windows by subtracting confirmed bookings from open hours.

    Args:
        bookings: List of booking dicts with ``start_time`` and ``end_time`` as ``HH:MM``.
        open_hhmm: Library open time as ``HH:MM``.
        close_hhmm: Library close time as ``HH:MM``.
        min_hours: Only return windows at least this many hours long.

    Returns:
        List of ``(start_mins, end_mins)`` tuples representing free windows.
    """
    open_min = _hhmm_to_mins(open_hhmm)
    close_min = _hhmm_to_mins(close_hhmm)

    booked: list[list[int]] = []
    for b in bookings:
        try:
            bs = _hhmm_to_mins(b.get("start_time", "00:00"))
            be = _hhmm_to_mins(b.get("end_time", "00:00"))
        except (ValueError, AttributeError):
            continue
        bs = max(bs, open_min)
        be = min(be, close_min)
        if be > bs:
            booked.append([bs, be])

    booked.sort(key=lambda x: x[0])
    merged: list[list[int]] = []
    for interval in booked:
        if merged and interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append([interval[0], interval[1]])

    free: list[tuple[int, int]] = []
    cursor = open_min
    for bs, be in merged:
        if bs > cursor:
            free.append((cursor, bs))
        cursor = max(cursor, be)
    if cursor < close_min:
        free.append((cursor, close_min))

    min_mins = int(min_hours * 60)
    return [(s, e) for s, e in free if e - s >= min_mins]


def format_slot(start_min: int, end_min: int) -> str:
    """Format a time window as a human-readable range string.

    Args:
        start_min: Window start in minutes since midnight.
        end_min: Window end in minutes since midnight.

    Returns:
        String like ``"11am–1pm"``.
    """
    return f"{_mins_to_ampm(start_min)}–{_mins_to_ampm(end_min)}"


# ---------------------------------------------------------------------------
# Per-date availability fetch
# ---------------------------------------------------------------------------


def get_availability_for_date(
    target_date: date,
    libraries_filter: str = "all",
    min_hours: float = 0,
) -> dict[str, dict[str, list[str]]]:
    """Fetch real-time availability for all spaces on a single date.

    Args:
        target_date: The date to check.
        libraries_filter: Comma-separated library names, or ``"all"``.
        min_hours: Only include windows at least this many hours long.

    Returns:
        Nested dict: ``{library: {space_name: [open_slot_strings]}}``.
    """
    if libraries_filter == "all":
        scope = LIBRARIES
    else:
        keys = [k.strip() for k in libraries_filter.split(",")]
        scope = {k: LIBRARIES[k] for k in keys if k in LIBRARIES}

    date_str = target_date.isoformat()
    dow = target_date.strftime("%A")
    results: dict[str, dict[str, list[str]]] = {}

    for lib_name, lib_cfg in scope.items():
        spaces: dict[str, int | None] = lib_cfg.get("spaces", {})
        if not spaces:
            continue

        if dow == "Saturday":
            open_h, close_h = lib_cfg.get("saturday_hours", ("11:00", "18:00"))
        elif dow == "Sunday":
            if not lib_cfg.get("sunday_open", False):
                continue
            open_h, close_h = lib_cfg.get("sunday_hours", ("11:00", "18:00"))
        else:
            open_h, close_h = lib_cfg.get("weekday_hours", ("10:00", "18:00"))

        lib_slots: dict[str, list[str]] = {}
        for space_name, space_id in spaces.items():
            if not space_id:
                continue
            time.sleep(REQUEST_DELAY)
            raw = fetch_bookings_api(space_id, date_str)
            bookings_simple = [
                {
                    "start_time": b.get("fromDate", "")[11:16],
                    "end_time": b.get("toDate", "")[11:16] or close_h,
                }
                for b in raw
                if len(b.get("fromDate", "")) >= 16
            ]
            slots = compute_open_slots(bookings_simple, open_h, close_h, min_hours)
            lib_slots[space_name] = [format_slot(s, e) for s, e in slots]

        if lib_slots:
            results[lib_name] = lib_slots

    return results


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------


def print_availability_table(avail: dict[str, dict[str, list[str]]], target_date: date) -> None:
    """Print a formatted table of open slots to stdout.

    Args:
        avail: Output of :func:`get_availability_for_date`.
        target_date: The date the availability data is for.
    """
    if not avail:
        print(f"No open slots found for {target_date}.")
        return

    print(f"\nAvailability for {target_date} ({target_date.strftime('%A')})\n")
    print(f"{'Date':<12}{'Library':<18}{'Room':<28}{'Open slots'}")
    print("-" * 80)
    for lib_name, spaces in sorted(avail.items()):
        for space_name, slots in sorted(spaces.items()):
            slot_str = ", ".join(slots) if slots else "(fully booked)"
            print(f"{str(target_date):<12}{lib_name:<18}{space_name:<28}{slot_str}")


def save_snapshot(avail: dict[str, dict[str, list[str]]], target_date: date) -> None:
    """Save an availability snapshot to ``data/availability/YYYY-MM-DD.json``.

    Args:
        avail: Output of :func:`get_availability_for_date`.
        target_date: The date the snapshot covers.
    """
    AVAIL_DIR.mkdir(parents=True, exist_ok=True)
    path = AVAIL_DIR / f"{target_date.isoformat()}.json"
    snapshot: dict = {
        "snapshot_date": datetime.utcnow().date().isoformat(),
        "snapshot_time": datetime.utcnow().strftime("%H:%M:%S"),
        "query_date": target_date.isoformat(),
        "spaces": {},
    }
    for lib_name, spaces in avail.items():
        lib_cfg = LIBRARIES.get(lib_name, {})
        for space_name, slots in spaces.items():
            space_id = lib_cfg.get("spaces", {}).get(space_name)
            snapshot["spaces"][str(space_id)] = {
                "library": lib_name,
                "space_name": space_name,
                "open_slots": slots,
            }
    try:
        path.write_text(json.dumps(snapshot, indent=2))
        logger.info("Snapshot saved to %s", path)
    except OSError:
        logger.exception("Failed to save snapshot to %s", path)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Parse CLI arguments and check real-time availability."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description="Check real-time KCLS meeting room availability")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--date", help="Check a specific date (YYYY-MM-DD)")
    group.add_argument("--saturdays", action="store_true", help="Check upcoming Saturdays")

    parser.add_argument("--weeks", type=int, default=4, help="Weeks ahead to check (with --saturdays, default: 4)")
    parser.add_argument("--library", default="all", help='Library name(s), comma-separated, or "all"')
    parser.add_argument("--min-hours", type=float, default=0, help="Minimum slot length in hours (default: 0)")
    parser.add_argument("--save", action="store_true", help="Save availability snapshots to data/availability/")
    args = parser.parse_args()

    if args.date:
        try:
            target = date.fromisoformat(args.date)
        except ValueError:
            logger.error("Invalid date: %s  (expected YYYY-MM-DD)", args.date)
            return
        avail = get_availability_for_date(target, args.library, args.min_hours)
        print_availability_table(avail, target)
        if args.save:
            save_snapshot(avail, target)
    else:
        today = date.today()
        days_until_sat = (5 - today.weekday()) % 7 or 7
        first_sat = today + timedelta(days=days_until_sat)
        for w in range(args.weeks):
            sat = first_sat + timedelta(weeks=w)
            avail = get_availability_for_date(sat, args.library, args.min_hours)
            print_availability_table(avail, sat)
            if args.save:
                save_snapshot(avail, sat)


if __name__ == "__main__":
    main()
