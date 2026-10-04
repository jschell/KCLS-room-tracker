# KCLS Room Monitor Report
*Generated: 2026-10-04 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 64,148 |
| Date range | 2026-03-22 to 2026-11-01 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (8%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 10,562 |
| Tuesday | 12,131 |
| Wednesday | 10,746 |
| Thursday | 4,652 |
| Friday | 10,968 |
| Saturday | 7,551 |
| Sunday | 7,538 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 4,119 |
| 11am | 8,498 |
| 12pm | 8,592 |
| 1pm | 8,562 |
| 2pm | 8,349 |
| 3pm | 8,383 |
| 4pm | 8,650 |
| 5pm | 5,544 |
| 6pm | 2,254 |
| 7pm | 1,197 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 47497 (43795 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.2% | 418 (386 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 19.9% | 422 (393 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 10206 (9354 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.0% | 5256 (5078 / 178) |
| woodinville | 28.0 | 3.0 | 28.0 | 28.0 | 21.8% | 349 (319 / 30) |

*64,148 bookings total — 59,325 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1370 | 992 | 1147 | 1584 | 1547 | 1553 | 1578 | 791 | 0 | 0 |
| Tuesday | 128 | 1279 | 1708 | 1543 | 1539 | 1520 | 1427 | 1213 | 1159 | 615 |
| Wednesday | 126 | 1344 | 1495 | 1192 | 1209 | 1241 | 1331 | 1131 | 1095 | 582 |
| Thursday | 780 | 413 | 553 | 606 | 609 | 642 | 688 | 361 | 0 | 0 |
| Friday | 1715 | 1341 | 1409 | 1436 | 1428 | 1472 | 1420 | 747 | 0 | 0 |
| Saturday | 0 | 1490 | 1131 | 1072 | 1041 | 973 | 1134 | 710 | 0 | 0 |
| Sunday | 0 | 1639 | 1149 | 1129 | 976 | 982 | 1072 | 591 | 0 | 0 |

## Saturday Availability Windows
*Based on 31 Saturdays observed (2026-03-28 to 2026-10-31):*

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
| 11am | 77% | ⚠️ Usually taken |
| 12pm | 74% | ⚠️ Usually taken |
| 1pm | 71% | ⚠️ Usually taken |
| 2pm | 45% | 🟡 Moderate demand |
| 3pm | 42% | 🟡 Moderate demand |
| 4pm | 81% | ⚠️ Usually taken |
| 5pm | 87% | ⚠️ Usually taken |

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
| 11am | 58% | 🟡 Moderate demand |
| 12pm | 23% | ✅ Often available |
| 1pm | 19% | ✅ Often available |
| 2pm | 19% | ✅ Often available |
| 3pm | 26% | ✅ Often available |
| 4pm | 39% | 🟡 Moderate demand |
| 5pm | 84% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 61% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 19% | ✅ Often available |
| 2pm | 42% | 🟡 Moderate demand |
| 3pm | 48% | 🟡 Moderate demand |
| 4pm | 55% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 61% | 🟡 Moderate demand |
| 12pm | 61% | 🟡 Moderate demand |
| 1pm | 48% | 🟡 Moderate demand |
| 2pm | 39% | 🟡 Moderate demand |
| 3pm | 39% | 🟡 Moderate demand |
| 4pm | 58% | 🟡 Moderate demand |
| 5pm | 61% | 🟡 Moderate demand |

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
| bellevue | 47,497 |
| redmond | 10,206 |
| sammamish | 5,256 |
| kingsgate | 422 |
| issaquah | 418 |
| woodinville | 349 |

## Data Quality Notes
- Total records: 64,148
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 59,325
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 92% fresh — grows toward 100% as initial batch ages out
