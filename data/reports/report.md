# KCLS Room Monitor Report
*Generated: 2026-08-25 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 52,178 |
| Date range | 2026-03-22 to 2026-09-22 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (9%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 8,794 |
| Tuesday | 9,963 |
| Wednesday | 8,732 |
| Thursday | 3,689 |
| Friday | 8,744 |
| Saturday | 6,053 |
| Sunday | 6,203 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 3,165 |
| 11am | 6,851 |
| 12pm | 6,952 |
| 1pm | 6,967 |
| 2pm | 6,809 |
| 3pm | 6,859 |
| 4pm | 7,145 |
| 5pm | 4,571 |
| 6pm | 1,861 |
| 7pm | 998 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 38697 (34995 / 3702) |
| issaquah | 28.0 | 5.0 | 28.0 | 28.0 | 17.9% | 341 (309 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 20.8% | 342 (313 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 8247 (7395 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 4272 (4094 / 178) |
| woodinville | 28.0 | 1.0 | 28.0 | 28.0 | 23.7% | 279 (249 / 30) |

*52,178 bookings total — 47,355 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1136 | 822 | 950 | 1324 | 1288 | 1289 | 1322 | 663 | 0 | 0 |
| Tuesday | 0 | 1040 | 1411 | 1273 | 1264 | 1257 | 1207 | 1014 | 975 | 522 |
| Wednesday | 0 | 1075 | 1211 | 987 | 1006 | 1040 | 1112 | 939 | 886 | 476 |
| Thursday | 640 | 343 | 417 | 478 | 477 | 503 | 545 | 286 | 0 | 0 |
| Friday | 1389 | 1081 | 1125 | 1135 | 1126 | 1169 | 1126 | 593 | 0 | 0 |
| Saturday | 0 | 1161 | 894 | 850 | 849 | 795 | 930 | 574 | 0 | 0 |
| Sunday | 0 | 1329 | 944 | 920 | 799 | 806 | 903 | 502 | 0 | 0 |

## Saturday Availability Windows
*Based on 25 Saturdays observed (2026-03-28 to 2026-09-19):*

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
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 76% | ⚠️ Usually taken |
| 1pm | 72% | ⚠️ Usually taken |
| 2pm | 48% | 🟡 Moderate demand |
| 3pm | 44% | 🟡 Moderate demand |
| 4pm | 80% | ⚠️ Usually taken |
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
| 11am | 52% | 🟡 Moderate demand |
| 12pm | 20% | ✅ Often available |
| 1pm | 20% | ✅ Often available |
| 2pm | 20% | ✅ Often available |
| 3pm | 32% | 🟡 Moderate demand |
| 4pm | 40% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 64% | 🟡 Moderate demand |
| 12pm | 56% | 🟡 Moderate demand |
| 1pm | 20% | ✅ Often available |
| 2pm | 36% | 🟡 Moderate demand |
| 3pm | 40% | 🟡 Moderate demand |
| 4pm | 48% | 🟡 Moderate demand |
| 5pm | 76% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 56% | 🟡 Moderate demand |
| 12pm | 56% | 🟡 Moderate demand |
| 1pm | 52% | 🟡 Moderate demand |
| 2pm | 40% | 🟡 Moderate demand |
| 3pm | 44% | 🟡 Moderate demand |
| 4pm | 60% | 🟡 Moderate demand |
| 5pm | 60% | 🟡 Moderate demand |

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
| bellevue | 38,697 |
| redmond | 8,247 |
| sammamish | 4,272 |
| kingsgate | 342 |
| issaquah | 341 |
| woodinville | 279 |

## Data Quality Notes
- Total records: 52,178
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 47,355
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 91% fresh — grows toward 100% as initial batch ages out
