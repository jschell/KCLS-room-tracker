# KCLS Room Monitor Report
*Generated: 2026-03-28 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 6,636 |
| Date range | 2026-03-22 to 2026-04-25 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (73%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 1,304 |
| Tuesday | 1,324 |
| Wednesday | 1,406 |
| Thursday | 360 |
| Friday | 1,093 |
| Saturday | 698 |
| Sunday | 451 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 428 |
| 11am | 892 |
| 12pm | 910 |
| 1pm | 883 |
| 2pm | 812 |
| 3pm | 830 |
| 4pm | 911 |
| 5pm | 627 |
| 6pm | 225 |
| 7pm | 118 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 20.0 | 10.0 | 28.0 | 28.0 | 0.3% | 5037 (1335 / 3702) |
| issaquah | 17.0 | 7.0 | 27.0 | 28.0 | 6.7% | 45 (13 / 32) |
| kingsgate | 15.0 | 5.0 | 25.0 | 28.0 | 9.8% | 41 (12 / 29) |
| redmond | 19.0 | 11.0 | 27.0 | 28.0 | 0.5% | 1122 (270 / 852) |
| sammamish | 7.0 | 5.0 | 7.0 | 10.0 | 6.6% | 351 (173 / 178) |
| woodinville | 17.0 | 7.5 | 25.0 | 28.0 | 5.0% | 40 (10 / 30) |

*6,636 bookings total — 1,813 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 180 | 123 | 147 | 193 | 177 | 179 | 200 | 105 | 0 | 0 |
| Tuesday | 0 | 140 | 200 | 181 | 184 | 170 | 175 | 127 | 99 | 48 |
| Wednesday | 0 | 190 | 209 | 159 | 155 | 165 | 175 | 157 | 126 | 70 |
| Thursday | 64 | 23 | 37 | 44 | 39 | 49 | 68 | 36 | 0 | 0 |
| Friday | 184 | 131 | 164 | 135 | 118 | 141 | 136 | 84 | 0 | 0 |
| Saturday | 0 | 125 | 90 | 102 | 98 | 86 | 112 | 85 | 0 | 0 |
| Sunday | 0 | 160 | 63 | 69 | 41 | 40 | 45 | 33 | 0 | 0 |

## Saturday Availability Windows
*Based on 5 Saturdays observed (2026-03-28 to 2026-04-25):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 60% | 🟡 Moderate demand |
| 1pm | 60% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 80% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 60% | 🟡 Moderate demand |
| 1pm | 60% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 80% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 60% | 🟡 Moderate demand |
| 1pm | 60% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 80% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 19.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 20% | ✅ Often available |
| 12pm | 20% | ✅ Often available |
| 1pm | 20% | ✅ Often available |
| 2pm | 20% | ✅ Often available |
| 3pm | 20% | ✅ Often available |
| 4pm | 40% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 40% | 🟡 Moderate demand |
| 12pm | 40% | 🟡 Moderate demand |
| 1pm | 40% | 🟡 Moderate demand |
| 2pm | 40% | 🟡 Moderate demand |
| 3pm | 40% | 🟡 Moderate demand |
| 4pm | 40% | 🟡 Moderate demand |
| 5pm | 40% | 🟡 Moderate demand |

**Typical lead time at Sammamish:** median 7.0 days, p90 10.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 20% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 17.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 40% | 🟡 Moderate demand |
| 12pm | 40% | 🟡 Moderate demand |
| 1pm | 20% | ✅ Often available |
| 2pm | 20% | ✅ Often available |
| 3pm | 20% | ✅ Often available |
| 4pm | 20% | ✅ Often available |
| 5pm | 40% | 🟡 Moderate demand |

**Typical lead time at Kingsgate:** median 15.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 20% | ✅ Often available |
| 12pm | 20% | ✅ Often available |
| 1pm | 40% | 🟡 Moderate demand |
| 2pm | 20% | ✅ Often available |
| 3pm | 20% | ✅ Often available |
| 4pm | 40% | 🟡 Moderate demand |
| 5pm | 40% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 17.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 80% | ⚠️ Usually taken |
| 1pm | 80% | ⚠️ Usually taken |
| 2pm | 60% | 🟡 Moderate demand |
| 3pm | 60% | 🟡 Moderate demand |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 80% | ⚠️ Usually taken |
| 1pm | 80% | ⚠️ Usually taken |
| 2pm | 60% | 🟡 Moderate demand |
| 3pm | 60% | 🟡 Moderate demand |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 80% | ⚠️ Usually taken |
| 1pm | 80% | ⚠️ Usually taken |
| 2pm | 60% | 🟡 Moderate demand |
| 3pm | 60% | 🟡 Moderate demand |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 80% | ⚠️ Usually taken |
| 1pm | 80% | ⚠️ Usually taken |
| 2pm | 60% | 🟡 Moderate demand |
| 3pm | 60% | 🟡 Moderate demand |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 80% | ⚠️ Usually taken |
| 12pm | 80% | ⚠️ Usually taken |
| 1pm | 80% | ⚠️ Usually taken |
| 2pm | 60% | 🟡 Moderate demand |
| 3pm | 60% | 🟡 Moderate demand |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 20.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 5,037 |
| redmond | 1,122 |
| sammamish | 351 |
| issaquah | 45 |
| kingsgate | 41 |
| woodinville | 40 |

## Data Quality Notes
- Total records: 6,636
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 1,813
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 27% fresh — grows toward 100% as initial batch ages out
