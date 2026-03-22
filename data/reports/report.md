# KCLS Room Monitor Report
*Generated: 2026-03-22 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 1,099 |
| Date range | 2026-03-22 to 2026-04-18 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 1,099 (100%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 339 |
| Tuesday | 196 |
| Wednesday | 42 |
| Thursday | 141 |
| Friday | 229 |
| Saturday | 81 |
| Sunday | 71 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 102 |
| 11am | 103 |
| 12pm | 171 |
| 1pm | 148 |
| 2pm | 124 |
| 3pm | 157 |
| 4pm | 186 |
| 5pm | 99 |
| 6pm | 1 |
| 7pm | 8 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 1.0 | 1.0 | 1.0 | 1.0 | 17.4% | 69 (0 / 69) |
| issaquah | 0.5 | 0.2 | 0.8 | 0.9 | 50.0% | 2 (0 / 2) |
| kingsgate | 1.0 | 1.0 | 1.0 | 1.0 | 0.0% | 1 (0 / 1) |
| redmond | 15.5 | 8.0 | 22.0 | 25.0 | 0.4% | 840 (0 / 840) |
| sammamish | 4.0 | 1.0 | 6.0 | 17.4 | 12.1% | 157 (0 / 157) |
| woodinville | 14.0 | 6.5 | 21.5 | 25.1 | 0.0% | 30 (0 / 30) |

*1,099 bookings total — 0 fresh-caught (accurate), 1,099 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 58 | 37 | 37 | 52 | 41 | 42 | 48 | 24 | 0 | 0 |
| Tuesday | 0 | 0 | 54 | 30 | 33 | 30 | 38 | 10 | 0 | 1 |
| Wednesday | 0 | 0 | 24 | 4 | 2 | 3 | 0 | 1 | 1 | 7 |
| Thursday | 13 | 0 | 17 | 18 | 14 | 28 | 31 | 20 | 0 | 0 |
| Friday | 31 | 10 | 22 | 24 | 18 | 46 | 52 | 26 | 0 | 0 |
| Saturday | 0 | 27 | 10 | 10 | 11 | 0 | 7 | 16 | 0 | 0 |
| Sunday | 0 | 29 | 7 | 10 | 5 | 8 | 10 | 2 | 0 | 0 |

## Saturday Availability Windows
*Based on 4 Saturdays observed (2026-03-28 to 2026-04-18):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 25% | ✅ Often available |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 25% | ✅ Often available |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 25% | ✅ Often available |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 15.5 days, p90 25.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 25% | ✅ Often available |
| 12pm | 25% | ✅ Often available |
| 1pm | 25% | ✅ Often available |
| 2pm | 25% | ✅ Often available |
| 3pm | 25% | ✅ Often available |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 25% | ✅ Often available |
| 12pm | 25% | ✅ Often available |
| 1pm | 25% | ✅ Often available |
| 2pm | 25% | ✅ Often available |
| 3pm | 25% | ✅ Often available |
| 4pm | 25% | ✅ Often available |
| 5pm | 25% | ✅ Often available |

**Typical lead time at Sammamish:** median 4.0 days, p90 17.4 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 25% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 14.0 days, p90 25.1 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 0% | ✅ Often available |
| 12pm | 0% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 0% | ✅ Often available |

**Typical lead time at Kingsgate:** median 1.0 days, p90 1.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 0% | ✅ Often available |
| 12pm | 0% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 0% | ✅ Often available |

**Typical lead time at Issaquah:** median 0.5 days, p90 0.9 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 0% | ✅ Often available |
| 12pm | 0% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 0% | ✅ Often available |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 0% | ✅ Often available |
| 12pm | 0% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 0% | ✅ Often available |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 0% | ✅ Often available |
| 12pm | 0% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 0% | ✅ Often available |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 0% | ✅ Often available |
| 12pm | 0% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 0% | ✅ Often available |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 0% | ✅ Often available |
| 12pm | 0% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 0% | ✅ Often available |

**Typical lead time at Bellevue:** median 1.0 days, p90 1.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| redmond | 840 |
| sammamish | 157 |
| bellevue | 69 |
| woodinville | 30 |
| issaquah | 2 |
| kingsgate | 1 |

## Data Quality Notes
- Total records: 1,099
- Records missing `created` timestamp: 1,099
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 0
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 1,099
- Data maturity: 0% fresh — grows toward 100% as initial batch ages out
