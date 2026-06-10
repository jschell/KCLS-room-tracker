# KCLS Room Monitor Report
*Generated: 2026-06-10 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 28,426 |
| Date range | 2026-03-22 to 2026-07-08 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (17%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 5,032 |
| Tuesday | 5,492 |
| Wednesday | 5,268 |
| Thursday | 1,977 |
| Friday | 4,538 |
| Saturday | 2,932 |
| Sunday | 3,187 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,742 |
| 11am | 3,693 |
| 12pm | 3,823 |
| 1pm | 3,828 |
| 2pm | 3,641 |
| 3pm | 3,678 |
| 4pm | 3,912 |
| 5pm | 2,514 |
| 6pm | 1,042 |
| 7pm | 553 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 20962 (17260 / 3702) |
| issaquah | 27.5 | 8.0 | 28.0 | 28.0 | 14.0% | 164 (132 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 16.7% | 180 (151 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 0.7% | 4614 (3762 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 2349 (2171 / 178) |
| woodinville | 25.0 | 4.0 | 28.0 | 28.0 | 21.0% | 157 (127 / 30) |

*28,426 bookings total — 23,603 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 660 | 475 | 557 | 761 | 725 | 725 | 750 | 379 | 0 | 0 |
| Tuesday | 0 | 570 | 797 | 712 | 697 | 688 | 683 | 552 | 520 | 273 |
| Wednesday | 0 | 655 | 755 | 597 | 597 | 623 | 677 | 562 | 522 | 280 |
| Thursday | 343 | 173 | 218 | 255 | 244 | 268 | 313 | 163 | 0 | 0 |
| Friday | 739 | 564 | 598 | 597 | 574 | 599 | 562 | 305 | 0 | 0 |
| Saturday | 0 | 546 | 409 | 428 | 420 | 384 | 454 | 291 | 0 | 0 |
| Sunday | 0 | 710 | 489 | 478 | 384 | 391 | 473 | 262 | 0 | 0 |

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

**Typical lead time at Woodinville:** median 25.0 days, p90 28.0 days

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

**Typical lead time at Issaquah:** median 27.5 days, p90 28.0 days

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
| bellevue | 20,962 |
| redmond | 4,614 |
| sammamish | 2,349 |
| kingsgate | 180 |
| issaquah | 164 |
| woodinville | 157 |

## Data Quality Notes
- Total records: 28,426
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 23,603
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 83% fresh — grows toward 100% as initial batch ages out
