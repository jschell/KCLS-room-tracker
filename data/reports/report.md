# KCLS Room Monitor Report
*Generated: 2026-07-17 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 40,036 |
| Date range | 2026-03-22 to 2026-08-14 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (12%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 6,928 |
| Tuesday | 7,608 |
| Wednesday | 6,955 |
| Thursday | 2,938 |
| Friday | 6,764 |
| Saturday | 4,336 |
| Sunday | 4,507 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,474 |
| 11am | 5,244 |
| 12pm | 5,338 |
| 1pm | 5,353 |
| 2pm | 5,185 |
| 3pm | 5,212 |
| 4pm | 5,508 |
| 5pm | 3,518 |
| 6pm | 1,434 |
| 7pm | 770 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 29522 (25820 / 3702) |
| issaquah | 28.0 | 5.8 | 28.0 | 28.0 | 17.5% | 252 (220 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 20.3% | 261 (232 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.2% | 6447 (5595 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 3336 (3158 / 178) |
| woodinville | 26.5 | 1.0 | 28.0 | 28.0 | 22.9% | 218 (188 / 30) |

*40,036 bookings total — 35,213 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 904 | 656 | 758 | 1043 | 1010 | 1002 | 1034 | 521 | 0 | 0 |
| Tuesday | 0 | 785 | 1078 | 975 | 964 | 959 | 945 | 772 | 736 | 394 |
| Wednesday | 0 | 870 | 983 | 783 | 787 | 821 | 889 | 748 | 698 | 376 |
| Thursday | 494 | 267 | 334 | 388 | 379 | 400 | 445 | 231 | 0 | 0 |
| Friday | 1076 | 828 | 862 | 875 | 881 | 914 | 867 | 461 | 0 | 0 |
| Saturday | 0 | 832 | 629 | 626 | 611 | 560 | 665 | 413 | 0 | 0 |
| Sunday | 0 | 1006 | 694 | 663 | 553 | 556 | 663 | 372 | 0 | 0 |

## Saturday Availability Windows
*Based on 19 Saturdays observed (2026-03-28 to 2026-08-08):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 84% | ⚠️ Usually taken |
| 12pm | 84% | ⚠️ Usually taken |
| 1pm | 84% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 84% | ⚠️ Usually taken |
| 12pm | 84% | ⚠️ Usually taken |
| 1pm | 84% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 84% | ⚠️ Usually taken |
| 12pm | 84% | ⚠️ Usually taken |
| 1pm | 84% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 74% | ⚠️ Usually taken |
| 12pm | 68% | 🟡 Moderate demand |
| 1pm | 63% | 🟡 Moderate demand |
| 2pm | 37% | 🟡 Moderate demand |
| 3pm | 32% | 🟡 Moderate demand |
| 4pm | 74% | ⚠️ Usually taken |
| 5pm | 84% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 84% | ⚠️ Usually taken |
| 12pm | 84% | ⚠️ Usually taken |
| 1pm | 84% | ⚠️ Usually taken |
| 2pm | 84% | ⚠️ Usually taken |
| 3pm | 84% | ⚠️ Usually taken |
| 4pm | 84% | ⚠️ Usually taken |
| 5pm | 84% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 53% | 🟡 Moderate demand |
| 12pm | 21% | ✅ Often available |
| 1pm | 26% | ✅ Often available |
| 2pm | 21% | ✅ Often available |
| 3pm | 26% | ✅ Often available |
| 4pm | 37% | 🟡 Moderate demand |
| 5pm | 79% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 26.5 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 68% | 🟡 Moderate demand |
| 12pm | 53% | 🟡 Moderate demand |
| 1pm | 16% | ✅ Often available |
| 2pm | 32% | 🟡 Moderate demand |
| 3pm | 37% | 🟡 Moderate demand |
| 4pm | 47% | 🟡 Moderate demand |
| 5pm | 74% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 47% | 🟡 Moderate demand |
| 12pm | 47% | 🟡 Moderate demand |
| 1pm | 47% | 🟡 Moderate demand |
| 2pm | 32% | 🟡 Moderate demand |
| 3pm | 37% | 🟡 Moderate demand |
| 4pm | 53% | 🟡 Moderate demand |
| 5pm | 53% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 29,522 |
| redmond | 6,447 |
| sammamish | 3,336 |
| kingsgate | 261 |
| issaquah | 252 |
| woodinville | 218 |

## Data Quality Notes
- Total records: 40,036
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 35,213
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 88% fresh — grows toward 100% as initial batch ages out
