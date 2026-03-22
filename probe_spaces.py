#!/usr/bin/env python3
"""
KCLS Space ID Discovery.

Scans LibCal space ID ranges to find all KCLS meeting rooms.
Run once (or periodically) to populate data/space_catalog.json.

Usage:
  uv run probe_spaces.py
  uv run probe_spaces.py --ranges 17215-17285,134480-134515
  uv run probe_spaces.py --dry-run
"""

import argparse
import json
import logging
import time
from pathlib import Path

import requests
import requests.exceptions

logger = logging.getLogger(__name__)

BASE_URL = "https://rooms.kcls.org"
ITEM_API = BASE_URL + "/api/1.1/space/item/{}"
CATALOG_PATH = Path("data") / "space_catalog.json"

# Known KCLS ID ranges — extend as new rooms are added
DEFAULT_RANGES = [
    range(17215, 17286),   # original LibCal setup
    range(134480, 134516), # later additions (e.g. Sammamish Sunset Room)
    range(176320, 176341), # possible future additions
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
    """Query the LibCal space metadata endpoint for a single ID.

    Args:
        space_id: Candidate LibCal space identifier.

    Returns:
        Metadata dict if the ID is valid, ``None`` otherwise.
    """
    url = ITEM_API.format(space_id)
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code == 429:
            logger.warning("Rate limited at %s, waiting 30s...", space_id)
            time.sleep(30)
            resp = requests.get(url, headers=HEADERS, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json()
        space = data.get("space") or data.get("item")
        if not space:
            return None
        return {
            "space_id": space_id,
            "name": space.get("name") or space.get("title"),
            "capacity": space.get("capacity"),
            "lid": space.get("lid"),
            "cid": space.get("cid"),
            "description": (space.get("description") or "")[:200],
        }
    except requests.exceptions.Timeout:
        logger.exception("Timeout probing space %s", space_id)
        return None
    except requests.exceptions.ConnectionError:
        logger.exception("Connection error probing space %s", space_id)
        return None
    except (requests.exceptions.RequestException, ValueError):
        logger.exception("Request error probing space %s", space_id)
        return None


def parse_ranges(ranges_str: str) -> list[range]:
    """Parse a comma-separated range string into a list of ranges.

    Args:
        ranges_str: String like ``"17215-17285,134480-134515"``.

    Returns:
        List of ``range`` objects (end-inclusive).
    """
    result: list[range] = []
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
    """Parse CLI arguments and scan for valid KCLS space IDs."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description="Discover KCLS LibCal space IDs")
    parser.add_argument("--ranges", default=None, help="Comma-separated ID ranges, e.g. '17215-17285,134480-134515'")
    parser.add_argument("--dry-run", action="store_true", help="Print IDs that would be scanned without requesting")
    args = parser.parse_args()

    ranges = parse_ranges(args.ranges) if args.ranges else DEFAULT_RANGES
    total_ids = sum(len(r) for r in ranges)

    if args.dry_run:
        print(f"Would probe {total_ids} space IDs:")
        for r in ranges:
            print(f"  {r.start}–{r.stop - 1}  ({len(r)} IDs)")
        return

    logger.info("Probing %d space IDs across %d ranges (~%.0fs)", total_ids, len(ranges), total_ids * PROBE_DELAY)

    existing: dict[str, dict] = {}
    if CATALOG_PATH.exists():
        try:
            existing = json.loads(CATALOG_PATH.read_text())
            logger.info("Loaded %d existing entries from %s", len(existing), CATALOG_PATH)
        except (OSError, json.JSONDecodeError):
            logger.exception("Failed to load existing catalog from %s", CATALOG_PATH)

    found: dict[str, dict] = dict(existing)

    for r in ranges:
        logger.info("Scanning %d–%d...", r.start, r.stop - 1)
        for space_id in r:
            key = str(space_id)
            if key in found:
                logger.debug("%s: already known — %s", space_id, found[key]["name"])
                continue
            time.sleep(PROBE_DELAY)
            result = probe_space(space_id)
            if result:
                found[key] = result
                logger.info("FOUND %s: %s  (lid=%s, cap=%s)", space_id, result["name"], result["lid"], result["capacity"])
            else:
                logger.debug("%s: not a valid space", space_id)

    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    try:
        CATALOG_PATH.write_text(json.dumps(found, indent=2))
    except OSError:
        logger.exception("Failed to write catalog to %s", CATALOG_PATH)
        return

    new_count = len(found) - len(existing)
    logger.info("Done. %d total spaces (%d new). Saved to %s", len(found), new_count, CATALOG_PATH)

    by_lid: dict[str, list[dict]] = {}
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
