# KCLS Room Monitor Report
*Generated: 2026-04-21 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 13,878 |
| Date range | 2026-03-22 to 2026-05-19 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (35%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 2,726 |
| Tuesday | 2,795 |
| Wednesday | 2,482 |
| Thursday | 832 |
| Friday | 2,132 |
| Saturday | 1,481 |
| Sunday | 1,430 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 854 |
| 11am | 1,801 |
| 12pm | 1,863 |
| 1pm | 1,867 |
| 2pm | 1,751 |
| 3pm | 1,800 |
| 4pm | 1,936 |
| 5pm | 1,261 |
| 6pm | 490 |
| 7pm | 255 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 20.0 | 28.0 | 28.0 | 0.2% | 10357 (6655 / 3702) |
| issaquah | 22.0 | 7.0 | 28.0 | 28.0 | 10.6% | 85 (53 / 32) |
| kingsgate | 24.0 | 8.0 | 28.0 | 28.0 | 11.4% | 88 (59 / 29) |
| redmond | 28.0 | 16.0 | 28.0 | 28.0 | 0.5% | 2214 (1362 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.7% | 1055 (877 / 178) |
| woodinville | 22.0 | 5.5 | 28.0 | 28.0 | 16.5% | 79 (49 / 30) |

*13,878 bookings total — 9,055 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 362 | 255 | 301 | 418 | 383 | 385 | 411 | 211 | 0 | 0 |
| Tuesday | 0 | 285 | 402 | 368 | 362 | 341 | 353 | 290 | 264 | 130 |
| Wednesday | 0 | 325 | 368 | 283 | 279 | 303 | 312 | 261 | 226 | 125 |
| Thursday | 142 | 62 | 85 | 100 | 93 | 121 | 153 | 76 | 0 | 0 |
| Friday | 350 | 257 | 292 | 266 | 252 | 288 | 270 | 157 | 0 | 0 |
| Saturday | 0 | 273 | 208 | 223 | 212 | 191 | 227 | 147 | 0 | 0 |
| Sunday | 0 | 344 | 207 | 209 | 170 | 171 | 210 | 119 | 0 | 0 |

## Saturday Availability Windows
*Based on 8 Saturdays observed (2026-03-28 to 2026-05-16):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 38% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 38% | 🟡 Moderate demand |
| 4pm | 62% | 🟡 Moderate demand |
| 5pm | 88% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 62% | 🟡 Moderate demand |
| 12pm | 62% | 🟡 Moderate demand |
| 1pm | 62% | 🟡 Moderate demand |
| 2pm | 62% | 🟡 Moderate demand |
| 3pm | 62% | 🟡 Moderate demand |
| 4pm | 62% | 🟡 Moderate demand |
| 5pm | 62% | 🟡 Moderate demand |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 12% | ✅ Often available |
| 1pm | 12% | ✅ Often available |
| 2pm | 12% | ✅ Often available |
| 3pm | 25% | ✅ Often available |
| 4pm | 25% | ✅ Often available |
| 5pm | 88% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 22.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 62% | 🟡 Moderate demand |
| 12pm | 38% | 🟡 Moderate demand |
| 1pm | 12% | ✅ Often available |
| 2pm | 25% | ✅ Often available |
| 3pm | 38% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 24.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 12% | ✅ Often available |
| 12pm | 12% | ✅ Often available |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 25% | ✅ Often available |
| 3pm | 38% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 50% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 22.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 88% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 88% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 88% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 88% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 88% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 88% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 88% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 88% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 88% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 88% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 10,357 |
| redmond | 2,214 |
| sammamish | 1,055 |
| kingsgate | 88 |
| issaquah | 85 |
| woodinville | 79 |

## Data Quality Notes
- Total records: 13,878
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 9,055
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 65% fresh — grows toward 100% as initial batch ages out
