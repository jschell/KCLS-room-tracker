# KCLS Room Monitor Report
*Generated: 2026-07-03 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 35,433 |
| Date range | 2026-03-22 to 2026-07-31 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (14%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 6,158 |
| Tuesday | 6,762 |
| Wednesday | 6,351 |
| Thursday | 2,618 |
| Friday | 5,945 |
| Saturday | 3,650 |
| Sunday | 3,949 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,203 |
| 11am | 4,610 |
| 12pm | 4,741 |
| 1pm | 4,776 |
| 2pm | 4,571 |
| 3pm | 4,588 |
| 4pm | 4,858 |
| 5pm | 3,115 |
| 6pm | 1,287 |
| 7pm | 684 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 26222 (22520 / 3702) |
| issaquah | 28.0 | 7.0 | 28.0 | 28.0 | 16.1% | 217 (185 / 32) |
| kingsgate | 28.0 | 7.5 | 28.0 | 28.0 | 19.4% | 227 (198 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.3% | 5622 (4770 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 2954 (2776 / 178) |
| woodinville | 26.0 | 3.5 | 28.0 | 28.0 | 22.0% | 191 (161 / 30) |

*35,433 bookings total — 30,610 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 807 | 583 | 676 | 926 | 898 | 887 | 918 | 463 | 0 | 0 |
| Tuesday | 0 | 700 | 963 | 870 | 853 | 843 | 838 | 689 | 657 | 349 |
| Wednesday | 0 | 780 | 893 | 725 | 725 | 759 | 829 | 675 | 630 | 335 |
| Thursday | 446 | 243 | 302 | 352 | 332 | 348 | 391 | 204 | 0 | 0 |
| Friday | 950 | 728 | 764 | 779 | 769 | 798 | 754 | 403 | 0 | 0 |
| Saturday | 0 | 701 | 523 | 528 | 512 | 470 | 557 | 359 | 0 | 0 |
| Sunday | 0 | 875 | 620 | 596 | 482 | 483 | 571 | 322 | 0 | 0 |

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
| bellevue | 26,222 |
| redmond | 5,622 |
| sammamish | 2,954 |
| kingsgate | 227 |
| issaquah | 217 |
| woodinville | 191 |

## Data Quality Notes
- Total records: 35,433
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 30,610
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 86% fresh — grows toward 100% as initial batch ages out
