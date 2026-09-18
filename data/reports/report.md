# KCLS Room Monitor Report
*Generated: 2026-09-18 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 59,328 |
| Date range | 2026-03-22 to 2026-10-16 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (8%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 9,855 |
| Tuesday | 11,221 |
| Wednesday | 10,037 |
| Thursday | 4,315 |
| Friday | 10,283 |
| Saturday | 6,739 |
| Sunday | 6,878 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 3,623 |
| 11am | 7,796 |
| 12pm | 7,926 |
| 1pm | 7,947 |
| 2pm | 7,759 |
| 3pm | 7,791 |
| 4pm | 8,065 |
| 5pm | 5,174 |
| 6pm | 2,117 |
| 7pm | 1,130 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 43952 (40250 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.7% | 389 (357 / 32) |
| kingsgate | 28.0 | 6.2 | 28.0 | 28.0 | 21.0% | 390 (361 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.0% | 9438 (8586 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.0% | 4832 (4654 / 178) |
| woodinville | 28.0 | 1.0 | 28.0 | 28.0 | 22.6% | 327 (297 / 30) |

*59,328 bookings total — 54,505 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1272 | 920 | 1063 | 1482 | 1446 | 1453 | 1478 | 741 | 0 | 0 |
| Tuesday | 0 | 1170 | 1588 | 1437 | 1429 | 1421 | 1353 | 1145 | 1095 | 583 |
| Wednesday | 0 | 1245 | 1401 | 1137 | 1156 | 1189 | 1268 | 1072 | 1022 | 547 |
| Thursday | 734 | 389 | 499 | 556 | 562 | 595 | 642 | 338 | 0 | 0 |
| Friday | 1617 | 1267 | 1326 | 1348 | 1338 | 1371 | 1319 | 697 | 0 | 0 |
| Saturday | 0 | 1313 | 1001 | 957 | 940 | 876 | 1020 | 632 | 0 | 0 |
| Sunday | 0 | 1492 | 1048 | 1030 | 888 | 886 | 985 | 549 | 0 | 0 |

## Saturday Availability Windows
*Based on 28 Saturdays observed (2026-03-28 to 2026-10-10):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 89% | ⚠️ Usually taken |
| 12pm | 89% | ⚠️ Usually taken |
| 1pm | 89% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 89% | ⚠️ Usually taken |
| 12pm | 89% | ⚠️ Usually taken |
| 1pm | 89% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 89% | ⚠️ Usually taken |
| 12pm | 89% | ⚠️ Usually taken |
| 1pm | 89% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 79% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 71% | ⚠️ Usually taken |
| 2pm | 46% | 🟡 Moderate demand |
| 3pm | 43% | 🟡 Moderate demand |
| 4pm | 82% | ⚠️ Usually taken |
| 5pm | 89% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 89% | ⚠️ Usually taken |
| 12pm | 89% | ⚠️ Usually taken |
| 1pm | 89% | ⚠️ Usually taken |
| 2pm | 89% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 89% | ⚠️ Usually taken |
| 5pm | 89% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 61% | 🟡 Moderate demand |
| 12pm | 21% | ✅ Often available |
| 1pm | 21% | ✅ Often available |
| 2pm | 21% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 43% | 🟡 Moderate demand |
| 5pm | 82% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 57% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 18% | ✅ Often available |
| 2pm | 43% | 🟡 Moderate demand |
| 3pm | 46% | 🟡 Moderate demand |
| 4pm | 54% | 🟡 Moderate demand |
| 5pm | 79% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 57% | 🟡 Moderate demand |
| 12pm | 57% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 39% | 🟡 Moderate demand |
| 3pm | 39% | 🟡 Moderate demand |
| 4pm | 57% | 🟡 Moderate demand |
| 5pm | 61% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 43,952 |
| redmond | 9,438 |
| sammamish | 4,832 |
| kingsgate | 390 |
| issaquah | 389 |
| woodinville | 327 |

## Data Quality Notes
- Total records: 59,328
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 54,505
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 92% fresh — grows toward 100% as initial batch ages out
