# KCLS Room Monitor Report
*Generated: 2026-03-31 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 7,746 |
| Date range | 2026-03-22 to 2026-04-28 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (62%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 1,682 |
| Tuesday | 1,762 |
| Wednesday | 1,415 |
| Thursday | 365 |
| Friday | 1,094 |
| Saturday | 714 |
| Sunday | 714 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 480 |
| 11am | 1,023 |
| 12pm | 1,049 |
| 1pm | 1,041 |
| 2pm | 970 |
| 3pm | 986 |
| 4pm | 1,061 |
| 5pm | 723 |
| 6pm | 270 |
| 7pm | 143 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 24.0 | 12.0 | 28.0 | 28.0 | 0.3% | 5852 (2150 / 3702) |
| issaquah | 17.0 | 7.0 | 27.0 | 28.0 | 10.0% | 50 (18 / 32) |
| kingsgate | 17.0 | 6.0 | 27.5 | 28.0 | 8.5% | 47 (18 / 29) |
| redmond | 22.0 | 12.0 | 28.0 | 28.0 | 0.5% | 1317 (465 / 852) |
| sammamish | 7.0 | 5.0 | 7.0 | 7.0 | 5.3% | 436 (258 / 178) |
| woodinville | 17.5 | 7.5 | 26.2 | 28.0 | 6.8% | 44 (14 / 30) |

*7,746 bookings total — 2,923 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 227 | 159 | 188 | 251 | 233 | 235 | 256 | 133 | 0 | 0 |
| Tuesday | 0 | 185 | 261 | 239 | 242 | 222 | 228 | 171 | 144 | 70 |
| Wednesday | 0 | 190 | 212 | 159 | 155 | 168 | 175 | 157 | 126 | 73 |
| Thursday | 69 | 23 | 37 | 44 | 39 | 49 | 68 | 36 | 0 | 0 |
| Friday | 184 | 131 | 164 | 136 | 118 | 141 | 136 | 84 | 0 | 0 |
| Saturday | 0 | 130 | 90 | 103 | 103 | 91 | 112 | 85 | 0 | 0 |
| Sunday | 0 | 205 | 97 | 109 | 80 | 80 | 86 | 57 | 0 | 0 |

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

**Typical lead time at Redmond:** median 22.0 days, p90 28.0 days

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

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

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

**Typical lead time at Woodinville:** median 17.5 days, p90 28.0 days

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

**Typical lead time at Kingsgate:** median 17.0 days, p90 28.0 days

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
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 80% | ⚠️ Usually taken |
| 3pm | 80% | ⚠️ Usually taken |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 80% | ⚠️ Usually taken |
| 3pm | 80% | ⚠️ Usually taken |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 80% | ⚠️ Usually taken |
| 3pm | 80% | ⚠️ Usually taken |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 80% | ⚠️ Usually taken |
| 3pm | 80% | ⚠️ Usually taken |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 80% | ⚠️ Usually taken |
| 3pm | 80% | ⚠️ Usually taken |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 24.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 5,852 |
| redmond | 1,317 |
| sammamish | 436 |
| issaquah | 50 |
| kingsgate | 47 |
| woodinville | 44 |

## Data Quality Notes
- Total records: 7,746
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 2,923
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 38% fresh — grows toward 100% as initial batch ages out
