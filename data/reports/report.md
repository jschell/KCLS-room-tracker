# KCLS Room Monitor Report
*Generated: 2026-05-05 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 17,875 |
| Date range | 2026-03-22 to 2026-06-02 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (27%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 3,139 |
| Tuesday | 3,578 |
| Wednesday | 3,127 |
| Thursday | 1,195 |
| Friday | 2,879 |
| Saturday | 2,038 |
| Sunday | 1,919 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,092 |
| 11am | 2,330 |
| 12pm | 2,412 |
| 1pm | 2,399 |
| 2pm | 2,256 |
| 3pm | 2,322 |
| 4pm | 2,480 |
| 5pm | 1,607 |
| 6pm | 642 |
| 7pm | 335 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 26.0 | 28.0 | 28.0 | 0.2% | 13212 (9510 / 3702) |
| issaquah | 26.0 | 9.0 | 28.0 | 28.0 | 9.1% | 110 (78 / 32) |
| kingsgate | 27.0 | 8.5 | 28.0 | 28.0 | 11.7% | 111 (82 / 29) |
| redmond | 28.0 | 22.0 | 28.0 | 28.0 | 0.5% | 2928 (2076 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.3% | 1413 (1235 / 178) |
| woodinville | 22.0 | 4.0 | 28.0 | 28.0 | 19.8% | 101 (71 / 30) |

*17,875 bookings total — 13,052 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 416 | 295 | 346 | 481 | 443 | 445 | 472 | 241 | 0 | 0 |
| Tuesday | 0 | 365 | 514 | 458 | 451 | 440 | 454 | 375 | 348 | 173 |
| Wednesday | 0 | 405 | 462 | 357 | 346 | 375 | 400 | 326 | 294 | 162 |
| Thursday | 204 | 98 | 133 | 152 | 140 | 168 | 199 | 101 | 0 | 0 |
| Friday | 472 | 353 | 390 | 372 | 354 | 386 | 352 | 200 | 0 | 0 |
| Saturday | 0 | 375 | 288 | 303 | 292 | 266 | 312 | 202 | 0 | 0 |
| Sunday | 0 | 439 | 279 | 276 | 230 | 242 | 291 | 162 | 0 | 0 |

## Saturday Availability Windows
*Based on 10 Saturdays observed (2026-03-28 to 2026-05-30):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 80% | ⚠️ Usually taken |
| 1pm | 80% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 80% | ⚠️ Usually taken |
| 1pm | 80% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 80% | ⚠️ Usually taken |
| 1pm | 80% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 60% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 40% | 🟡 Moderate demand |
| 3pm | 40% | 🟡 Moderate demand |
| 4pm | 70% | 🟡 Moderate demand |
| 5pm | 90% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 70% | 🟡 Moderate demand |
| 12pm | 70% | 🟡 Moderate demand |
| 1pm | 70% | 🟡 Moderate demand |
| 2pm | 70% | 🟡 Moderate demand |
| 3pm | 70% | 🟡 Moderate demand |
| 4pm | 70% | 🟡 Moderate demand |
| 5pm | 70% | 🟡 Moderate demand |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 10% | ✅ Often available |
| 1pm | 10% | ✅ Often available |
| 2pm | 10% | ✅ Often available |
| 3pm | 20% | ✅ Often available |
| 4pm | 20% | ✅ Often available |
| 5pm | 80% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 22.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 40% | 🟡 Moderate demand |
| 1pm | 20% | ✅ Often available |
| 2pm | 30% | 🟡 Moderate demand |
| 3pm | 40% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 70% | 🟡 Moderate demand |

**Typical lead time at Kingsgate:** median 27.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 10% | ✅ Often available |
| 12pm | 10% | ✅ Often available |
| 1pm | 40% | 🟡 Moderate demand |
| 2pm | 20% | ✅ Often available |
| 3pm | 30% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 50% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 26.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 90% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 90% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 90% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 90% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 90% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 90% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 90% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 90% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 90% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 90% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 13,212 |
| redmond | 2,928 |
| sammamish | 1,413 |
| kingsgate | 111 |
| issaquah | 110 |
| woodinville | 101 |

## Data Quality Notes
- Total records: 17,875
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 13,052
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 73% fresh — grows toward 100% as initial batch ages out
