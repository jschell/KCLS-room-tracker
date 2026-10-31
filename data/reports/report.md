# KCLS Room Monitor Report
*Generated: 2026-10-31 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 71,740 |
| Date range | 2026-03-22 to 2026-11-28 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (7%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 12,001 |
| Tuesday | 14,056 |
| Wednesday | 11,713 |
| Thursday | 5,151 |
| Friday | 12,040 |
| Saturday | 8,494 |
| Sunday | 8,285 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 4,948 |
| 11am | 9,478 |
| 12pm | 9,524 |
| 1pm | 9,528 |
| 2pm | 9,293 |
| 3pm | 9,303 |
| 4pm | 9,603 |
| 5pm | 6,211 |
| 6pm | 2,516 |
| 7pm | 1,336 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 52767 (49065 / 3702) |
| issaquah | 28.0 | 7.0 | 28.0 | 28.0 | 16.2% | 452 (420 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 18.6% | 468 (439 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.0% | 11679 (10827 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 1.8% | 5986 (5808 / 178) |
| woodinville | 28.0 | 4.8 | 28.0 | 28.0 | 20.4% | 388 (358 / 30) |

*71,740 bookings total — 66,917 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1550 | 1121 | 1302 | 1804 | 1763 | 1770 | 1796 | 895 | 0 | 0 |
| Tuesday | 398 | 1485 | 1913 | 1743 | 1749 | 1727 | 1619 | 1394 | 1326 | 702 |
| Wednesday | 273 | 1461 | 1610 | 1295 | 1314 | 1320 | 1407 | 1209 | 1190 | 634 |
| Thursday | 856 | 446 | 616 | 678 | 683 | 713 | 761 | 398 | 0 | 0 |
| Friday | 1871 | 1471 | 1544 | 1568 | 1565 | 1613 | 1572 | 836 | 0 | 0 |
| Saturday | 0 | 1709 | 1281 | 1203 | 1143 | 1072 | 1269 | 817 | 0 | 0 |
| Sunday | 0 | 1785 | 1258 | 1237 | 1076 | 1088 | 1179 | 662 | 0 | 0 |

## Saturday Availability Windows
*Based on 35 Saturdays observed (2026-03-28 to 2026-11-28):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 91% | ⚠️ Usually taken |
| 12pm | 91% | ⚠️ Usually taken |
| 1pm | 91% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 91% | ⚠️ Usually taken |
| 12pm | 91% | ⚠️ Usually taken |
| 1pm | 91% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 91% | ⚠️ Usually taken |
| 12pm | 91% | ⚠️ Usually taken |
| 1pm | 91% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 77% | ⚠️ Usually taken |
| 12pm | 71% | ⚠️ Usually taken |
| 1pm | 69% | 🟡 Moderate demand |
| 2pm | 40% | 🟡 Moderate demand |
| 3pm | 37% | 🟡 Moderate demand |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 86% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 91% | ⚠️ Usually taken |
| 12pm | 91% | ⚠️ Usually taken |
| 1pm | 91% | ⚠️ Usually taken |
| 2pm | 91% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 89% | ⚠️ Usually taken |
| 5pm | 91% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 26% | ✅ Often available |
| 1pm | 23% | ✅ Often available |
| 2pm | 23% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 43% | 🟡 Moderate demand |
| 5pm | 83% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 66% | 🟡 Moderate demand |
| 12pm | 54% | 🟡 Moderate demand |
| 1pm | 20% | ✅ Often available |
| 2pm | 40% | 🟡 Moderate demand |
| 3pm | 46% | 🟡 Moderate demand |
| 4pm | 51% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 63% | 🟡 Moderate demand |
| 12pm | 63% | 🟡 Moderate demand |
| 1pm | 51% | 🟡 Moderate demand |
| 2pm | 40% | 🟡 Moderate demand |
| 3pm | 40% | 🟡 Moderate demand |
| 4pm | 57% | 🟡 Moderate demand |
| 5pm | 60% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 52,767 |
| redmond | 11,679 |
| sammamish | 5,986 |
| kingsgate | 468 |
| issaquah | 452 |
| woodinville | 388 |

## Data Quality Notes
- Total records: 71,740
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 66,917
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 93% fresh — grows toward 100% as initial batch ages out
