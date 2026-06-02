# KCLS Room Monitor Report
*Generated: 2026-06-02 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 25,959 |
| Date range | 2026-03-22 to 2026-06-30 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (19%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 4,593 |
| Tuesday | 5,085 |
| Wednesday | 4,570 |
| Thursday | 1,841 |
| Friday | 4,124 |
| Saturday | 2,908 |
| Sunday | 2,838 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,584 |
| 11am | 3,373 |
| 12pm | 3,486 |
| 1pm | 3,509 |
| 2pm | 3,318 |
| 3pm | 3,374 |
| 4pm | 3,593 |
| 5pm | 2,300 |
| 6pm | 930 |
| 7pm | 492 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 19117 (15415 / 3702) |
| issaquah | 27.0 | 8.2 | 28.0 | 28.0 | 12.7% | 150 (118 / 32) |
| kingsgate | 28.0 | 8.2 | 28.0 | 28.0 | 15.1% | 166 (137 / 29) |
| redmond | 28.0 | 27.0 | 28.0 | 28.0 | 0.6% | 4239 (3387 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 2140 (1962 / 178) |
| woodinville | 24.0 | 4.0 | 28.0 | 28.0 | 20.4% | 147 (117 / 30) |

*25,959 bookings total — 21,136 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 591 | 419 | 500 | 704 | 666 | 668 | 694 | 351 | 0 | 0 |
| Tuesday | 0 | 525 | 734 | 651 | 645 | 636 | 637 | 518 | 486 | 253 |
| Wednesday | 0 | 575 | 665 | 524 | 511 | 545 | 587 | 480 | 444 | 239 |
| Thursday | 317 | 157 | 202 | 239 | 229 | 254 | 293 | 150 | 0 | 0 |
| Friday | 676 | 514 | 547 | 544 | 517 | 543 | 506 | 277 | 0 | 0 |
| Saturday | 0 | 541 | 405 | 424 | 416 | 384 | 452 | 286 | 0 | 0 |
| Sunday | 0 | 642 | 433 | 423 | 334 | 344 | 424 | 238 | 0 | 0 |

## Saturday Availability Windows
*Based on 14 Saturdays observed (2026-03-28 to 2026-06-27):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 64% | 🟡 Moderate demand |
| 12pm | 64% | 🟡 Moderate demand |
| 1pm | 43% | 🟡 Moderate demand |
| 2pm | 36% | 🟡 Moderate demand |
| 3pm | 29% | ✅ Often available |
| 4pm | 64% | 🟡 Moderate demand |
| 5pm | 79% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 79% | ⚠️ Usually taken |
| 12pm | 79% | ⚠️ Usually taken |
| 1pm | 79% | ⚠️ Usually taken |
| 2pm | 79% | ⚠️ Usually taken |
| 3pm | 79% | ⚠️ Usually taken |
| 4pm | 79% | ⚠️ Usually taken |
| 5pm | 79% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 14% | ✅ Often available |
| 1pm | 14% | ✅ Often available |
| 2pm | 14% | ✅ Often available |
| 3pm | 21% | ✅ Often available |
| 4pm | 29% | ✅ Often available |
| 5pm | 79% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 24.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 64% | 🟡 Moderate demand |
| 12pm | 43% | 🟡 Moderate demand |
| 1pm | 14% | ✅ Often available |
| 2pm | 29% | ✅ Often available |
| 3pm | 36% | 🟡 Moderate demand |
| 4pm | 43% | 🟡 Moderate demand |
| 5pm | 71% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 29% | ✅ Often available |
| 12pm | 29% | ✅ Often available |
| 1pm | 43% | 🟡 Moderate demand |
| 2pm | 29% | ✅ Often available |
| 3pm | 36% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 50% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 27.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 93% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 93% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 93% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 93% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 93% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 93% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 93% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 93% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 93% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 93% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 19,117 |
| redmond | 4,239 |
| sammamish | 2,140 |
| kingsgate | 166 |
| issaquah | 150 |
| woodinville | 147 |

## Data Quality Notes
- Total records: 25,959
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 21,136
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 81% fresh — grows toward 100% as initial batch ages out
