# KCLS Room Monitor Report
*Generated: 2026-04-14 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 12,021 |
| Date range | 2026-03-22 to 2026-05-12 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (40%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 2,381 |
| Tuesday | 2,440 |
| Wednesday | 2,116 |
| Thursday | 671 |
| Friday | 1,844 |
| Saturday | 1,302 |
| Sunday | 1,267 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 731 |
| 11am | 1,572 |
| 12pm | 1,629 |
| 1pm | 1,630 |
| 2pm | 1,527 |
| 3pm | 1,557 |
| 4pm | 1,660 |
| 5pm | 1,081 |
| 6pm | 416 |
| 7pm | 218 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 17.0 | 28.0 | 28.0 | 0.2% | 8942 (5240 / 3702) |
| issaquah | 18.5 | 5.8 | 28.0 | 28.0 | 11.1% | 72 (40 / 32) |
| kingsgate | 22.5 | 8.0 | 28.0 | 28.0 | 10.5% | 76 (47 / 29) |
| redmond | 28.0 | 16.0 | 28.0 | 28.0 | 0.6% | 2007 (1155 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 3.0% | 855 (677 / 178) |
| woodinville | 20.0 | 6.0 | 28.0 | 28.0 | 14.5% | 69 (39 / 30) |

*12,021 bookings total — 7,198 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 317 | 225 | 266 | 365 | 333 | 335 | 357 | 183 | 0 | 0 |
| Tuesday | 0 | 250 | 350 | 328 | 323 | 298 | 309 | 248 | 224 | 110 |
| Wednesday | 0 | 280 | 316 | 238 | 235 | 256 | 266 | 225 | 192 | 108 |
| Thursday | 116 | 48 | 68 | 81 | 74 | 95 | 126 | 63 | 0 | 0 |
| Friday | 298 | 222 | 258 | 229 | 218 | 251 | 234 | 134 | 0 | 0 |
| Saturday | 0 | 239 | 183 | 194 | 188 | 170 | 199 | 129 | 0 | 0 |
| Sunday | 0 | 308 | 188 | 195 | 156 | 152 | 169 | 99 | 0 | 0 |

## Saturday Availability Windows
*Based on 7 Saturdays observed (2026-03-28 to 2026-05-09):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 71% | ⚠️ Usually taken |
| 12pm | 71% | ⚠️ Usually taken |
| 1pm | 71% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 71% | ⚠️ Usually taken |
| 12pm | 71% | ⚠️ Usually taken |
| 1pm | 71% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 71% | ⚠️ Usually taken |
| 12pm | 71% | ⚠️ Usually taken |
| 1pm | 71% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 43% | 🟡 Moderate demand |
| 12pm | 43% | 🟡 Moderate demand |
| 1pm | 43% | 🟡 Moderate demand |
| 2pm | 43% | 🟡 Moderate demand |
| 3pm | 43% | 🟡 Moderate demand |
| 4pm | 57% | 🟡 Moderate demand |
| 5pm | 86% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 57% | 🟡 Moderate demand |
| 12pm | 57% | 🟡 Moderate demand |
| 1pm | 57% | 🟡 Moderate demand |
| 2pm | 57% | 🟡 Moderate demand |
| 3pm | 57% | 🟡 Moderate demand |
| 4pm | 57% | 🟡 Moderate demand |
| 5pm | 57% | 🟡 Moderate demand |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 57% | 🟡 Moderate demand |
| 12pm | 14% | ✅ Often available |
| 1pm | 14% | ✅ Often available |
| 2pm | 14% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 29% | ✅ Often available |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 20.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 71% | ⚠️ Usually taken |
| 12pm | 43% | 🟡 Moderate demand |
| 1pm | 14% | ✅ Often available |
| 2pm | 29% | ✅ Often available |
| 3pm | 43% | 🟡 Moderate demand |
| 4pm | 57% | 🟡 Moderate demand |
| 5pm | 71% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 22.5 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 14% | ✅ Often available |
| 12pm | 14% | ✅ Often available |
| 1pm | 29% | ✅ Often available |
| 2pm | 14% | ✅ Often available |
| 3pm | 14% | ✅ Often available |
| 4pm | 29% | ✅ Often available |
| 5pm | 29% | ✅ Often available |

**Typical lead time at Issaquah:** median 18.5 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 86% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 86% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 86% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 86% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 86% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 86% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 86% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 86% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 86% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 86% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 8,942 |
| redmond | 2,007 |
| sammamish | 855 |
| kingsgate | 76 |
| issaquah | 72 |
| woodinville | 69 |

## Data Quality Notes
- Total records: 12,021
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 7,198
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 60% fresh — grows toward 100% as initial batch ages out
