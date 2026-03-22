#!/usr/bin/env python3
"""
KCLS Space ID Discovery
Scans LibCal space ID ranges to find all KCLS meeting rooms.
Run once (or periodically) to populate data/space_catalog.json.

Usage:
  python probe_spaces.py
  python probe_spaces.py --ranges 17215-17285,134480-134515
  python probe_spaces.py --dry-run   # just print what would be scanned
"""

import argparse
import json
import time
from pathlib import Path

import requests

BASE_URL     = "https://rooms.kcls.org"
ITEM_API     = BASE_URL + "/api/1.1/space/item/{}"
CATALOG_PATH = Path("data") / "space_catalog.json"

# Known KCLS ID ranges — extend as new rooms are added
DEFAULT_RANGES = [
    range(17215, 17286),     # original LibCal setup
    range(134480, 134516),   # later additions (e.g. Sammamish Sunset Room)
    range(176320, 176341),   # possible future additions
]

PROBE_DELAY = 0.3  # seconds between requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}


def probe_space(space_id: int) -> dict | None:
    """
    Query /api/1.1/space/item/{space_id}.
    Returns a metadata dict if valid, None otherwise.
    """
    url = ITEM_API.format(space_id)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code == 429:
            print(f"  [429] Rate limited at {space_id}, waiting 30s...")
            time.sleep(30)
            resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json()
        # LibCal returns {"space": {...}} for valid IDs
        space = data.get("space") or data.get("item")
        if not space:
            return None
        return {
            "space_id":  space_id,
            "name":      space.get("name") or space.get("title"),
            "capacity":  space.get("capacity"),
            "lid":       space.get("lid"),
            "cid":       space.get("cid"),
            "image":     space.get("image"),
            "description": (space.get("description") or "")[:200],
        }
    except Exception as e:
        print(f"  [ERROR] {space_id}: {e}")
        return None


def parse_ranges(ranges_str: str) -> list[range]:
    """Parse '17215-17285,134480-134515' → [range(17215,17286), ...]"""
    result = []
    for part in ranges_str.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-", 1)
            result.append(range(int(lo), int(hi) + 1))
        else:
            n = int(part)
            result.append(range(n, n + 1))
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover KCLS LibCal space IDs")
    parser.add_argument(
        "--ranges",
        default=None,
        help="Comma-separated ID ranges to probe, e.g. '17215-17285,134480-134515'",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print IDs that would be scanned without making requests",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        default=True,
        help="Merge results with existing catalog (default: True)",
    )
    args = parser.parse_args()

    ranges = parse_ranges(args.ranges) if args.ranges else DEFAULT_RANGES
    total_ids = sum(len(r) for r in ranges)

    if args.dry_run:
        print(f"Would probe {total_ids} space IDs:")
        for r in ranges:
            print(f"  {r.start}–{r.stop - 1}  ({len(r)} IDs)")
        return

    print(f"Probing {total_ids} space IDs across {len(ranges)} ranges...")
    print(f"(~{total_ids * PROBE_DELAY:.0f}s at {PROBE_DELAY}s/request)\n")

    # Load existing catalog if merging
    existing: dict = {}
    if args.merge and CATALOG_PATH.exists():
        existing = json.loads(CATALOG_PATH.read_text())
        print(f"  Loaded {len(existing)} existing entries from {CATALOG_PATH}")

    found: dict = dict(existing)  # str keys for JSON

    for r in ranges:
        print(f"\nScanning {r.start}–{r.stop - 1}...")
        for space_id in r:
            key = str(space_id)
            if key in found:
                print(f"  {space_id}: already known — {found[key]['name']}")
                continue
            time.sleep(PROBE_DELAY)
            result = probe_space(space_id)
            if result:
                found[key] = result
                print(f"  FOUND {space_id}: {result['name']}  (lid={result['lid']}, cap={result['capacity']})")
            else:
                print(f"  {space_id}: not a valid space")

    # Save results
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(json.dumps(found, indent=2))

    new_count = len(found) - len(existing)
    print(f"\nDone. {len(found)} total spaces ({new_count} new). Saved to {CATALOG_PATH}")

    # Print summary of found spaces grouped by library (lid)
    by_lid: dict = {}
    for meta in found.values():
        lid = str(meta.get("lid", "unknown"))
        by_lid.setdefault(lid, []).append(meta)

    print("\nFound spaces by library (lid):")
    for lid, spaces in sorted(by_lid.items()):
        print(f"  lid={lid}:")
        for s in sorted(spaces, key=lambda x: x["space_id"]):
            print(f"    space_id={s['space_id']:>6}  cap={str(s.get('capacity') or '?'):>4}  {s['name']}")


if __name__ == "__main__":
    main()
