# KCLS Room Monitor Report
*Generated: 2026-07-21 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 41,318 |
| Date range | 2026-03-22 to 2026-08-18 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (12%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 7,287 |
| Tuesday | 7,960 |
| Wednesday | 6,957 |
| Thursday | 2,938 |
| Friday | 6,766 |
| Saturday | 4,650 |
| Sunday | 4,760 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,517 |
| 11am | 5,419 |
| 12pm | 5,508 |
| 1pm | 5,522 |
| 2pm | 5,357 |
| 3pm | 5,389 |
| 4pm | 5,691 |
| 5pm | 3,641 |
| 6pm | 1,478 |
| 7pm | 796 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 30487 (26785 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.4% | 258 (226 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 20.7% | 271 (242 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.2% | 6663 (5811 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 3415 (3237 / 178) |
| woodinville | 27.0 | 1.0 | 28.0 | 28.0 | 23.2% | 224 (194 / 30) |

*41,318 bookings total — 36,495 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 947 | 686 | 793 | 1094 | 1066 | 1062 | 1090 | 549 | 0 | 0 |
| Tuesday | 0 | 820 | 1125 | 1016 | 1002 | 996 | 987 | 815 | 780 | 419 |
| Wednesday | 0 | 870 | 983 | 783 | 788 | 821 | 889 | 748 | 698 | 377 |
| Thursday | 494 | 267 | 334 | 388 | 379 | 400 | 445 | 231 | 0 | 0 |
| Friday | 1076 | 828 | 864 | 875 | 881 | 914 | 867 | 461 | 0 | 0 |
| Saturday | 0 | 895 | 679 | 666 | 651 | 603 | 714 | 442 | 0 | 0 |
| Sunday | 0 | 1053 | 730 | 700 | 590 | 593 | 699 | 395 | 0 | 0 |

## Saturday Availability Windows
*Based on 20 Saturdays observed (2026-03-28 to 2026-08-15):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 70% | 🟡 Moderate demand |
| 1pm | 65% | 🟡 Moderate demand |
| 2pm | 35% | 🟡 Moderate demand |
| 3pm | 30% | 🟡 Moderate demand |
| 4pm | 70% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 85% | ⚠️ Usually taken |
| 3pm | 85% | ⚠️ Usually taken |
| 4pm | 85% | ⚠️ Usually taken |
| 5pm | 85% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 55% | 🟡 Moderate demand |
| 12pm | 20% | ✅ Often available |
| 1pm | 25% | ✅ Often available |
| 2pm | 20% | ✅ Often available |
| 3pm | 30% | 🟡 Moderate demand |
| 4pm | 40% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 27.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 70% | 🟡 Moderate demand |
| 12pm | 55% | 🟡 Moderate demand |
| 1pm | 15% | ✅ Often available |
| 2pm | 30% | 🟡 Moderate demand |
| 3pm | 35% | 🟡 Moderate demand |
| 4pm | 45% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 35% | 🟡 Moderate demand |
| 3pm | 40% | 🟡 Moderate demand |
| 4pm | 55% | 🟡 Moderate demand |
| 5pm | 55% | 🟡 Moderate demand |

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
| bellevue | 30,487 |
| redmond | 6,663 |
| sammamish | 3,415 |
| kingsgate | 271 |
| issaquah | 258 |
| woodinville | 224 |

## Data Quality Notes
- Total records: 41,318
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 36,495
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 88% fresh — grows toward 100% as initial batch ages out
