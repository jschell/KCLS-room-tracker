# KCLS Room Monitor Report
*Generated: 2026-07-14 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 39,241 |
| Date range | 2026-03-22 to 2026-08-11 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (12%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 6,927 |
| Tuesday | 7,598 |
| Wednesday | 6,764 |
| Thursday | 2,760 |
| Friday | 6,352 |
| Saturday | 4,334 |
| Sunday | 4,506 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,386 |
| 11am | 5,134 |
| 12pm | 5,234 |
| 1pm | 5,267 |
| 2pm | 5,084 |
| 3pm | 5,113 |
| 4pm | 5,400 |
| 5pm | 3,450 |
| 6pm | 1,414 |
| 7pm | 759 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 29002 (25300 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.7% | 243 (211 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 19.7% | 254 (225 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.2% | 6303 (5451 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 3228 (3050 / 178) |
| woodinville | 26.0 | 1.5 | 28.0 | 28.0 | 23.2% | 211 (181 / 30) |

*39,241 bookings total — 34,418 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 904 | 656 | 758 | 1042 | 1010 | 1002 | 1034 | 521 | 0 | 0 |
| Tuesday | 0 | 785 | 1078 | 974 | 964 | 959 | 941 | 767 | 736 | 394 |
| Wednesday | 0 | 825 | 947 | 771 | 771 | 807 | 873 | 727 | 678 | 365 |
| Thursday | 468 | 253 | 316 | 367 | 352 | 372 | 415 | 217 | 0 | 0 |
| Friday | 1014 | 778 | 812 | 824 | 823 | 857 | 811 | 433 | 0 | 0 |
| Saturday | 0 | 831 | 629 | 626 | 611 | 560 | 664 | 413 | 0 | 0 |
| Sunday | 0 | 1006 | 694 | 663 | 553 | 556 | 662 | 372 | 0 | 0 |

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
| 11am | 47% | 🟡 Moderate demand |
| 12pm | 16% | ✅ Often available |
| 1pm | 21% | ✅ Often available |
| 2pm | 21% | ✅ Often available |
| 3pm | 26% | ✅ Often available |
| 4pm | 32% | 🟡 Moderate demand |
| 5pm | 74% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 26.0 days, p90 28.0 days

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
| bellevue | 29,002 |
| redmond | 6,303 |
| sammamish | 3,228 |
| kingsgate | 254 |
| issaquah | 243 |
| woodinville | 211 |

## Data Quality Notes
- Total records: 39,241
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 34,418
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 88% fresh — grows toward 100% as initial batch ages out
