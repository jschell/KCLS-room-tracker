# KCLS Room Monitor Report
*Generated: 2026-07-25 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 42,375 |
| Date range | 2026-03-22 to 2026-08-22 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (11%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 7,287 |
| Tuesday | 7,961 |
| Wednesday | 7,305 |
| Thursday | 3,038 |
| Friday | 7,119 |
| Saturday | 4,905 |
| Sunday | 4,760 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,600 |
| 11am | 5,564 |
| 12pm | 5,644 |
| 1pm | 5,648 |
| 2pm | 5,495 |
| 3pm | 5,522 |
| 4pm | 5,832 |
| 5pm | 3,736 |
| 6pm | 1,518 |
| 7pm | 816 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 31372 (27670 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.3% | 266 (234 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 20.9% | 278 (249 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.2% | 6702 (5850 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 3526 (3348 / 178) |
| woodinville | 27.0 | 1.0 | 28.0 | 28.0 | 22.9% | 231 (201 / 30) |

*42,375 bookings total — 37,552 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 947 | 686 | 793 | 1094 | 1066 | 1062 | 1090 | 549 | 0 | 0 |
| Tuesday | 0 | 820 | 1125 | 1016 | 1002 | 996 | 988 | 815 | 780 | 419 |
| Wednesday | 0 | 905 | 1024 | 821 | 833 | 865 | 934 | 788 | 738 | 397 |
| Thursday | 520 | 277 | 341 | 397 | 391 | 415 | 459 | 238 | 0 | 0 |
| Friday | 1133 | 872 | 908 | 920 | 928 | 958 | 916 | 484 | 0 | 0 |
| Saturday | 0 | 951 | 723 | 700 | 685 | 633 | 746 | 467 | 0 | 0 |
| Sunday | 0 | 1053 | 730 | 700 | 590 | 593 | 699 | 395 | 0 | 0 |

## Saturday Availability Windows
*Based on 21 Saturdays observed (2026-03-28 to 2026-08-22):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 76% | ⚠️ Usually taken |
| 12pm | 71% | ⚠️ Usually taken |
| 1pm | 62% | 🟡 Moderate demand |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 29% | ✅ Often available |
| 4pm | 67% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 86% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 86% | ⚠️ Usually taken |
| 5pm | 86% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 57% | 🟡 Moderate demand |
| 12pm | 19% | ✅ Often available |
| 1pm | 24% | ✅ Often available |
| 2pm | 19% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 38% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 27.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 14% | ✅ Often available |
| 2pm | 29% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 43% | 🟡 Moderate demand |
| 5pm | 71% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 52% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 52% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 43% | 🟡 Moderate demand |
| 4pm | 57% | 🟡 Moderate demand |
| 5pm | 57% | 🟡 Moderate demand |

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
| bellevue | 31,372 |
| redmond | 6,702 |
| sammamish | 3,526 |
| kingsgate | 278 |
| issaquah | 266 |
| woodinville | 231 |

## Data Quality Notes
- Total records: 42,375
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 37,552
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 89% fresh — grows toward 100% as initial batch ages out
