# KCLS Room Monitor Report
*Generated: 2026-03-25 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 5,917 |
| Date range | 2026-03-22 to 2026-04-22 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (82%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 1,304 |
| Tuesday | 1,324 |
| Wednesday | 1,396 |
| Thursday | 225 |
| Friday | 830 |
| Saturday | 387 |
| Sunday | 451 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 357 |
| 11am | 792 |
| 12pm | 803 |
| 1pm | 775 |
| 2pm | 717 |
| 3pm | 736 |
| 4pm | 823 |
| 5pm | 571 |
| 6pm | 225 |
| 7pm | 118 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 17.0 | 10.0 | 27.0 | 28.0 | 0.3% | 4537 (835 / 3702) |
| issaquah | 16.0 | 7.0 | 26.0 | 28.0 | 4.9% | 41 (9 / 32) |
| kingsgate | 14.5 | 6.5 | 24.0 | 27.5 | 5.6% | 36 (7 / 29) |
| redmond | 18.0 | 9.8 | 25.0 | 28.0 | 0.6% | 1008 (156 / 852) |
| sammamish | 7.0 | 3.0 | 7.0 | 14.1 | 8.5% | 260 (82 / 178) |
| woodinville | 16.0 | 7.0 | 23.5 | 27.0 | 2.9% | 35 (5 / 30) |

*5,917 bookings total — 1,094 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 180 | 123 | 147 | 193 | 177 | 179 | 200 | 105 | 0 | 0 |
| Tuesday | 0 | 140 | 200 | 181 | 184 | 170 | 175 | 127 | 99 | 48 |
| Wednesday | 0 | 190 | 209 | 159 | 154 | 162 | 173 | 153 | 126 | 70 |
| Thursday | 40 | 8 | 17 | 24 | 25 | 33 | 52 | 26 | 0 | 0 |
| Friday | 137 | 97 | 122 | 94 | 84 | 112 | 112 | 72 | 0 | 0 |
| Saturday | 0 | 74 | 45 | 55 | 52 | 40 | 66 | 55 | 0 | 0 |
| Sunday | 0 | 160 | 63 | 69 | 41 | 40 | 45 | 33 | 0 | 0 |

## Saturday Availability Windows
*Based on 4 Saturdays observed (2026-03-28 to 2026-04-18):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 75% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 75% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 75% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 18.0 days, p90 28.0 days

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

**Typical lead time at Sammamish:** median 7.0 days, p90 14.1 days

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

**Typical lead time at Woodinville:** median 16.0 days, p90 27.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 25% | ✅ Often available |
| 12pm | 25% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 25% | ✅ Often available |

**Typical lead time at Kingsgate:** median 14.5 days, p90 27.5 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 25% | ✅ Often available |
| 12pm | 25% | ✅ Often available |
| 1pm | 25% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 25% | ✅ Often available |
| 5pm | 25% | ✅ Often available |

**Typical lead time at Issaquah:** median 16.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 50% | 🟡 Moderate demand |
| 4pm | 75% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 50% | 🟡 Moderate demand |
| 4pm | 75% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 50% | 🟡 Moderate demand |
| 4pm | 75% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 50% | 🟡 Moderate demand |
| 4pm | 75% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 75% | ⚠️ Usually taken |
| 1pm | 75% | ⚠️ Usually taken |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 50% | 🟡 Moderate demand |
| 4pm | 75% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 17.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 4,537 |
| redmond | 1,008 |
| sammamish | 260 |
| issaquah | 41 |
| kingsgate | 36 |
| woodinville | 35 |

## Data Quality Notes
- Total records: 5,917
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 1,094
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 18% fresh — grows toward 100% as initial batch ages out
