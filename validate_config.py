#!/usr/bin/env python3
"""
KCLS Library Config Validator.

Checks that every library, lid, gid, and space_id in LIBRARIES still
matches what rooms.kcls.org reports.  Run weekly to catch changes.

Exit code 0 = all OK, 1 = discrepancies found.

Usage:
  uv run validate_config.py
  uv run validate_config.py --fix   # print corrected LIBRARIES snippet
"""

import argparse
import logging
import re
import sys
import time

import requests
import requests.exceptions

from scraper import LIBRARIES

logger = logging.getLogger(__name__)

BASE_URL = "https://rooms.kcls.org"
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
REQUEST_DELAY = 0.4


def fetch_allspaces_lids() -> dict[int, str]:
    """Return a mapping of lid → library name from the /allspaces page.

    Args: None

    Returns:
        Dict of ``{lid: library_name}`` for all active libraries.
    """
    try:
        r = requests.get(f"{BASE_URL}/allspaces", headers=HEADERS, timeout=15)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        logger.exception("Failed to fetch /allspaces")
        return {}
    options = re.findall(r'<option[^>]+value="(\d+)"[^>]*>\s*([^<]+)\s*</option>', r.text)
    return {int(val): name.strip() for val, name in options if int(val) > 0}


def fetch_space_info(space_id: int) -> dict | None:
    """Fetch lid, gid, title, and capacity for a single space from its booking page.

    Retries up to 3 times on timeout with exponential backoff.

    Args:
        space_id: LibCal space identifier.

    Returns:
        Dict with keys ``lid``, ``gid``, ``title``, ``capacity``, or ``None`` on failure.
    """
    url = f"{BASE_URL}/space/{space_id}"
    for attempt in range(3):
        try:
            r = requests.get(url, headers=HEADERS, timeout=20)
            break
        except requests.exceptions.Timeout:
            if attempt < 2:
                wait = 2 ** (attempt + 1)
                logger.warning("Timeout fetching space %s (attempt %d/3), retrying in %ds…",
                               space_id, attempt + 1, wait)
                time.sleep(wait)
            else:
                logger.exception("Timeout fetching space %s after 3 attempts", space_id)
                return None
        except requests.exceptions.ConnectionError:
            logger.exception("Connection error fetching space %s", space_id)
            return None
        except requests.exceptions.RequestException:
            logger.exception("Request error fetching space %s", space_id)
            return None

    if r.status_code != 200:
        logger.warning("HTTP %s for space %s", r.status_code, space_id)
        return None

    lid_m = re.search(r"locationId\s*:\s*(\d+)", r.text)
    gid_m = re.search(r"groupId\s*:\s*(\d+)", r.text)
    title_m = re.search(r'title\s*:\s*"([^"]+Capacity[^"]+)"', r.text)
    cap_m = re.search(r"Capacity\s+(\d+)", r.text)

    if not lid_m:
        logger.warning("Could not parse locationId for space %s (may no longer exist)", space_id)
        return None

    return {
        "lid": int(lid_m.group(1)),
        "gid": int(gid_m.group(1)) if gid_m else None,
        "title": title_m.group(1) if title_m else "",
        "capacity": int(cap_m.group(1)) if cap_m else None,
    }


def validate() -> list[str]:
    """Validate all LIBRARIES entries against live data.

    Returns:
        List of discrepancy strings (empty if everything matches).
    """
    issues: list[str] = []

    logger.info("Fetching current lid→name mapping from /allspaces…")
    live_lids = fetch_allspaces_lids()
    if not live_lids:
        issues.append("FATAL: could not fetch /allspaces — skipping lid name checks")
    else:
        logger.info("Found %d libraries on site.", len(live_lids))

    for lib_name, lib_cfg in LIBRARIES.items():
        lid: int | None = lib_cfg.get("lid")
        cfg_gid: int | None = lib_cfg.get("gid")
        spaces: dict[str, int | None] = lib_cfg.get("spaces", {})
        space_gids: dict[int, int] = lib_cfg.get("space_gids", {})

        if lid is None:
            issues.append(f"{lib_name}: lid is None — not configured")
            continue

        # Check lid still exists and matches expected library name
        if live_lids:
            if lid not in live_lids:
                issues.append(f"{lib_name}: lid={lid} not found on site")
            else:
                live_name = live_lids[lid].lower()
                if lib_name not in live_name and live_name not in lib_name:
                    issues.append(
                        f"{lib_name}: lid={lid} maps to '{live_lids[lid]}' on site "
                        f"— name mismatch (config has '{lib_name}')"
                    )
                else:
                    logger.info("  %s: lid=%s ✓ (%s)", lib_name, lid, live_lids[lid])

        if not spaces:
            logger.info("  %s: no spaces configured — skipping space checks", lib_name)
            continue

        # Validate each space
        for space_name, space_id in spaces.items():
            if not space_id:
                issues.append(f"{lib_name}/{space_name}: space_id is None")
                continue

            time.sleep(REQUEST_DELAY)
            info = fetch_space_info(space_id)

            if info is None:
                issues.append(f"{lib_name}/{space_name}: space_id={space_id} — page not found or parse error")
                continue

            # Check lid matches
            if info["lid"] != lid:
                issues.append(
                    f"{lib_name}/{space_name}: space_id={space_id} has lid={info['lid']} on site, "
                    f"but config says lid={lid}"
                )
            else:
                logger.info("    %s (space_id=%s): lid=%s ✓", space_name, space_id, lid)

            # Check gid: per-space override takes priority
            expected_gid = space_gids.get(space_id, cfg_gid)
            if expected_gid is not None and info["gid"] is not None and info["gid"] != expected_gid:
                issues.append(
                    f"{lib_name}/{space_name}: space_id={space_id} has gid={info['gid']} on site, "
                    f"but config says gid={expected_gid}"
                )
            elif info["gid"] is not None:
                logger.info("    %s (space_id=%s): gid=%s ✓", space_name, space_id, info["gid"])

    return issues


def main() -> None:
    """Parse CLI arguments and run the validator."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description="Validate KCLS LIBRARIES config against live site")
    parser.add_argument("--quiet", action="store_true", help="Only print issues, not progress")
    args = parser.parse_args()

    if args.quiet:
        logging.getLogger().setLevel(logging.WARNING)

    logger.info("Validating LIBRARIES config against %s…", BASE_URL)
    issues = validate()

    if issues:
        print(f"\n{'='*60}")
        print(f"VALIDATION FAILED — {len(issues)} issue(s) found:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        print("=" * 60)
        sys.exit(1)
    else:
        print("\nAll library/space IDs validated successfully ✓")
        sys.exit(0)


if __name__ == "__main__":
    main()
