# KCLS Room Monitor Report
*Generated: 2026-06-21 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 31,379 |
| Date range | 2026-03-22 to 2026-07-19 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (15%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 5,414 |
| Tuesday | 5,827 |
| Wednesday | 5,613 |
| Thursday | 2,231 |
| Friday | 5,241 |
| Saturday | 3,381 |
| Sunday | 3,672 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,944 |
| 11am | 4,118 |
| 12pm | 4,207 |
| 1pm | 4,210 |
| 2pm | 4,055 |
| 3pm | 4,068 |
| 4pm | 4,323 |
| 5pm | 2,754 |
| 6pm | 1,110 |
| 7pm | 590 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 23227 (19525 / 3702) |
| issaquah | 28.0 | 8.0 | 28.0 | 28.0 | 14.5% | 186 (154 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 18.0% | 200 (171 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 0.7% | 5001 (4149 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 2594 (2416 / 178) |
| woodinville | 25.0 | 3.5 | 28.0 | 28.0 | 21.6% | 171 (141 / 30) |

*31,379 bookings total — 26,556 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 709 | 511 | 598 | 818 | 784 | 781 | 806 | 407 | 0 | 0 |
| Tuesday | 0 | 610 | 838 | 751 | 741 | 730 | 724 | 586 | 554 | 293 |
| Wednesday | 0 | 690 | 793 | 637 | 645 | 670 | 728 | 597 | 556 | 297 |
| Thursday | 385 | 188 | 241 | 286 | 291 | 307 | 349 | 184 | 0 | 0 |
| Friday | 850 | 650 | 684 | 685 | 672 | 694 | 654 | 352 | 0 | 0 |
| Saturday | 0 | 652 | 483 | 489 | 476 | 434 | 521 | 326 | 0 | 0 |
| Sunday | 0 | 817 | 570 | 544 | 446 | 452 | 541 | 302 | 0 | 0 |

## Saturday Availability Windows
*Based on 16 Saturdays observed (2026-03-28 to 2026-07-18):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 69% | 🟡 Moderate demand |
| 12pm | 62% | 🟡 Moderate demand |
| 1pm | 56% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 69% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

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
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 19% | ✅ Often available |
| 1pm | 19% | ✅ Often available |
| 2pm | 19% | ✅ Often available |
| 3pm | 25% | ✅ Often available |
| 4pm | 31% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 25.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 62% | 🟡 Moderate demand |
| 12pm | 44% | 🟡 Moderate demand |
| 1pm | 12% | ✅ Often available |
| 2pm | 25% | ✅ Often available |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 38% | 🟡 Moderate demand |
| 5pm | 69% | 🟡 Moderate demand |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 38% | 🟡 Moderate demand |
| 12pm | 38% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 25% | ✅ Often available |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 44% | 🟡 Moderate demand |
| 5pm | 44% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 23,227 |
| redmond | 5,001 |
| sammamish | 2,594 |
| kingsgate | 200 |
| issaquah | 186 |
| woodinville | 171 |

## Data Quality Notes
- Total records: 31,379
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 26,556
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 85% fresh — grows toward 100% as initial batch ages out
