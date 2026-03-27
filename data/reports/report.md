# KCLS Room Monitor Report
*Generated: 2026-03-27 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 6,324 |
| Date range | 2026-03-22 to 2026-04-24 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (76%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 1,304 |
| Tuesday | 1,324 |
| Wednesday | 1,405 |
| Thursday | 360 |
| Friday | 1,093 |
| Saturday | 387 |
| Sunday | 451 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 428 |
| 11am | 841 |
| 12pm | 865 |
| 1pm | 836 |
| 2pm | 765 |
| 3pm | 784 |
| 4pm | 865 |
| 5pm | 597 |
| 6pm | 225 |
| 7pm | 118 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 19.0 | 10.0 | 28.0 | 28.0 | 0.2% | 4827 (1125 / 3702) |
| issaquah | 16.5 | 7.0 | 26.2 | 28.0 | 6.8% | 44 (12 / 32) |
| kingsgate | 14.5 | 5.0 | 24.2 | 28.0 | 10.0% | 40 (11 / 29) |
| redmond | 18.0 | 10.0 | 26.0 | 28.0 | 0.6% | 1053 (201 / 852) |
| sammamish | 7.0 | 4.0 | 7.0 | 11.0 | 7.1% | 323 (145 / 178) |
| woodinville | 16.0 | 6.0 | 24.0 | 27.4 | 5.4% | 37 (7 / 30) |

*6,324 bookings total — 1,501 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 180 | 123 | 147 | 193 | 177 | 179 | 200 | 105 | 0 | 0 |
| Tuesday | 0 | 140 | 200 | 181 | 184 | 170 | 175 | 127 | 99 | 48 |
| Wednesday | 0 | 190 | 209 | 159 | 154 | 165 | 175 | 157 | 126 | 70 |
| Thursday | 64 | 23 | 37 | 44 | 39 | 49 | 68 | 36 | 0 | 0 |
| Friday | 184 | 131 | 164 | 135 | 118 | 141 | 136 | 84 | 0 | 0 |
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

**Typical lead time at Sammamish:** median 7.0 days, p90 11.0 days

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

**Typical lead time at Woodinville:** median 16.0 days, p90 27.4 days

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

**Typical lead time at Kingsgate:** median 14.5 days, p90 28.0 days

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

**Typical lead time at Issaquah:** median 16.5 days, p90 28.0 days

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

**Typical lead time at Bellevue:** median 19.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 4,827 |
| redmond | 1,053 |
| sammamish | 323 |
| issaquah | 44 |
| kingsgate | 40 |
| woodinville | 37 |

## Data Quality Notes
- Total records: 6,324
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 1,501
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 24% fresh — grows toward 100% as initial batch ages out
