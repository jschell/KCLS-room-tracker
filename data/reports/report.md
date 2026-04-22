# KCLS Room Monitor Report
*Generated: 2026-04-22 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 14,201 |
| Date range | 2026-03-22 to 2026-05-20 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (34%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 2,726 |
| Tuesday | 2,795 |
| Wednesday | 2,801 |
| Thursday | 833 |
| Friday | 2,134 |
| Saturday | 1,482 |
| Sunday | 1,430 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 855 |
| 11am | 1,836 |
| 12pm | 1,905 |
| 1pm | 1,905 |
| 2pm | 1,785 |
| 3pm | 1,836 |
| 4pm | 1,982 |
| 5pm | 1,298 |
| 6pm | 524 |
| 7pm | 275 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 21.0 | 28.0 | 28.0 | 0.2% | 10627 (6925 / 3702) |
| issaquah | 21.5 | 8.0 | 28.0 | 28.0 | 10.0% | 90 (58 / 32) |
| kingsgate | 24.0 | 8.0 | 28.0 | 28.0 | 12.1% | 91 (62 / 29) |
| redmond | 28.0 | 16.0 | 28.0 | 28.0 | 0.7% | 2223 (1371 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.6% | 1088 (910 / 178) |
| woodinville | 21.5 | 6.0 | 28.0 | 28.0 | 15.9% | 82 (52 / 30) |

*14,201 bookings total — 9,378 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 362 | 255 | 301 | 418 | 383 | 385 | 411 | 211 | 0 | 0 |
| Tuesday | 0 | 285 | 402 | 368 | 362 | 341 | 353 | 290 | 264 | 130 |
| Wednesday | 0 | 360 | 410 | 321 | 313 | 338 | 358 | 296 | 260 | 145 |
| Thursday | 142 | 62 | 85 | 100 | 93 | 121 | 153 | 77 | 0 | 0 |
| Friday | 351 | 257 | 292 | 266 | 252 | 289 | 270 | 157 | 0 | 0 |
| Saturday | 0 | 273 | 208 | 223 | 212 | 191 | 227 | 148 | 0 | 0 |
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

**Typical lead time at Woodinville:** median 21.5 days, p90 28.0 days

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

**Typical lead time at Issaquah:** median 21.5 days, p90 28.0 days

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
| bellevue | 10,627 |
| redmond | 2,223 |
| sammamish | 1,088 |
| kingsgate | 91 |
| issaquah | 90 |
| woodinville | 82 |

## Data Quality Notes
- Total records: 14,201
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 9,378
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 66% fresh — grows toward 100% as initial batch ages out
