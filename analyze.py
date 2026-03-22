#!/usr/bin/env python3
"""
KCLS Meeting Room Analyzer.

Reads data/bookings/bookings.csv and generates pattern reports.

Usage:
  uv run analyze.py
  uv run analyze.py --csv data/bookings/bookings.csv --out data/reports
"""

import argparse
import json
import logging
import os
from datetime import datetime
from pathlib import Path

import pandas as pd

from scraper import LIBRARIES

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
DATA_DIR = Path("data")
CSV_PATH = DATA_DIR / "bookings" / "bookings.csv"
REPORT_DIR = DATA_DIR / "reports"

# Saturday availability thresholds
THRESH_OPEN = 0.30  # pct_booked < 30% → often available
THRESH_BUSY = 0.70  # pct_booked > 70% → usually taken

# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------

_EMPTY_COLUMNS = [
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


def load_bookings(csv_path: Path) -> pd.DataFrame:
    """Load the bookings CSV into a DataFrame with parsed types.

    Args:
        csv_path: Path to the bookings CSV file.

    Returns:
        DataFrame with parsed date columns, numeric columns, and a ``start_hour`` column.
        Returns an empty DataFrame with the correct schema if the file does not exist.
    """
    if not csv_path.exists():
        logger.warning("%s not found — returning empty DataFrame", csv_path)
        return pd.DataFrame(columns=_EMPTY_COLUMNS)
    df = pd.read_csv(csv_path, dtype=str)
    df["booking_date"] = pd.to_datetime(df["booking_date"], errors="coerce")
    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")
    df["fetch_date"] = pd.to_datetime(df["fetch_date"], errors="coerce")
    df["duration_hrs"] = pd.to_numeric(df["duration_hrs"], errors="coerce")
    df["lead_days"] = pd.to_numeric(df["lead_days"], errors="coerce")
    df["space_id"] = pd.to_numeric(df["space_id"], errors="coerce").astype("Int64")
    df["start_hour"] = df["start_time"].str.extract(r"^(\d+):", expand=False).astype("Int64")
    return df


# ---------------------------------------------------------------------------
# Day × hour heatmap
# ---------------------------------------------------------------------------

DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def compute_day_hour_frequency(df: pd.DataFrame) -> pd.DataFrame:
    """Compute a day-of-week × start-hour booking count matrix.

    Args:
        df: Bookings DataFrame from :func:`load_bookings`.

    Returns:
        Pivot table with day-of-week rows and hour columns, or empty DataFrame.
    """
    if df.empty:
        return pd.DataFrame()
    grp = df.dropna(subset=["start_hour"]).groupby(["day_of_week", "start_hour"]).size().reset_index(name="count")
    pivot = grp.pivot(index="day_of_week", columns="start_hour", values="count").fillna(0)
    return pivot.reindex([d for d in DAY_ORDER if d in pivot.index])


# ---------------------------------------------------------------------------
# Lead time distribution
# ---------------------------------------------------------------------------


def compute_lead_time_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """Compute per-library lead time statistics.

    Args:
        df: Bookings DataFrame from :func:`load_bookings`.

    Returns:
        DataFrame with columns: library, n, median_days, p25, p75, p90, pct_same_day.
    """
    valid = df.dropna(subset=["lead_days"])
    if valid.empty:
        return pd.DataFrame()
    rows = []
    for lib, grp in valid.groupby("library"):
        ld = grp["lead_days"]
        rows.append(
            {
                "library": lib,
                "n": len(ld),
                "median_days": round(ld.median(), 1),
                "p25": round(ld.quantile(0.25), 1),
                "p75": round(ld.quantile(0.75), 1),
                "p90": round(ld.quantile(0.90), 1),
                "pct_same_day": round((ld == 0).mean() * 100, 1),
            }
        )
    return pd.DataFrame(rows).sort_values("library")


# ---------------------------------------------------------------------------
# Saturday availability windows
# ---------------------------------------------------------------------------


def _slot_booked(slot_hour: int, start_time_str: str, end_time_str: str) -> bool:
    """Return True if the 1-hour slot starting at ``slot_hour`` overlaps the booking.

    Args:
        slot_hour: Hour of the slot (e.g. 11 for 11:00–12:00).
        start_time_str: Booking start time as ``HH:MM``.
        end_time_str: Booking end time as ``HH:MM``.

    Returns:
        ``True`` if the booking overlaps the slot window.
    """
    try:
        bstart_h, bstart_m = map(int, start_time_str.split(":"))
        bend_h, bend_m = map(int, end_time_str.split(":"))
    except (ValueError, AttributeError):
        return False
    slot_start = slot_hour * 60
    slot_end = slot_start + 60
    b_start = bstart_h * 60 + bstart_m
    b_end = bend_h * 60 + bend_m
    return b_start < slot_end and b_end > slot_start


def compute_saturday_windows(df: pd.DataFrame, libraries: dict[str, dict]) -> dict[str, dict]:
    """Compute per-hour Saturday booking rates for each library/space.

    Args:
        df: Bookings DataFrame from :func:`load_bookings`.
        libraries: Library configuration dict (same structure as ``LIBRARIES``).

    Returns:
        Nested dict: ``{library: {space_name: {hour_str: {pct_booked, n_saturdays, n_booked}}}}``.
    """
    sat_df = df[df["day_of_week"] == "Saturday"].copy()
    all_sats = sorted(df[df["day_of_week"] == "Saturday"]["booking_date"].dt.date.dropna().unique())
    n_saturdays = len(all_sats)
    result: dict[str, dict] = {}

    for lib_name, lib_cfg in libraries.items():
        sat_open_str, sat_close_str = lib_cfg.get("saturday_hours", ("11:00", "18:00"))
        open_h = int(sat_open_str.split(":")[0])
        close_h = int(sat_close_str.split(":")[0])
        slot_hours = list(range(open_h, close_h))

        lib_result: dict[str, dict] = {}
        for space_name, space_id in lib_cfg.get("spaces", {}).items():
            if not space_id:
                continue
            sp_df = sat_df[sat_df["space_id"] == space_id]
            hour_stats: dict[str, dict] = {}
            for h in slot_hours:
                if n_saturdays == 0:
                    hour_stats[f"{h:02d}:00"] = {"pct_booked": None, "n_saturdays": 0, "n_booked": 0}
                    continue
                n_booked = sum(
                    any(
                        _slot_booked(h, row["start_time"], row["end_time"])
                        for _, row in sp_df[sp_df["booking_date"].dt.date == sat].iterrows()
                    )
                    for sat in all_sats
                )
                pct = round(n_booked / n_saturdays, 4)
                hour_stats[f"{h:02d}:00"] = {"pct_booked": pct, "n_saturdays": n_saturdays, "n_booked": n_booked}
            lib_result[space_name] = hour_stats
        result[lib_name] = lib_result
    return result


# ---------------------------------------------------------------------------
# Report formatting helpers
# ---------------------------------------------------------------------------


def _fmt_hour(h_str: str) -> str:
    """Format an ``HH:MM`` string as a human-readable am/pm label.

    Args:
        h_str: Hour string like ``"11:00"`` or ``"13:00"``.

    Returns:
        Label like ``"11am"`` or ``"1pm"``.
    """
    h = int(h_str.split(":")[0])
    if h == 0:
        return "12am"
    if h < 12:
        return f"{h}am"
    if h == 12:
        return "12pm"
    return f"{h - 12}pm"


def _status_icon(pct: float | None) -> str:
    """Return a status emoji + label for a booking percentage.

    Args:
        pct: Fraction of slots booked (0.0–1.0), or ``None`` if unknown.

    Returns:
        Status string with emoji.
    """
    if pct is None:
        return "—"
    if pct < THRESH_OPEN:
        return "✅ Often available"
    if pct > THRESH_BUSY:
        return "⚠️ Usually taken"
    return "🟡 Moderate demand"


def _pct_str(pct: float | None) -> str:
    """Format a fraction as a percentage string.

    Args:
        pct: Fraction (0.0–1.0), or ``None``.

    Returns:
        String like ``"42%"`` or ``"n/a"``.
    """
    return "n/a" if pct is None else f"{round(pct * 100)}%"


# ---------------------------------------------------------------------------
# Markdown report
# ---------------------------------------------------------------------------


def generate_report(
    df: pd.DataFrame,
    saturday_windows: dict[str, dict],
    lead_times: pd.DataFrame,
    heatmap: pd.DataFrame,
    libraries: dict[str, dict],
) -> str:
    """Generate the full Markdown pattern report.

    Args:
        df: Bookings DataFrame.
        saturday_windows: Output of :func:`compute_saturday_windows`.
        lead_times: Output of :func:`compute_lead_time_distribution`.
        heatmap: Output of :func:`compute_day_hour_frequency`.
        libraries: Library configuration dict.

    Returns:
        Markdown string ready to write to ``report.md``.
    """
    lines: list[str] = []
    today_str = datetime.utcnow().strftime("%Y-%m-%d")
    n_total = len(df)
    n_missing_created = int(df["created_date"].isna().sum())

    date_min = df["booking_date"].min()
    date_max = df["booking_date"].max()
    date_range_str = (
        f"{date_min.date()} to {date_max.date()}"
        if not df.empty and pd.notna(date_min) and pd.notna(date_max)
        else "no data"
    )
    libs_covered: list[str] = sorted(df["library"].dropna().unique().tolist()) if not df.empty else []

    lines.append("# KCLS Room Monitor Report")
    lines.append(f"*Generated: {today_str} UTC*\n")

    # 1. Dataset summary
    lines.append("## Dataset Summary")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Total records | {n_total:,} |")
    lines.append(f"| Date range | {date_range_str} |")
    lines.append(f"| Libraries | {', '.join(libs_covered) if libs_covered else 'none'} |")
    pct_missing = round(n_missing_created / n_total * 100) if n_total else 0
    lines.append(f"| Missing `created` (affects lead time) | {n_missing_created:,} ({pct_missing}%) |")
    lines.append("")

    # 2. Booking volume by day of week
    lines.append("## Booking Volume by Day of Week")
    if not df.empty:
        dow_counts = df["day_of_week"].value_counts().reindex(DAY_ORDER).fillna(0).astype(int)
        lines.append("| Day | Bookings |")
        lines.append("|-----|---------|")
        for day, count in dow_counts.items():
            lines.append(f"| {day} | {count:,} |")
    else:
        lines.append("*No data yet.*")
    lines.append("")

    # 3. Booking volume by hour
    lines.append("## Booking Volume by Hour (All Libraries)")
    if not df.empty and "start_hour" in df.columns:
        hour_counts = df.dropna(subset=["start_hour"]).groupby("start_hour").size().sort_index()
        lines.append("| Hour | Bookings |")
        lines.append("|------|---------|")
        for h, cnt in hour_counts.items():
            lines.append(f"| {_fmt_hour(f'{int(h):02d}:00')} | {cnt:,} |")
    else:
        lines.append("*No data yet.*")
    lines.append("")

    # 4. Lead time distribution
    lines.append("## Booking Lead Times")
    lines.append("*How far in advance meeting rooms are typically reserved:*\n")
    if not lead_times.empty:
        lines.append("| Library | Median days | p25 | p75 | p90 | % same-day | N |")
        lines.append("|---------|------------|-----|-----|-----|------------|---|")
        for _, row in lead_times.iterrows():
            lines.append(
                f"| {row['library']} | {row['median_days']} | {row['p25']} | "
                f"{row['p75']} | {row['p90']} | {row['pct_same_day']}% | {int(row['n'])} |"
            )
        lines.append(f"\n*Based on {int(lead_times['n'].sum()):,} bookings with valid `created` timestamps.*")
    else:
        lines.append("*Not enough data yet (need bookings with `created` timestamps).*")
    lines.append("")

    # 5. Day × hour heatmap
    lines.append("## Day × Hour Heatmap (Booking Counts)")
    if not heatmap.empty:
        hour_cols = sorted(heatmap.columns.tolist())
        header = "| Day | " + " | ".join(_fmt_hour(f"{int(h):02d}:00") for h in hour_cols) + " |"
        sep = "|-----|" + "|".join(["----"] * len(hour_cols)) + "|"
        lines.append(header)
        lines.append(sep)
        for day in heatmap.index:
            row_vals = " | ".join(str(int(heatmap.loc[day, h])) for h in hour_cols)
            lines.append(f"| {day} | {row_vals} |")
    else:
        lines.append("*No data yet.*")
    lines.append("")

    # 6. Saturday availability windows
    n_saturdays_global = (
        len(df[df["day_of_week"] == "Saturday"]["booking_date"].dt.date.dropna().unique()) if not df.empty else 0
    )
    lines.append("## Saturday Availability Windows")
    if n_saturdays_global:
        sat_dates = sorted(df[df["day_of_week"] == "Saturday"]["booking_date"].dt.date.dropna().unique())
        lines.append(f"*Based on {n_saturdays_global} Saturdays observed ({sat_dates[0]} to {sat_dates[-1]}):*\n")
        for lib_name, spaces in saturday_windows.items():
            if not spaces:
                continue
            lines.append(f"### {lib_name.title()}")
            for space_name, hour_stats in spaces.items():
                if not hour_stats:
                    continue
                lines.append(f"**{space_name}**\n")
                lines.append("| Hour | Booking rate | Status |")
                lines.append("|------|-------------|--------|")
                for h_str, stats in sorted(hour_stats.items()):
                    pct = stats["pct_booked"]
                    lines.append(f"| {_fmt_hour(h_str)} | {_pct_str(pct)} | {_status_icon(pct)} |")
                lines.append("")
            if not lead_times.empty:
                lib_lt = lead_times[lead_times["library"] == lib_name]
                if not lib_lt.empty:
                    r = lib_lt.iloc[0]
                    lines.append(
                        f"**Typical lead time at {lib_name.title()}:** "
                        f"median {r['median_days']} days, p90 {r['p90']} days\n"
                    )
    else:
        lines.append("*Not enough Saturday data yet (need at least 1 Saturday observed).*")
    lines.append("")

    # 7. Booking frequency by library
    lines.append("## Booking Frequency by Library")
    if not df.empty:
        lib_counts = df.groupby("library").size().sort_values(ascending=False)
        lines.append("| Library | Bookings |")
        lines.append("|---------|---------|")
        for lib, cnt in lib_counts.items():
            lines.append(f"| {lib} | {cnt:,} |")
    else:
        lines.append("*No data yet.*")
    lines.append("")

    # 8. Data quality notes
    lines.append("## Data Quality Notes")
    lines.append(f"- Total records: {n_total:,}")
    lines.append(f"- Records missing `created` timestamp: {n_missing_created:,}")
    if n_total:
        coverage = round((n_total - n_missing_created) / n_total * 100)
        lines.append(f"- Lead time coverage: {coverage}% of records have valid lead time data")
    lines.append("")

    return os.linesep.join(lines)


# ---------------------------------------------------------------------------
# Output writers
# ---------------------------------------------------------------------------


def write_outputs(df: pd.DataFrame, libraries: dict[str, dict], report_dir: Path) -> None:
    """Compute all analyses and write report files.

    Args:
        df: Bookings DataFrame from :func:`load_bookings`.
        libraries: Library configuration dict.
        report_dir: Directory to write output files into.
    """
    report_dir.mkdir(parents=True, exist_ok=True)

    heatmap = compute_day_hour_frequency(df)
    lead_times = compute_lead_time_distribution(df)
    sat_windows = compute_saturday_windows(df, libraries)
    report_md = generate_report(df, sat_windows, lead_times, heatmap, libraries)

    try:
        (report_dir / "report.md").write_text(report_md, encoding="utf-8")
        logger.info("Wrote %s", report_dir / "report.md")

        if not heatmap.empty:
            heatmap.to_csv(report_dir / "heatmap.csv")
            logger.info("Wrote %s", report_dir / "heatmap.csv")

        if not lead_times.empty:
            lead_times.to_csv(report_dir / "lead_times.csv", index=False)
            logger.info("Wrote %s", report_dir / "lead_times.csv")

        (report_dir / "saturday_windows.json").write_text(json.dumps(sat_windows, indent=2), encoding="utf-8")
        logger.info("Wrote %s", report_dir / "saturday_windows.json")

        n_total = len(df)
        n_missing = int(df["created_date"].isna().sum()) if not df.empty else 0
        summary = {
            "generated_at": datetime.utcnow().isoformat(),
            "total_records": n_total,
            "missing_created": n_missing,
            "libraries": sorted(df["library"].dropna().unique().tolist()) if not df.empty else [],
            "date_range": {
                "min": df["booking_date"].min().date().isoformat()
                if not df.empty and pd.notna(df["booking_date"].min())
                else None,
                "max": df["booking_date"].max().date().isoformat()
                if not df.empty and pd.notna(df["booking_date"].max())
                else None,
            },
            "saturday_windows": sat_windows,
            "lead_time_summary": lead_times.to_dict(orient="records") if not lead_times.empty else [],
        }
        (report_dir / "summary.json").write_text(json.dumps(summary, indent=2, default=str), encoding="utf-8")
        logger.info("Wrote %s", report_dir / "summary.json")

    except OSError:
        logger.exception("Failed to write report outputs to %s", report_dir)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Parse CLI arguments and run the analyzer."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    parser = argparse.ArgumentParser(description="KCLS booking pattern analyzer")
    parser.add_argument("--csv", default=str(CSV_PATH), help="Path to bookings CSV")
    parser.add_argument("--out", default=str(REPORT_DIR), help="Output directory for reports")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    report_dir = Path(args.out)

    logger.info("Loading bookings from %s", csv_path)
    df = load_bookings(csv_path)
    logger.info("%d records loaded.", len(df))

    write_outputs(df, LIBRARIES, report_dir)
    logger.info("Done.")


if __name__ == "__main__":
    main()
