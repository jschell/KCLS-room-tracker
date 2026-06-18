# KCLS Room Monitor Report
*Generated: 2026-06-18 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 30,506 |
| Date range | 2026-03-22 to 2026-07-16 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (16%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 5,414 |
| Tuesday | 5,827 |
| Wednesday | 5,613 |
| Thursday | 2,231 |
| Friday | 4,846 |
| Saturday | 3,142 |
| Sunday | 3,433 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,881 |
| 11am | 3,970 |
| 12pm | 4,077 |
| 1pm | 4,104 |
| 2pm | 3,941 |
| 3pm | 3,955 |
| 4pm | 4,195 |
| 5pm | 2,683 |
| 6pm | 1,110 |
| 7pm | 590 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 22537 (18835 / 3702) |
| issaquah | 28.0 | 8.0 | 28.0 | 28.0 | 14.8% | 182 (150 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 18.4% | 196 (167 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 0.7% | 4890 (4038 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 2531 (2353 / 178) |
| woodinville | 25.0 | 3.2 | 28.0 | 28.0 | 21.8% | 170 (140 / 30) |

*30,506 bookings total — 25,683 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 709 | 511 | 598 | 818 | 784 | 781 | 806 | 407 | 0 | 0 |
| Tuesday | 0 | 610 | 838 | 751 | 741 | 730 | 724 | 586 | 554 | 293 |
| Wednesday | 0 | 690 | 793 | 637 | 645 | 670 | 728 | 597 | 556 | 297 |
| Thursday | 385 | 188 | 241 | 286 | 291 | 307 | 349 | 184 | 0 | 0 |
| Friday | 787 | 600 | 634 | 634 | 620 | 641 | 604 | 326 | 0 | 0 |
| Saturday | 0 | 604 | 443 | 464 | 444 | 404 | 480 | 303 | 0 | 0 |
| Sunday | 0 | 767 | 530 | 514 | 416 | 422 | 504 | 280 | 0 | 0 |

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
| bellevue | 22,537 |
| redmond | 4,890 |
| sammamish | 2,531 |
| kingsgate | 196 |
| issaquah | 182 |
| woodinville | 170 |

## Data Quality Notes
- Total records: 30,506
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 25,683
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 84% fresh — grows toward 100% as initial batch ages out
