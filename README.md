# KCLS Meeting Room Monitor

Monitors all King County Library System (KCLS) meeting room availability by scraping the LibCal JSON API at [rooms.kcls.org](https://rooms.kcls.org). Tracks confirmed bookings over time, analyzes booking patterns by day and hour, and identifies how far in advance rooms tend to get reserved.

**Primary use case:** Help community groups find reliably-open Saturday meeting room slots and know how far in advance to book.

---

## What It Does

- **Scrapes** confirmed bookings for all KCLS libraries with reservable meeting rooms (Phase 1: 6 branches; Phase 2: all ~44 branches)
- **Accumulates** an append-only historical CSV dataset committed to this repo
- **Analyzes** booking patterns: which days/hours are most booked, how far in advance rooms get reserved, which Saturday windows tend to stay open
- **Runs automatically** via GitHub Actions twice daily (7am and 3pm Pacific)

---

## Quick Start

### Check real-time availability

```bash
uv sync

# Check availability for a specific date
uv run check_availability.py --date 2026-04-05

# Check all Saturdays for the next 4 weeks, show slots ≥ 2 hours
uv run check_availability.py --saturdays --weeks 4 --min-hours 2

# Check a specific library
uv run check_availability.py --date 2026-04-05 --library redmond
```

### Run the scraper manually

```bash
# Scrape all configured libraries for the next 28 days
uv run scraper.py

# Scrape specific libraries for the next 7 days
uv run scraper.py --days 7 --libraries redmond,sammamish
```

### Generate the analysis report

```bash
uv run analyze.py
# Outputs to data/reports/
```

### Discover space IDs for new branches

```bash
uv run probe_spaces.py
# Scans ID ranges and saves data/space_catalog.json
```

---

## Repository Structure

```
KCLS-room-tracker/
├── .github/workflows/
│   └── monitor.yml          # GitHub Actions: runs scraper + analyzer twice daily
├── data/
│   ├── bookings/
│   │   ├── bookings.csv     # Append-only historical record (committed)
│   │   └── last_run.json    # Metadata from the most recent scrape run
│   ├── availability/        # Optional daily open-slot snapshots (gitignored)
│   └── reports/
│       ├── report.md        # Latest pattern report (posted to Actions summary)
│       ├── summary.json     # Machine-readable stats
│       ├── heatmap.csv      # Day × hour booking frequency matrix
│       ├── lead_times.csv   # Lead time distribution per library
│       └── saturday_windows.json
├── scraper.py               # Main scraper
├── analyze.py               # Pattern analysis and report generation
├── check_availability.py    # Ad-hoc real-time slot checker
├── probe_spaces.py          # One-time space ID discovery tool
└── requirements.txt
```

---

## Data Schema (`bookings.csv`)

| Column | Description |
|--------|-------------|
| `fetch_date` | Date this record was scraped |
| `booking_date` | Date the room is booked for |
| `day_of_week` | Monday–Sunday |
| `library` | Branch name (lowercase) |
| `space_name` | Human-readable room name |
| `space_id` | LibCal space ID |
| `booking_id` | LibCal `bookId` — deduplication key |
| `title` | Booking title (often generic) |
| `start_time` | `HH:MM` |
| `end_time` | `HH:MM` |
| `duration_hrs` | Computed from start/end |
| `created_date` | When the reservation was made |
| `lead_days` | `booking_date - created_date` in days |
| `source` | `api` or `playwright` |

**Key metric:** `lead_days` — how far in advance rooms are booked. Used to answer "how early do I need to book a Saturday slot?"

---

## Configured Libraries (Phase 1)

| Library | space IDs |
|---------|-----------|
| Redmond | East Meeting Room 1 (17228), East Meeting Room 2 (17229), Conference Room (17230) |
| Sammamish | Meeting Room (17254), Sunset Room (134490) |
| Woodinville | Meeting Room (17258) |
| Kingsgate | Meeting Room 1 (17223) |
| Issaquah | Meeting Room (17233) |
| Bellevue | TBD — run `probe_spaces.py` |

Phase 2 will add all remaining ~38 branches after running `probe_spaces.py` to discover their space IDs.

---

## KCLS Reservation Policy (Key Rules)

| Rule | Value |
|------|-------|
| Minimum advance booking | 12 hours |
| Maximum advance booking | 28 days (most branches), up to 12 weeks (some) |
| Group frequency limit | Once per calendar month per group |
| Cancellation | Arrive within 30 min or reservation is cancelled |
| Late bookings (< 72 hrs) | Book online AND call the library |
| Saturday hours | 11am–6pm at most branches |

Full policy: [kcls.org/room-policy](https://kcls.org/room-policy/)

---

## GitHub Actions Workflow

The workflow runs automatically at:
- **7:00 AM Pacific** (`0 15 * * *` UTC)
- **3:00 PM Pacific** (`0 23 * * *` UTC)

Each run:
1. Scrapes all configured libraries for the next 28 days
2. Appends new booking records to `data/bookings/bookings.csv`
3. Runs the analyzer to regenerate all reports
4. Posts `report.md` to the Actions step summary
5. Commits changed data files back to the repo
6. Uploads `data/reports/` as an artifact (retained 90 days)

You can also trigger a manual run from the Actions tab with custom `days` and `libraries` parameters.

---

## Analysis Notes

- **Saturday availability:** Requires at least 6 weeks of data for reliable patterns. `pct_booked < 30%` = often available; `> 70%` = book early.
- **Lead time analysis:** Only includes bookings where the `created` timestamp was returned by the API (some older bookings may be missing this field).
- **Minimum dataset for patterns:** ~6 Saturday observations per library.
