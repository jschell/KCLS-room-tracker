# KCLS Room Monitor Report
*Generated: 2026-11-12 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 75,460 |
| Date range | 2026-03-22 to 2026-12-09 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (6%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 12,731 |
| Tuesday | 14,969 |
| Wednesday | 12,384 |
| Thursday | 5,273 |
| Friday | 12,425 |
| Saturday | 8,761 |
| Sunday | 8,917 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 5,372 |
| 11am | 9,973 |
| 12pm | 9,998 |
| 1pm | 10,010 |
| 2pm | 9,770 |
| 3pm | 9,726 |
| 4pm | 10,041 |
| 5pm | 6,501 |
| 6pm | 2,659 |
| 7pm | 1,410 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 55512 (51810 / 3702) |
| issaquah | 28.0 | 7.0 | 28.0 | 28.0 | 15.6% | 469 (437 / 32) |
| kingsgate | 28.0 | 8.8 | 28.0 | 28.0 | 18.3% | 492 (463 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.0% | 12363 (11511 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 1.7% | 6222 (6044 / 178) |
| woodinville | 28.0 | 6.0 | 28.0 | 28.0 | 19.9% | 402 (372 / 30) |

*75,460 bookings total — 70,637 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1646 | 1189 | 1381 | 1916 | 1873 | 1874 | 1903 | 949 | 0 | 0 |
| Tuesday | 534 | 1592 | 2012 | 1839 | 1851 | 1826 | 1713 | 1469 | 1395 | 738 |
| Wednesday | 368 | 1532 | 1685 | 1371 | 1391 | 1374 | 1462 | 1265 | 1264 | 672 |
| Thursday | 886 | 456 | 628 | 684 | 695 | 725 | 787 | 412 | 0 | 0 |
| Friday | 1938 | 1527 | 1601 | 1614 | 1612 | 1656 | 1617 | 860 | 0 | 0 |
| Saturday | 0 | 1767 | 1326 | 1244 | 1178 | 1102 | 1304 | 840 | 0 | 0 |
| Sunday | 0 | 1910 | 1365 | 1342 | 1170 | 1169 | 1255 | 706 | 0 | 0 |

## Saturday Availability Windows
*Based on 36 Saturdays observed (2026-03-28 to 2026-12-05):*

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
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 69% | 🟡 Moderate demand |
| 1pm | 67% | 🟡 Moderate demand |
| 2pm | 39% | 🟡 Moderate demand |
| 3pm | 36% | 🟡 Moderate demand |
| 4pm | 78% | ⚠️ Usually taken |
| 5pm | 83% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 92% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 92% | ⚠️ Usually taken |
| 5pm | 92% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 58% | 🟡 Moderate demand |
| 12pm | 25% | ✅ Often available |
| 1pm | 22% | ✅ Often available |
| 2pm | 22% | ✅ Often available |
| 3pm | 28% | ✅ Often available |
| 4pm | 42% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 56% | 🟡 Moderate demand |
| 1pm | 19% | ✅ Often available |
| 2pm | 42% | 🟡 Moderate demand |
| 3pm | 47% | 🟡 Moderate demand |
| 4pm | 53% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 64% | 🟡 Moderate demand |
| 12pm | 64% | 🟡 Moderate demand |
| 1pm | 53% | 🟡 Moderate demand |
| 2pm | 42% | 🟡 Moderate demand |
| 3pm | 42% | 🟡 Moderate demand |
| 4pm | 56% | 🟡 Moderate demand |
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
| bellevue | 55,512 |
| redmond | 12,363 |
| sammamish | 6,222 |
| kingsgate | 492 |
| issaquah | 469 |
| woodinville | 402 |

## Data Quality Notes
- Total records: 75,460
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 70,637
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 94% fresh — grows toward 100% as initial batch ages out
