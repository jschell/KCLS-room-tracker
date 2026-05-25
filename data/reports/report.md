# KCLS Room Monitor Report
*Generated: 2026-05-25 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 23,471 |
| Date range | 2026-03-22 to 2026-06-22 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (21%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 4,212 |
| Tuesday | 4,308 |
| Wednesday | 4,239 |
| Thursday | 1,684 |
| Friday | 3,711 |
| Saturday | 2,701 |
| Sunday | 2,616 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,447 |
| 11am | 3,066 |
| 12pm | 3,150 |
| 1pm | 3,174 |
| 2pm | 2,993 |
| 3pm | 3,044 |
| 4pm | 3,247 |
| 5pm | 2,087 |
| 6pm | 828 |
| 7pm | 435 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 17277 (13575 / 3702) |
| issaquah | 27.0 | 8.0 | 28.0 | 28.0 | 12.6% | 135 (103 / 32) |
| kingsgate | 28.0 | 9.0 | 28.0 | 28.0 | 13.6% | 154 (125 / 29) |
| redmond | 28.0 | 25.0 | 28.0 | 28.0 | 0.5% | 3873 (3021 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 1899 (1721 / 178) |
| woodinville | 23.0 | 4.0 | 28.0 | 28.0 | 19.5% | 133 (103 / 30) |

*23,471 bookings total — 18,648 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 542 | 383 | 459 | 648 | 607 | 612 | 638 | 323 | 0 | 0 |
| Tuesday | 0 | 445 | 617 | 546 | 541 | 533 | 545 | 450 | 418 | 213 |
| Wednesday | 0 | 530 | 614 | 489 | 477 | 510 | 541 | 446 | 410 | 222 |
| Thursday | 291 | 143 | 184 | 216 | 204 | 234 | 272 | 140 | 0 | 0 |
| Friday | 614 | 464 | 497 | 490 | 461 | 487 | 450 | 248 | 0 | 0 |
| Saturday | 0 | 505 | 381 | 399 | 391 | 347 | 415 | 263 | 0 | 0 |
| Sunday | 0 | 596 | 398 | 386 | 312 | 321 | 386 | 217 | 0 | 0 |

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
| bellevue | 17,277 |
| redmond | 3,873 |
| sammamish | 1,899 |
| kingsgate | 154 |
| issaquah | 135 |
| woodinville | 133 |

## Data Quality Notes
- Total records: 23,471
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 18,648
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 79% fresh — grows toward 100% as initial batch ages out
