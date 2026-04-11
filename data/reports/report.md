# KCLS Room Monitor Report
*Generated: 2026-04-11 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 11,070 |
| Date range | 2026-03-22 to 2026-05-09 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (44%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 2,066 |
| Tuesday | 2,121 |
| Wednesday | 2,111 |
| Thursday | 671 |
| Friday | 1,843 |
| Saturday | 1,300 |
| Sunday | 958 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 689 |
| 11am | 1,460 |
| 12pm | 1,510 |
| 1pm | 1,491 |
| 2pm | 1,403 |
| 3pm | 1,431 |
| 4pm | 1,521 |
| 5pm | 991 |
| 6pm | 376 |
| 7pm | 198 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 17.0 | 28.0 | 28.0 | 0.3% | 8262 (4560 / 3702) |
| issaquah | 17.5 | 6.2 | 28.0 | 28.0 | 10.6% | 66 (34 / 32) |
| kingsgate | 22.5 | 8.0 | 28.0 | 28.0 | 10.3% | 68 (39 / 29) |
| redmond | 27.0 | 15.0 | 28.0 | 28.0 | 0.5% | 1842 (990 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 3.3% | 768 (590 / 178) |
| woodinville | 20.5 | 6.0 | 28.0 | 28.0 | 14.1% | 64 (34 / 30) |

*11,070 bookings total — 6,247 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 275 | 195 | 230 | 312 | 289 | 291 | 313 | 161 | 0 | 0 |
| Tuesday | 0 | 220 | 308 | 285 | 288 | 266 | 272 | 208 | 184 | 90 |
| Wednesday | 0 | 280 | 316 | 238 | 235 | 252 | 265 | 225 | 192 | 108 |
| Thursday | 116 | 48 | 68 | 81 | 74 | 95 | 126 | 63 | 0 | 0 |
| Friday | 298 | 222 | 257 | 229 | 218 | 251 | 234 | 134 | 0 | 0 |
| Saturday | 0 | 239 | 183 | 194 | 187 | 170 | 198 | 129 | 0 | 0 |
| Sunday | 0 | 256 | 148 | 152 | 112 | 106 | 113 | 71 | 0 | 0 |

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

**Typical lead time at Redmond:** median 27.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 43% | 🟡 Moderate demand |
| 12pm | 43% | 🟡 Moderate demand |
| 1pm | 43% | 🟡 Moderate demand |
| 2pm | 29% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
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

**Typical lead time at Woodinville:** median 20.5 days, p90 28.0 days

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

**Typical lead time at Issaquah:** median 17.5 days, p90 28.0 days

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
| bellevue | 8,262 |
| redmond | 1,842 |
| sammamish | 768 |
| kingsgate | 68 |
| issaquah | 66 |
| woodinville | 64 |

## Data Quality Notes
- Total records: 11,070
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 6,247
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 56% fresh — grows toward 100% as initial batch ages out
