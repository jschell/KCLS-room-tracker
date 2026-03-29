# KCLS Room Monitor Report
*Generated: 2026-03-29 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 6,905 |
| Date range | 2026-03-22 to 2026-04-26 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (70%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 1,304 |
| Tuesday | 1,325 |
| Wednesday | 1,409 |
| Thursday | 360 |
| Friday | 1,093 |
| Saturday | 703 |
| Sunday | 711 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 428 |
| 11am | 937 |
| 12pm | 944 |
| 1pm | 920 |
| 2pm | 857 |
| 3pm | 873 |
| 4pm | 952 |
| 5pm | 651 |
| 6pm | 225 |
| 7pm | 118 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 21.0 | 10.0 | 28.0 | 28.0 | 0.3% | 5242 (1540 / 3702) |
| issaquah | 17.0 | 7.5 | 27.0 | 28.0 | 6.4% | 47 (15 / 32) |
| kingsgate | 16.5 | 6.5 | 27.0 | 28.0 | 9.1% | 44 (15 / 29) |
| redmond | 19.0 | 11.0 | 27.0 | 28.0 | 0.5% | 1152 (300 / 852) |
| sammamish | 7.0 | 5.0 | 7.0 | 9.1 | 6.1% | 380 (202 / 178) |
| woodinville | 17.0 | 7.5 | 25.0 | 28.0 | 5.0% | 40 (10 / 30) |

*6,905 bookings total — 2,082 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 180 | 123 | 147 | 193 | 177 | 179 | 200 | 105 | 0 | 0 |
| Tuesday | 0 | 140 | 200 | 181 | 185 | 170 | 175 | 127 | 99 | 48 |
| Wednesday | 0 | 190 | 209 | 159 | 155 | 168 | 175 | 157 | 126 | 70 |
| Thursday | 64 | 23 | 37 | 44 | 39 | 49 | 68 | 36 | 0 | 0 |
| Friday | 184 | 131 | 164 | 135 | 118 | 141 | 136 | 84 | 0 | 0 |
| Saturday | 0 | 125 | 90 | 102 | 103 | 86 | 112 | 85 | 0 | 0 |
| Sunday | 0 | 205 | 97 | 106 | 80 | 80 | 86 | 57 | 0 | 0 |

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

**Typical lead time at Sammamish:** median 7.0 days, p90 9.1 days

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

**Typical lead time at Kingsgate:** median 16.5 days, p90 28.0 days

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

**Typical lead time at Bellevue:** median 21.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 5,242 |
| redmond | 1,152 |
| sammamish | 380 |
| issaquah | 47 |
| kingsgate | 44 |
| woodinville | 40 |

## Data Quality Notes
- Total records: 6,905
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 2,082
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 30% fresh — grows toward 100% as initial batch ages out
