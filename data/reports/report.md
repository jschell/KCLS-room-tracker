# KCLS Room Monitor Report
*Generated: 2026-09-21 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 59,825 |
| Date range | 2026-03-22 to 2026-10-18 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (8%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 9,855 |
| Tuesday | 11,221 |
| Wednesday | 10,037 |
| Thursday | 4,331 |
| Friday | 10,284 |
| Saturday | 7,020 |
| Sunday | 7,077 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 3,623 |
| 11am | 7,910 |
| 12pm | 8,017 |
| 1pm | 8,017 |
| 2pm | 7,823 |
| 3pm | 7,847 |
| 4pm | 8,130 |
| 5pm | 5,211 |
| 6pm | 2,117 |
| 7pm | 1,130 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 44352 (40650 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.6% | 391 (359 / 32) |
| kingsgate | 28.0 | 6.5 | 28.0 | 28.0 | 21.0% | 395 (366 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.0% | 9483 (8631 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.0% | 4874 (4696 / 178) |
| woodinville | 28.0 | 1.0 | 28.0 | 28.0 | 22.7% | 330 (300 / 30) |

*59,825 bookings total — 55,002 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1272 | 920 | 1063 | 1482 | 1446 | 1453 | 1478 | 741 | 0 | 0 |
| Tuesday | 0 | 1170 | 1588 | 1437 | 1429 | 1421 | 1353 | 1145 | 1095 | 583 |
| Wednesday | 0 | 1245 | 1401 | 1137 | 1156 | 1189 | 1268 | 1072 | 1022 | 547 |
| Thursday | 734 | 389 | 504 | 560 | 569 | 595 | 642 | 338 | 0 | 0 |
| Friday | 1617 | 1267 | 1326 | 1348 | 1338 | 1371 | 1320 | 697 | 0 | 0 |
| Saturday | 0 | 1380 | 1051 | 989 | 973 | 908 | 1062 | 657 | 0 | 0 |
| Sunday | 0 | 1539 | 1084 | 1064 | 912 | 910 | 1007 | 561 | 0 | 0 |

## Saturday Availability Windows
*Based on 29 Saturdays observed (2026-03-28 to 2026-10-17):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 90% | ⚠️ Usually taken |
| 12pm | 90% | ⚠️ Usually taken |
| 1pm | 90% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 90% | ⚠️ Usually taken |
| 12pm | 90% | ⚠️ Usually taken |
| 1pm | 90% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 90% | ⚠️ Usually taken |
| 12pm | 90% | ⚠️ Usually taken |
| 1pm | 90% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 76% | ⚠️ Usually taken |
| 12pm | 72% | ⚠️ Usually taken |
| 1pm | 69% | 🟡 Moderate demand |
| 2pm | 45% | 🟡 Moderate demand |
| 3pm | 41% | 🟡 Moderate demand |
| 4pm | 79% | ⚠️ Usually taken |
| 5pm | 86% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 90% | ⚠️ Usually taken |
| 12pm | 90% | ⚠️ Usually taken |
| 1pm | 90% | ⚠️ Usually taken |
| 2pm | 90% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 90% | ⚠️ Usually taken |
| 5pm | 90% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 59% | 🟡 Moderate demand |
| 12pm | 21% | ✅ Often available |
| 1pm | 21% | ✅ Often available |
| 2pm | 21% | ✅ Often available |
| 3pm | 28% | ✅ Often available |
| 4pm | 41% | 🟡 Moderate demand |
| 5pm | 83% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 59% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 17% | ✅ Often available |
| 2pm | 41% | 🟡 Moderate demand |
| 3pm | 45% | 🟡 Moderate demand |
| 4pm | 52% | 🟡 Moderate demand |
| 5pm | 79% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 59% | 🟡 Moderate demand |
| 12pm | 59% | 🟡 Moderate demand |
| 1pm | 48% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 38% | 🟡 Moderate demand |
| 4pm | 55% | 🟡 Moderate demand |
| 5pm | 59% | 🟡 Moderate demand |

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
| bellevue | 44,352 |
| redmond | 9,483 |
| sammamish | 4,874 |
| kingsgate | 395 |
| issaquah | 391 |
| woodinville | 330 |

## Data Quality Notes
- Total records: 59,825
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 55,002
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 92% fresh — grows toward 100% as initial batch ages out
