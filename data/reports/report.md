# KCLS Room Monitor Report
*Generated: 2026-08-19 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 50,327 |
| Date range | 2026-03-22 to 2026-09-16 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (10%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 8,412 |
| Tuesday | 9,569 |
| Wednesday | 8,727 |
| Thursday | 3,520 |
| Friday | 8,361 |
| Saturday | 5,771 |
| Sunday | 5,967 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 3,025 |
| 11am | 6,608 |
| 12pm | 6,710 |
| 1pm | 6,715 |
| 2pm | 6,560 |
| 3pm | 6,592 |
| 4pm | 6,895 |
| 5pm | 4,418 |
| 6pm | 1,825 |
| 7pm | 979 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 37417 (33715 / 3702) |
| issaquah | 28.0 | 5.0 | 28.0 | 28.0 | 17.6% | 329 (297 / 32) |
| kingsgate | 28.0 | 6.0 | 28.0 | 28.0 | 21.0% | 329 (300 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 7863 (7011 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 4117 (3939 / 178) |
| woodinville | 28.0 | 1.0 | 28.0 | 28.0 | 23.9% | 272 (242 / 30) |

*50,327 bookings total — 45,504 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1086 | 786 | 908 | 1267 | 1232 | 1232 | 1266 | 635 | 0 | 0 |
| Tuesday | 0 | 995 | 1349 | 1219 | 1210 | 1205 | 1171 | 977 | 939 | 504 |
| Wednesday | 0 | 1075 | 1209 | 987 | 1006 | 1040 | 1110 | 939 | 886 | 475 |
| Thursday | 606 | 330 | 405 | 458 | 454 | 476 | 518 | 273 | 0 | 0 |
| Friday | 1333 | 1038 | 1079 | 1088 | 1078 | 1111 | 1070 | 564 | 0 | 0 |
| Saturday | 0 | 1108 | 850 | 815 | 815 | 757 | 881 | 545 | 0 | 0 |
| Sunday | 0 | 1276 | 910 | 881 | 765 | 771 | 879 | 485 | 0 | 0 |

## Saturday Availability Windows
*Based on 24 Saturdays observed (2026-03-28 to 2026-09-12):*

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
| 11am | 71% | ⚠️ Usually taken |
| 12pm | 67% | 🟡 Moderate demand |
| 1pm | 58% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 67% | 🟡 Moderate demand |
| 5pm | 79% | ⚠️ Usually taken |

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
| 12pm | 21% | ✅ Often available |
| 1pm | 21% | ✅ Often available |
| 2pm | 21% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 42% | 🟡 Moderate demand |
| 5pm | 83% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 54% | 🟡 Moderate demand |
| 1pm | 17% | ✅ Often available |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 38% | 🟡 Moderate demand |
| 4pm | 46% | 🟡 Moderate demand |
| 5pm | 71% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 54% | 🟡 Moderate demand |
| 12pm | 54% | 🟡 Moderate demand |
| 1pm | 54% | 🟡 Moderate demand |
| 2pm | 42% | 🟡 Moderate demand |
| 3pm | 46% | 🟡 Moderate demand |
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
| bellevue | 37,417 |
| redmond | 7,863 |
| sammamish | 4,117 |
| issaquah | 329 |
| kingsgate | 329 |
| woodinville | 272 |

## Data Quality Notes
- Total records: 50,327
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 45,504
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 90% fresh — grows toward 100% as initial batch ages out
