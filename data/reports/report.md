# KCLS Room Monitor Report
*Generated: 2026-05-23 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 22,821 |
| Date range | 2026-03-22 to 2026-06-20 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (21%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 3,834 |
| Tuesday | 4,306 |
| Wednesday | 4,239 |
| Thursday | 1,684 |
| Friday | 3,711 |
| Saturday | 2,698 |
| Sunday | 2,349 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,398 |
| 11am | 2,972 |
| 12pm | 3,062 |
| 1pm | 3,080 |
| 2pm | 2,903 |
| 3pm | 2,957 |
| 4pm | 3,148 |
| 5pm | 2,038 |
| 6pm | 828 |
| 7pm | 435 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 16812 (13110 / 3702) |
| issaquah | 27.0 | 8.0 | 28.0 | 28.0 | 12.7% | 134 (102 / 32) |
| kingsgate | 28.0 | 8.2 | 28.0 | 28.0 | 14.0% | 150 (121 / 29) |
| redmond | 28.0 | 25.0 | 28.0 | 28.0 | 0.5% | 3741 (2889 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 1852 (1674 / 178) |
| woodinville | 22.5 | 4.0 | 28.0 | 28.0 | 19.7% | 132 (102 / 30) |

*22,821 bookings total — 17,998 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 493 | 347 | 418 | 592 | 551 | 556 | 582 | 295 | 0 | 0 |
| Tuesday | 0 | 445 | 616 | 546 | 540 | 533 | 545 | 450 | 418 | 213 |
| Wednesday | 0 | 530 | 614 | 489 | 477 | 510 | 541 | 446 | 410 | 222 |
| Thursday | 291 | 143 | 184 | 216 | 204 | 234 | 272 | 140 | 0 | 0 |
| Friday | 614 | 464 | 497 | 490 | 461 | 487 | 450 | 248 | 0 | 0 |
| Saturday | 0 | 505 | 381 | 399 | 388 | 347 | 415 | 263 | 0 | 0 |
| Sunday | 0 | 538 | 352 | 348 | 282 | 290 | 343 | 196 | 0 | 0 |

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

**Typical lead time at Woodinville:** median 22.5 days, p90 28.0 days

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
| bellevue | 16,812 |
| redmond | 3,741 |
| sammamish | 1,852 |
| kingsgate | 150 |
| issaquah | 134 |
| woodinville | 132 |

## Data Quality Notes
- Total records: 22,821
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 17,998
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 79% fresh — grows toward 100% as initial batch ages out
