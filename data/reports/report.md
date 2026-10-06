# KCLS Room Monitor Report
*Generated: 2026-10-06 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 64,966 |
| Date range | 2026-03-22 to 2026-11-03 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (7%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 10,906 |
| Tuesday | 12,580 |
| Wednesday | 10,752 |
| Thursday | 4,659 |
| Friday | 10,971 |
| Saturday | 7,559 |
| Sunday | 7,539 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 4,222 |
| 11am | 8,570 |
| 12pm | 8,676 |
| 1pm | 8,672 |
| 2pm | 8,468 |
| 3pm | 8,492 |
| 4pm | 8,750 |
| 5pm | 5,611 |
| 6pm | 2,288 |
| 7pm | 1,217 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 48042 (44340 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.0% | 423 (391 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 19.8% | 429 (400 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 10404 (9552 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 1.9% | 5316 (5138 / 178) |
| woodinville | 28.0 | 3.0 | 28.0 | 28.0 | 21.6% | 352 (322 / 30) |

*64,966 bookings total — 60,143 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1409 | 1019 | 1181 | 1641 | 1602 | 1605 | 1632 | 817 | 0 | 0 |
| Tuesday | 192 | 1321 | 1755 | 1589 | 1596 | 1576 | 1473 | 1250 | 1193 | 635 |
| Wednesday | 126 | 1344 | 1495 | 1192 | 1211 | 1241 | 1331 | 1135 | 1095 | 582 |
| Thursday | 780 | 413 | 553 | 609 | 613 | 642 | 688 | 361 | 0 | 0 |
| Friday | 1715 | 1344 | 1409 | 1436 | 1428 | 1472 | 1420 | 747 | 0 | 0 |
| Saturday | 0 | 1490 | 1134 | 1075 | 1042 | 974 | 1134 | 710 | 0 | 0 |
| Sunday | 0 | 1639 | 1149 | 1130 | 976 | 982 | 1072 | 591 | 0 | 0 |

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
| bellevue | 48,042 |
| redmond | 10,404 |
| sammamish | 5,316 |
| kingsgate | 429 |
| issaquah | 423 |
| woodinville | 352 |

## Data Quality Notes
- Total records: 64,966
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 60,143
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 93% fresh — grows toward 100% as initial batch ages out
