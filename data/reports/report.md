# KCLS Room Monitor Report
*Generated: 2026-06-28 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 33,654 |
| Date range | 2026-03-22 to 2026-07-26 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (14%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 5,774 |
| Tuesday | 6,298 |
| Wednesday | 5,986 |
| Thursday | 2,447 |
| Friday | 5,590 |
| Saturday | 3,650 |
| Sunday | 3,909 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,083 |
| 11am | 4,427 |
| 12pm | 4,520 |
| 1pm | 4,540 |
| 2pm | 4,342 |
| 3pm | 4,346 |
| 4pm | 4,612 |
| 5pm | 2,951 |
| 6pm | 1,197 |
| 7pm | 636 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 24947 (21245 / 3702) |
| issaquah | 28.0 | 8.0 | 28.0 | 28.0 | 15.1% | 205 (173 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 18.6% | 215 (186 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.4% | 5316 (4464 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 2789 (2611 / 178) |
| woodinville | 26.0 | 3.2 | 28.0 | 28.0 | 22.0% | 182 (152 / 30) |

*33,654 bookings total — 28,831 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 758 | 547 | 634 | 869 | 838 | 831 | 862 | 435 | 0 | 0 |
| Tuesday | 0 | 655 | 900 | 811 | 797 | 787 | 781 | 639 | 607 | 321 |
| Wednesday | 0 | 735 | 843 | 687 | 691 | 715 | 779 | 631 | 590 | 315 |
| Thursday | 421 | 223 | 278 | 321 | 312 | 328 | 370 | 194 | 0 | 0 |
| Friday | 904 | 694 | 728 | 734 | 719 | 739 | 698 | 374 | 0 | 0 |
| Saturday | 0 | 701 | 523 | 528 | 512 | 470 | 557 | 359 | 0 | 0 |
| Sunday | 0 | 872 | 614 | 590 | 473 | 476 | 565 | 319 | 0 | 0 |

## Saturday Availability Windows
*Based on 17 Saturdays observed (2026-03-28 to 2026-07-25):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 71% | ⚠️ Usually taken |
| 12pm | 65% | 🟡 Moderate demand |
| 1pm | 59% | 🟡 Moderate demand |
| 2pm | 35% | 🟡 Moderate demand |
| 3pm | 29% | ✅ Often available |
| 4pm | 71% | ⚠️ Usually taken |
| 5pm | 82% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 82% | ⚠️ Usually taken |
| 3pm | 82% | ⚠️ Usually taken |
| 4pm | 82% | ⚠️ Usually taken |
| 5pm | 82% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 53% | 🟡 Moderate demand |
| 12pm | 18% | ✅ Often available |
| 1pm | 18% | ✅ Often available |
| 2pm | 18% | ✅ Often available |
| 3pm | 24% | ✅ Often available |
| 4pm | 29% | ✅ Often available |
| 5pm | 76% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 26.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 65% | 🟡 Moderate demand |
| 12pm | 47% | 🟡 Moderate demand |
| 1pm | 18% | ✅ Often available |
| 2pm | 29% | ✅ Often available |
| 3pm | 35% | 🟡 Moderate demand |
| 4pm | 41% | 🟡 Moderate demand |
| 5pm | 71% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 41% | 🟡 Moderate demand |
| 12pm | 41% | 🟡 Moderate demand |
| 1pm | 47% | 🟡 Moderate demand |
| 2pm | 24% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 47% | 🟡 Moderate demand |
| 5pm | 47% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 24,947 |
| redmond | 5,316 |
| sammamish | 2,789 |
| kingsgate | 215 |
| issaquah | 205 |
| woodinville | 182 |

## Data Quality Notes
- Total records: 33,654
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 28,831
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 86% fresh — grows toward 100% as initial batch ages out
