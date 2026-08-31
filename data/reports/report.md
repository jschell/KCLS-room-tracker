# KCLS Room Monitor Report
*Generated: 2026-08-31 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 53,766 |
| Date range | 2026-03-22 to 2026-09-28 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (9%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 9,142 |
| Tuesday | 9,968 |
| Wednesday | 9,086 |
| Thursday | 3,829 |
| Friday | 9,065 |
| Saturday | 6,217 |
| Sunday | 6,459 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 3,279 |
| 11am | 7,080 |
| 12pm | 7,161 |
| 1pm | 7,189 |
| 2pm | 7,021 |
| 3pm | 7,081 |
| 4pm | 7,355 |
| 5pm | 4,689 |
| 6pm | 1,895 |
| 7pm | 1,016 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 39922 (36220 / 3702) |
| issaquah | 28.0 | 5.0 | 28.0 | 28.0 | 17.8% | 353 (321 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 20.5% | 351 (322 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 8466 (7614 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 4387 (4209 / 178) |
| woodinville | 28.0 | 1.0 | 28.0 | 28.0 | 23.3% | 287 (257 / 30) |

*53,766 bookings total — 48,943 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1180 | 854 | 988 | 1376 | 1340 | 1341 | 1374 | 689 | 0 | 0 |
| Tuesday | 0 | 1040 | 1411 | 1274 | 1265 | 1257 | 1208 | 1015 | 975 | 523 |
| Wednesday | 0 | 1120 | 1261 | 1031 | 1048 | 1084 | 1156 | 973 | 920 | 493 |
| Thursday | 662 | 353 | 441 | 498 | 491 | 523 | 565 | 296 | 0 | 0 |
| Friday | 1437 | 1119 | 1162 | 1176 | 1168 | 1218 | 1170 | 615 | 0 | 0 |
| Saturday | 0 | 1203 | 914 | 873 | 870 | 817 | 953 | 587 | 0 | 0 |
| Sunday | 0 | 1391 | 984 | 961 | 839 | 841 | 929 | 514 | 0 | 0 |

## Saturday Availability Windows
*Based on 26 Saturdays observed (2026-03-28 to 2026-09-26):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 81% | ⚠️ Usually taken |
| 12pm | 77% | ⚠️ Usually taken |
| 1pm | 73% | ⚠️ Usually taken |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 46% | 🟡 Moderate demand |
| 4pm | 81% | ⚠️ Usually taken |
| 5pm | 88% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 88% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 88% | ⚠️ Usually taken |
| 5pm | 88% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 54% | 🟡 Moderate demand |
| 12pm | 19% | ✅ Often available |
| 1pm | 19% | ✅ Often available |
| 2pm | 19% | ✅ Often available |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 38% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 62% | 🟡 Moderate demand |
| 12pm | 54% | 🟡 Moderate demand |
| 1pm | 19% | ✅ Often available |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 42% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 77% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 58% | 🟡 Moderate demand |
| 12pm | 58% | 🟡 Moderate demand |
| 1pm | 54% | 🟡 Moderate demand |
| 2pm | 42% | 🟡 Moderate demand |
| 3pm | 42% | 🟡 Moderate demand |
| 4pm | 62% | 🟡 Moderate demand |
| 5pm | 62% | 🟡 Moderate demand |

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
| bellevue | 39,922 |
| redmond | 8,466 |
| sammamish | 4,387 |
| issaquah | 353 |
| kingsgate | 351 |
| woodinville | 287 |

## Data Quality Notes
- Total records: 53,766
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 48,943
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 91% fresh — grows toward 100% as initial batch ages out
