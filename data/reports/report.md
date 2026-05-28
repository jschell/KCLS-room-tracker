# KCLS Room Monitor Report
*Generated: 2026-05-28 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 24,343 |
| Date range | 2026-03-22 to 2026-06-25 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (20%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 4,212 |
| Tuesday | 4,692 |
| Wednesday | 4,569 |
| Thursday | 1,836 |
| Friday | 3,711 |
| Saturday | 2,706 |
| Sunday | 2,617 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,473 |
| 11am | 3,160 |
| 12pm | 3,274 |
| 1pm | 3,280 |
| 2pm | 3,105 |
| 3pm | 3,157 |
| 4pm | 3,361 |
| 5pm | 2,165 |
| 6pm | 896 |
| 7pm | 472 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 17927 (14225 / 3702) |
| issaquah | 27.0 | 8.0 | 28.0 | 28.0 | 12.9% | 140 (108 / 32) |
| kingsgate | 28.0 | 9.0 | 28.0 | 28.0 | 13.9% | 158 (129 / 29) |
| redmond | 28.0 | 26.0 | 28.0 | 28.0 | 0.5% | 3978 (3126 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 2001 (1823 / 178) |
| woodinville | 23.0 | 4.0 | 28.0 | 28.0 | 20.1% | 139 (109 / 30) |

*24,343 bookings total — 19,520 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 542 | 383 | 459 | 648 | 607 | 612 | 638 | 323 | 0 | 0 |
| Tuesday | 0 | 480 | 671 | 595 | 597 | 589 | 591 | 484 | 452 | 233 |
| Wednesday | 0 | 575 | 665 | 524 | 511 | 544 | 587 | 480 | 444 | 239 |
| Thursday | 317 | 157 | 202 | 238 | 225 | 254 | 293 | 150 | 0 | 0 |
| Friday | 614 | 464 | 497 | 490 | 461 | 487 | 450 | 248 | 0 | 0 |
| Saturday | 0 | 505 | 381 | 399 | 392 | 350 | 416 | 263 | 0 | 0 |
| Sunday | 0 | 596 | 399 | 386 | 312 | 321 | 386 | 217 | 0 | 0 |

## Saturday Availability Windows
*Based on 13 Saturdays observed (2026-03-28 to 2026-06-20):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 62% | 🟡 Moderate demand |
| 12pm | 62% | 🟡 Moderate demand |
| 1pm | 46% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 62% | 🟡 Moderate demand |
| 5pm | 77% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 77% | ⚠️ Usually taken |
| 12pm | 77% | ⚠️ Usually taken |
| 1pm | 77% | ⚠️ Usually taken |
| 2pm | 77% | ⚠️ Usually taken |
| 3pm | 77% | ⚠️ Usually taken |
| 4pm | 77% | ⚠️ Usually taken |
| 5pm | 77% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 46% | 🟡 Moderate demand |
| 12pm | 15% | ✅ Often available |
| 1pm | 15% | ✅ Often available |
| 2pm | 15% | ✅ Often available |
| 3pm | 23% | ✅ Often available |
| 4pm | 31% | 🟡 Moderate demand |
| 5pm | 77% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 23.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 69% | 🟡 Moderate demand |
| 12pm | 46% | 🟡 Moderate demand |
| 1pm | 15% | ✅ Often available |
| 2pm | 31% | 🟡 Moderate demand |
| 3pm | 38% | 🟡 Moderate demand |
| 4pm | 46% | 🟡 Moderate demand |
| 5pm | 77% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 23% | ✅ Often available |
| 12pm | 23% | ✅ Often available |
| 1pm | 38% | 🟡 Moderate demand |
| 2pm | 23% | ✅ Often available |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 46% | 🟡 Moderate demand |
| 5pm | 46% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 27.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 92% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 92% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 92% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 92% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 92% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 92% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 92% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 92% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 92% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 92% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 17,927 |
| redmond | 3,978 |
| sammamish | 2,001 |
| kingsgate | 158 |
| issaquah | 140 |
| woodinville | 139 |

## Data Quality Notes
- Total records: 24,343
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 19,520
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 80% fresh — grows toward 100% as initial batch ages out
