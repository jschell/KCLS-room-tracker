# KCLS Room Monitor Report
*Generated: 2026-11-22 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 78,529 |
| Date range | 2026-03-22 to 2026-12-20 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (6%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 13,063 |
| Tuesday | 15,421 |
| Wednesday | 12,775 |
| Thursday | 5,556 |
| Friday | 13,165 |
| Saturday | 9,185 |
| Sunday | 9,364 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 5,701 |
| 11am | 10,383 |
| 12pm | 10,374 |
| 1pm | 10,395 |
| 2pm | 10,158 |
| 3pm | 10,099 |
| 4pm | 10,448 |
| 5pm | 6,762 |
| 6pm | 2,754 |
| 7pm | 1,455 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 57802 (54100 / 3702) |
| issaquah | 28.0 | 8.0 | 28.0 | 28.0 | 15.1% | 489 (457 / 32) |
| kingsgate | 28.0 | 9.5 | 28.0 | 28.0 | 17.8% | 507 (478 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 0.9% | 12885 (12033 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 1.7% | 6432 (6254 / 178) |
| woodinville | 28.0 | 6.0 | 28.0 | 28.0 | 19.3% | 414 (384 / 30) |

*78,529 bookings total — 73,706 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1688 | 1219 | 1416 | 1966 | 1922 | 1920 | 1957 | 975 | 0 | 0 |
| Tuesday | 602 | 1638 | 2059 | 1885 | 1894 | 1865 | 1751 | 1515 | 1449 | 763 |
| Wednesday | 423 | 1566 | 1727 | 1413 | 1436 | 1412 | 1496 | 1305 | 1305 | 692 |
| Thursday | 937 | 483 | 661 | 723 | 732 | 762 | 827 | 431 | 0 | 0 |
| Friday | 2051 | 1617 | 1690 | 1706 | 1711 | 1750 | 1724 | 916 | 0 | 0 |
| Saturday | 0 | 1857 | 1388 | 1301 | 1230 | 1153 | 1374 | 882 | 0 | 0 |
| Sunday | 0 | 2003 | 1433 | 1401 | 1233 | 1237 | 1319 | 738 | 0 | 0 |

## Saturday Availability Windows
*Based on 38 Saturdays observed (2026-03-28 to 2026-12-19):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 74% | ⚠️ Usually taken |
| 12pm | 68% | 🟡 Moderate demand |
| 1pm | 63% | 🟡 Moderate demand |
| 2pm | 37% | 🟡 Moderate demand |
| 3pm | 34% | 🟡 Moderate demand |
| 4pm | 74% | ⚠️ Usually taken |
| 5pm | 79% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 92% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 92% | ⚠️ Usually taken |
| 5pm | 92% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 58% | 🟡 Moderate demand |
| 12pm | 26% | ✅ Often available |
| 1pm | 24% | ✅ Often available |
| 2pm | 24% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 39% | 🟡 Moderate demand |
| 5pm | 79% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 68% | 🟡 Moderate demand |
| 12pm | 58% | 🟡 Moderate demand |
| 1pm | 18% | ✅ Often available |
| 2pm | 39% | 🟡 Moderate demand |
| 3pm | 45% | 🟡 Moderate demand |
| 4pm | 53% | 🟡 Moderate demand |
| 5pm | 82% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 63% | 🟡 Moderate demand |
| 12pm | 63% | 🟡 Moderate demand |
| 1pm | 53% | 🟡 Moderate demand |
| 2pm | 42% | 🟡 Moderate demand |
| 3pm | 42% | 🟡 Moderate demand |
| 4pm | 55% | 🟡 Moderate demand |
| 5pm | 58% | 🟡 Moderate demand |

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
| bellevue | 57,802 |
| redmond | 12,885 |
| sammamish | 6,432 |
| kingsgate | 507 |
| issaquah | 489 |
| woodinville | 414 |

## Data Quality Notes
- Total records: 78,529
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 73,706
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 94% fresh — grows toward 100% as initial batch ages out
