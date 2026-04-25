# KCLS Room Monitor Report
*Generated: 2026-04-25 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 15,107 |
| Date range | 2026-03-22 to 2026-05-23 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (32%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 2,728 |
| Tuesday | 2,795 |
| Wednesday | 2,804 |
| Thursday | 1,034 |
| Friday | 2,537 |
| Saturday | 1,779 |
| Sunday | 1,430 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 949 |
| 11am | 1,959 |
| 12pm | 2,023 |
| 1pm | 2,037 |
| 2pm | 1,913 |
| 3pm | 1,964 |
| 4pm | 2,099 |
| 5pm | 1,364 |
| 6pm | 524 |
| 7pm | 275 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 22.0 | 28.0 | 28.0 | 0.2% | 11202 (7500 / 3702) |
| issaquah | 23.0 | 8.0 | 28.0 | 28.0 | 10.3% | 97 (65 / 32) |
| kingsgate | 24.5 | 8.0 | 28.0 | 28.0 | 11.5% | 96 (67 / 29) |
| redmond | 28.0 | 18.0 | 28.0 | 28.0 | 0.6% | 2445 (1593 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.6% | 1179 (1001 / 178) |
| woodinville | 22.0 | 6.0 | 28.0 | 28.0 | 15.9% | 88 (58 / 30) |

*15,107 bookings total — 10,284 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 362 | 255 | 301 | 420 | 383 | 385 | 411 | 211 | 0 | 0 |
| Tuesday | 0 | 285 | 402 | 368 | 362 | 341 | 353 | 290 | 264 | 130 |
| Wednesday | 0 | 360 | 410 | 321 | 313 | 341 | 358 | 296 | 260 | 145 |
| Thursday | 173 | 83 | 113 | 129 | 119 | 148 | 179 | 90 | 0 | 0 |
| Friday | 414 | 307 | 342 | 324 | 308 | 345 | 316 | 181 | 0 | 0 |
| Saturday | 0 | 325 | 248 | 266 | 258 | 233 | 272 | 177 | 0 | 0 |
| Sunday | 0 | 344 | 207 | 209 | 170 | 171 | 210 | 119 | 0 | 0 |

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

**Typical lead time at Kingsgate:** median 24.5 days, p90 28.0 days

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

**Typical lead time at Issaquah:** median 23.0 days, p90 28.0 days

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
| bellevue | 11,202 |
| redmond | 2,445 |
| sammamish | 1,179 |
| issaquah | 97 |
| kingsgate | 96 |
| woodinville | 88 |

## Data Quality Notes
- Total records: 15,107
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 10,284
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 68% fresh — grows toward 100% as initial batch ages out
