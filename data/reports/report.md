# KCLS Room Monitor Report
*Generated: 2026-05-19 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 22,031 |
| Date range | 2026-03-22 to 2026-06-16 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (22%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 3,834 |
| Tuesday | 4,305 |
| Wednesday | 3,889 |
| Thursday | 1,515 |
| Friday | 3,676 |
| Saturday | 2,466 |
| Sunday | 2,346 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,362 |
| 11am | 2,871 |
| 12pm | 2,966 |
| 1pm | 2,980 |
| 2pm | 2,793 |
| 3pm | 2,852 |
| 4pm | 3,040 |
| 5pm | 1,965 |
| 6pm | 788 |
| 7pm | 414 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 16257 (12555 / 3702) |
| issaquah | 27.0 | 8.2 | 28.0 | 28.0 | 12.3% | 130 (98 / 32) |
| kingsgate | 28.0 | 8.5 | 28.0 | 28.0 | 13.7% | 139 (110 / 29) |
| redmond | 28.0 | 23.0 | 28.0 | 28.0 | 0.5% | 3639 (2787 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 1740 (1562 / 178) |
| woodinville | 22.0 | 4.0 | 28.0 | 28.0 | 19.8% | 126 (96 / 30) |

*22,031 bookings total — 17,208 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 493 | 347 | 418 | 592 | 551 | 556 | 582 | 295 | 0 | 0 |
| Tuesday | 0 | 445 | 616 | 546 | 540 | 533 | 545 | 450 | 418 | 212 |
| Wednesday | 0 | 495 | 572 | 449 | 432 | 466 | 497 | 406 | 370 | 202 |
| Thursday | 260 | 128 | 169 | 197 | 181 | 208 | 245 | 127 | 0 | 0 |
| Friday | 609 | 460 | 492 | 484 | 456 | 483 | 446 | 246 | 0 | 0 |
| Saturday | 0 | 459 | 347 | 365 | 351 | 317 | 382 | 245 | 0 | 0 |
| Sunday | 0 | 537 | 352 | 347 | 282 | 289 | 343 | 196 | 0 | 0 |

## Saturday Availability Windows
*Based on 12 Saturdays observed (2026-03-28 to 2026-06-13):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 58% | 🟡 Moderate demand |
| 12pm | 58% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 42% | 🟡 Moderate demand |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 58% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 75% | ⚠️ Usually taken |
| 3pm | 75% | ⚠️ Usually taken |
| 4pm | 75% | ⚠️ Usually taken |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 42% | 🟡 Moderate demand |
| 12pm | 8% | ✅ Often available |
| 1pm | 8% | ✅ Often available |
| 2pm | 8% | ✅ Often available |
| 3pm | 17% | ✅ Often available |
| 4pm | 25% | ✅ Often available |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 22.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 42% | 🟡 Moderate demand |
| 1pm | 17% | ✅ Often available |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 42% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 25% | ✅ Often available |
| 12pm | 25% | ✅ Often available |
| 1pm | 42% | 🟡 Moderate demand |
| 2pm | 25% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
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
| bellevue | 16,257 |
| redmond | 3,639 |
| sammamish | 1,740 |
| kingsgate | 139 |
| issaquah | 130 |
| woodinville | 126 |

## Data Quality Notes
- Total records: 22,031
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 17,208
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 78% fresh — grows toward 100% as initial batch ages out
