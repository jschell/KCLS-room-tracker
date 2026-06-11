# KCLS Room Monitor Report
*Generated: 2026-06-11 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 28,555 |
| Date range | 2026-03-22 to 2026-07-09 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (17%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 5,032 |
| Tuesday | 5,492 |
| Wednesday | 5,272 |
| Thursday | 2,101 |
| Friday | 4,538 |
| Saturday | 2,932 |
| Sunday | 3,188 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,763 |
| 11am | 3,703 |
| 12pm | 3,837 |
| 1pm | 3,843 |
| 2pm | 3,664 |
| 3pm | 3,696 |
| 4pm | 3,927 |
| 5pm | 2,527 |
| 6pm | 1,042 |
| 7pm | 553 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 21042 (17340 / 3702) |
| issaquah | 28.0 | 8.0 | 28.0 | 28.0 | 13.8% | 167 (135 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 17.0% | 182 (153 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 0.6% | 4629 (3777 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 2375 (2197 / 178) |
| woodinville | 24.5 | 3.8 | 28.0 | 28.0 | 21.2% | 160 (130 / 30) |

*28,555 bookings total — 23,732 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 660 | 475 | 557 | 761 | 725 | 725 | 750 | 379 | 0 | 0 |
| Tuesday | 0 | 570 | 797 | 712 | 697 | 688 | 683 | 552 | 520 | 273 |
| Wednesday | 0 | 655 | 755 | 597 | 597 | 626 | 677 | 563 | 522 | 280 |
| Thursday | 364 | 183 | 232 | 270 | 267 | 283 | 328 | 174 | 0 | 0 |
| Friday | 739 | 564 | 598 | 597 | 574 | 599 | 562 | 305 | 0 | 0 |
| Saturday | 0 | 546 | 409 | 428 | 420 | 384 | 454 | 291 | 0 | 0 |
| Sunday | 0 | 710 | 489 | 478 | 384 | 391 | 473 | 263 | 0 | 0 |

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
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 86% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 86% | ⚠️ Usually taken |
| 5pm | 86% | ⚠️ Usually taken |

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

**Typical lead time at Woodinville:** median 24.5 days, p90 28.0 days

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

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

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
| bellevue | 21,042 |
| redmond | 4,629 |
| sammamish | 2,375 |
| kingsgate | 182 |
| issaquah | 167 |
| woodinville | 160 |

## Data Quality Notes
- Total records: 28,555
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 23,732
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 83% fresh — grows toward 100% as initial batch ages out
