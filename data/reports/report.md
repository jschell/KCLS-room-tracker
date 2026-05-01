# KCLS Room Monitor Report
*Generated: 2026-05-01 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 16,561 |
| Date range | 2026-03-22 to 2026-05-29 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (29%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 2,759 |
| Tuesday | 3,168 |
| Wednesday | 3,124 |
| Thursday | 1,189 |
| Friday | 2,879 |
| Saturday | 1,783 |
| Sunday | 1,659 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,043 |
| 11am | 2,162 |
| 12pm | 2,235 |
| 1pm | 2,226 |
| 2pm | 2,083 |
| 3pm | 2,134 |
| 4pm | 2,283 |
| 5pm | 1,484 |
| 6pm | 598 |
| 7pm | 313 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 24.0 | 28.0 | 28.0 | 0.2% | 12247 (8545 / 3702) |
| issaquah | 25.5 | 8.8 | 28.0 | 28.0 | 9.6% | 104 (72 / 32) |
| kingsgate | 26.0 | 8.0 | 28.0 | 28.0 | 12.1% | 107 (78 / 29) |
| redmond | 28.0 | 19.0 | 28.0 | 28.0 | 0.6% | 2694 (1842 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.4% | 1313 (1135 / 178) |
| woodinville | 22.0 | 4.8 | 28.0 | 28.0 | 18.8% | 96 (66 / 30) |

*16,561 bookings total — 11,738 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 367 | 259 | 305 | 424 | 387 | 389 | 415 | 213 | 0 | 0 |
| Tuesday | 0 | 330 | 460 | 411 | 405 | 383 | 396 | 328 | 304 | 151 |
| Wednesday | 0 | 405 | 462 | 357 | 346 | 372 | 400 | 326 | 294 | 162 |
| Thursday | 204 | 98 | 128 | 152 | 140 | 168 | 199 | 100 | 0 | 0 |
| Friday | 472 | 353 | 390 | 372 | 354 | 386 | 352 | 200 | 0 | 0 |
| Saturday | 0 | 325 | 248 | 269 | 258 | 233 | 273 | 177 | 0 | 0 |
| Sunday | 0 | 392 | 242 | 241 | 193 | 203 | 248 | 140 | 0 | 0 |

## Saturday Availability Windows
*Based on 9 Saturdays observed (2026-03-28 to 2026-05-23):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 78% | ⚠️ Usually taken |
| 12pm | 78% | ⚠️ Usually taken |
| 1pm | 78% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 78% | ⚠️ Usually taken |
| 12pm | 78% | ⚠️ Usually taken |
| 1pm | 78% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 78% | ⚠️ Usually taken |
| 12pm | 78% | ⚠️ Usually taken |
| 1pm | 78% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 56% | 🟡 Moderate demand |
| 12pm | 56% | 🟡 Moderate demand |
| 1pm | 44% | 🟡 Moderate demand |
| 2pm | 44% | 🟡 Moderate demand |
| 3pm | 44% | 🟡 Moderate demand |
| 4pm | 67% | 🟡 Moderate demand |
| 5pm | 89% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 67% | 🟡 Moderate demand |
| 1pm | 67% | 🟡 Moderate demand |
| 2pm | 67% | 🟡 Moderate demand |
| 3pm | 67% | 🟡 Moderate demand |
| 4pm | 67% | 🟡 Moderate demand |
| 5pm | 67% | 🟡 Moderate demand |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 56% | 🟡 Moderate demand |
| 12pm | 11% | ✅ Often available |
| 1pm | 11% | ✅ Often available |
| 2pm | 11% | ✅ Often available |
| 3pm | 22% | ✅ Often available |
| 4pm | 22% | ✅ Often available |
| 5pm | 89% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 22.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 44% | 🟡 Moderate demand |
| 1pm | 22% | ✅ Often available |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 44% | 🟡 Moderate demand |
| 4pm | 56% | 🟡 Moderate demand |
| 5pm | 78% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 26.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 11% | ✅ Often available |
| 12pm | 11% | ✅ Often available |
| 1pm | 44% | 🟡 Moderate demand |
| 2pm | 22% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 56% | 🟡 Moderate demand |
| 5pm | 56% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 25.5 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 89% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 89% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 89% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 89% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 89% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 89% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 89% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 89% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 89% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 89% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 12,247 |
| redmond | 2,694 |
| sammamish | 1,313 |
| kingsgate | 107 |
| issaquah | 104 |
| woodinville | 96 |

## Data Quality Notes
- Total records: 16,561
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 11,738
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 71% fresh — grows toward 100% as initial batch ages out
