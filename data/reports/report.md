# KCLS Room Monitor Report
*Generated: 2026-05-11 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 19,626 |
| Date range | 2026-03-22 to 2026-06-08 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (25%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 3,503 |
| Tuesday | 3,579 |
| Wednesday | 3,503 |
| Thursday | 1,334 |
| Friday | 3,298 |
| Saturday | 2,289 |
| Sunday | 2,120 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,232 |
| 11am | 2,574 |
| 12pm | 2,642 |
| 1pm | 2,655 |
| 2pm | 2,483 |
| 3pm | 2,540 |
| 4pm | 2,720 |
| 5pm | 1,747 |
| 6pm | 677 |
| 7pm | 356 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.2% | 14497 (10795 / 3702) |
| issaquah | 26.0 | 9.0 | 28.0 | 28.0 | 11.1% | 117 (85 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 13.6% | 125 (96 / 29) |
| redmond | 28.0 | 22.0 | 28.0 | 28.0 | 0.5% | 3201 (2349 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 1574 (1396 / 178) |
| woodinville | 22.0 | 3.8 | 28.0 | 28.0 | 20.5% | 112 (82 / 30) |

*19,626 bookings total — 14,803 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 459 | 325 | 381 | 538 | 499 | 504 | 528 | 269 | 0 | 0 |
| Tuesday | 0 | 365 | 514 | 458 | 451 | 440 | 454 | 375 | 348 | 174 |
| Wednesday | 0 | 450 | 514 | 401 | 390 | 422 | 446 | 369 | 329 | 182 |
| Thursday | 233 | 112 | 147 | 169 | 155 | 182 | 222 | 114 | 0 | 0 |
| Friday | 540 | 409 | 446 | 433 | 410 | 437 | 400 | 223 | 0 | 0 |
| Saturday | 0 | 421 | 322 | 341 | 327 | 297 | 357 | 224 | 0 | 0 |
| Sunday | 0 | 492 | 318 | 315 | 251 | 258 | 313 | 173 | 0 | 0 |

## Saturday Availability Windows
*Based on 11 Saturdays observed (2026-03-28 to 2026-06-06):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 64% | 🟡 Moderate demand |
| 12pm | 64% | 🟡 Moderate demand |
| 1pm | 55% | 🟡 Moderate demand |
| 2pm | 45% | 🟡 Moderate demand |
| 3pm | 36% | 🟡 Moderate demand |
| 4pm | 64% | 🟡 Moderate demand |
| 5pm | 82% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 73% | ⚠️ Usually taken |
| 12pm | 73% | ⚠️ Usually taken |
| 1pm | 73% | ⚠️ Usually taken |
| 2pm | 73% | ⚠️ Usually taken |
| 3pm | 73% | ⚠️ Usually taken |
| 4pm | 73% | ⚠️ Usually taken |
| 5pm | 73% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 45% | 🟡 Moderate demand |
| 12pm | 9% | ✅ Often available |
| 1pm | 9% | ✅ Often available |
| 2pm | 9% | ✅ Often available |
| 3pm | 18% | ✅ Often available |
| 4pm | 18% | ✅ Often available |
| 5pm | 73% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 22.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 64% | 🟡 Moderate demand |
| 12pm | 45% | 🟡 Moderate demand |
| 1pm | 18% | ✅ Often available |
| 2pm | 36% | 🟡 Moderate demand |
| 3pm | 45% | 🟡 Moderate demand |
| 4pm | 55% | 🟡 Moderate demand |
| 5pm | 73% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 18% | ✅ Often available |
| 12pm | 18% | ✅ Often available |
| 1pm | 36% | 🟡 Moderate demand |
| 2pm | 18% | ✅ Often available |
| 3pm | 27% | ✅ Often available |
| 4pm | 45% | 🟡 Moderate demand |
| 5pm | 45% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 26.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 91% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 91% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 91% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 91% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 91% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 91% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 91% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 91% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 91% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 91% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 14,497 |
| redmond | 3,201 |
| sammamish | 1,574 |
| kingsgate | 125 |
| issaquah | 117 |
| woodinville | 112 |

## Data Quality Notes
- Total records: 19,626
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 14,803
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 75% fresh — grows toward 100% as initial batch ages out
