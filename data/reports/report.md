# KCLS Room Monitor Report
*Generated: 2026-06-13 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 29,076 |
| Date range | 2026-03-22 to 2026-07-11 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (17%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 5,032 |
| Tuesday | 5,492 |
| Wednesday | 5,275 |
| Thursday | 2,102 |
| Friday | 4,846 |
| Saturday | 3,139 |
| Sunday | 3,190 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,811 |
| 11am | 3,797 |
| 12pm | 3,907 |
| 1pm | 3,917 |
| 2pm | 3,735 |
| 3pm | 3,759 |
| 4pm | 3,995 |
| 5pm | 2,560 |
| 6pm | 1,042 |
| 7pm | 553 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 21437 (17735 / 3702) |
| issaquah | 28.0 | 8.0 | 28.0 | 28.0 | 14.0% | 171 (139 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 17.3% | 185 (156 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 0.6% | 4716 (3864 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 2403 (2225 / 178) |
| woodinville | 25.0 | 3.8 | 28.0 | 28.0 | 21.3% | 164 (134 / 30) |

*29,076 bookings total — 24,253 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 660 | 475 | 557 | 761 | 725 | 725 | 750 | 379 | 0 | 0 |
| Tuesday | 0 | 570 | 797 | 712 | 697 | 688 | 683 | 552 | 520 | 273 |
| Wednesday | 0 | 655 | 755 | 597 | 597 | 626 | 680 | 563 | 522 | 280 |
| Thursday | 364 | 183 | 232 | 270 | 267 | 284 | 328 | 174 | 0 | 0 |
| Friday | 787 | 600 | 634 | 634 | 620 | 641 | 604 | 326 | 0 | 0 |
| Saturday | 0 | 604 | 443 | 464 | 444 | 404 | 477 | 303 | 0 | 0 |
| Sunday | 0 | 710 | 489 | 479 | 385 | 391 | 473 | 263 | 0 | 0 |

## Saturday Availability Windows
*Based on 15 Saturdays observed (2026-03-28 to 2026-07-11):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 87% | ⚠️ Usually taken |
| 12pm | 87% | ⚠️ Usually taken |
| 1pm | 87% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 87% | ⚠️ Usually taken |
| 12pm | 87% | ⚠️ Usually taken |
| 1pm | 87% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 87% | ⚠️ Usually taken |
| 12pm | 87% | ⚠️ Usually taken |
| 1pm | 87% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 60% | 🟡 Moderate demand |
| 1pm | 47% | 🟡 Moderate demand |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 27% | ✅ Often available |
| 4pm | 67% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 87% | ⚠️ Usually taken |
| 12pm | 87% | ⚠️ Usually taken |
| 1pm | 87% | ⚠️ Usually taken |
| 2pm | 87% | ⚠️ Usually taken |
| 3pm | 87% | ⚠️ Usually taken |
| 4pm | 87% | ⚠️ Usually taken |
| 5pm | 87% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 53% | 🟡 Moderate demand |
| 12pm | 20% | ✅ Often available |
| 1pm | 20% | ✅ Often available |
| 2pm | 20% | ✅ Often available |
| 3pm | 27% | ✅ Often available |
| 4pm | 33% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 25.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 40% | 🟡 Moderate demand |
| 1pm | 13% | ✅ Often available |
| 2pm | 27% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 40% | 🟡 Moderate demand |
| 5pm | 67% | 🟡 Moderate demand |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 33% | 🟡 Moderate demand |
| 12pm | 33% | 🟡 Moderate demand |
| 1pm | 47% | 🟡 Moderate demand |
| 2pm | 27% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 47% | 🟡 Moderate demand |
| 5pm | 47% | 🟡 Moderate demand |

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
| bellevue | 21,437 |
| redmond | 4,716 |
| sammamish | 2,403 |
| kingsgate | 185 |
| issaquah | 171 |
| woodinville | 164 |

## Data Quality Notes
- Total records: 29,076
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 24,253
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 83% fresh — grows toward 100% as initial batch ages out
