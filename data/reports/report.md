# KCLS Room Monitor Report
*Generated: 2026-06-04 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 26,449 |
| Date range | 2026-03-22 to 2026-07-02 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (18%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 4,593 |
| Tuesday | 5,085 |
| Wednesday | 4,919 |
| Thursday | 1,977 |
| Friday | 4,125 |
| Saturday | 2,911 |
| Sunday | 2,839 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,610 |
| 11am | 3,424 |
| 12pm | 3,542 |
| 1pm | 3,559 |
| 2pm | 3,385 |
| 3pm | 3,433 |
| 4pm | 3,658 |
| 5pm | 2,357 |
| 6pm | 968 |
| 7pm | 513 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 19487 (15785 / 3702) |
| issaquah | 27.0 | 8.0 | 28.0 | 28.0 | 12.8% | 156 (124 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 15.9% | 170 (141 / 29) |
| redmond | 28.0 | 27.0 | 28.0 | 28.0 | 0.6% | 4296 (3444 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 2190 (2012 / 178) |
| woodinville | 24.0 | 4.0 | 28.0 | 28.0 | 20.7% | 150 (120 / 30) |

*26,449 bookings total — 21,626 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 591 | 419 | 500 | 704 | 666 | 668 | 694 | 351 | 0 | 0 |
| Tuesday | 0 | 525 | 734 | 651 | 645 | 636 | 637 | 518 | 486 | 253 |
| Wednesday | 0 | 610 | 704 | 558 | 563 | 589 | 632 | 521 | 482 | 260 |
| Thursday | 343 | 173 | 218 | 255 | 244 | 268 | 313 | 163 | 0 | 0 |
| Friday | 676 | 514 | 548 | 544 | 517 | 543 | 506 | 277 | 0 | 0 |
| Saturday | 0 | 541 | 405 | 424 | 416 | 384 | 452 | 289 | 0 | 0 |
| Sunday | 0 | 642 | 433 | 423 | 334 | 345 | 424 | 238 | 0 | 0 |

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
| bellevue | 19,487 |
| redmond | 4,296 |
| sammamish | 2,190 |
| kingsgate | 170 |
| issaquah | 156 |
| woodinville | 150 |

## Data Quality Notes
- Total records: 26,449
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 21,626
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 82% fresh — grows toward 100% as initial batch ages out
