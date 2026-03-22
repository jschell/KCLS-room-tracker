# KCLS Room Monitor Report
*Generated: 2026-03-22 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 4,823 |
| Date range | 2026-03-22 to 2026-04-19 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (100%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 981 |
| Tuesday | 965 |
| Wednesday | 1,015 |
| Thursday | 218 |
| Friday | 830 |
| Saturday | 370 |
| Sunday | 444 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 311 |
| 11am | 674 |
| 12pm | 657 |
| 1pm | 629 |
| 2pm | 560 |
| 3pm | 590 |
| 4pm | 696 |
| 5pm | 467 |
| 6pm | 156 |
| 7pm | 83 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 16.0 | 9.0 | 22.0 | 26.0 | 0.3% | 3702 (0 / 3702) |
| issaquah | 13.5 | 6.5 | 22.2 | 26.0 | 3.1% | 32 (0 / 32) |
| kingsgate | 14.0 | 8.0 | 22.0 | 25.2 | 0.0% | 29 (0 / 29) |
| redmond | 16.0 | 8.0 | 22.0 | 25.0 | 0.4% | 852 (0 / 852) |
| sammamish | 5.0 | 2.0 | 7.0 | 17.3 | 10.7% | 178 (0 / 178) |
| woodinville | 14.0 | 6.5 | 21.5 | 25.1 | 0.0% | 30 (0 / 30) |

*4,823 bookings total — 0 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 135 | 93 | 112 | 148 | 131 | 133 | 153 | 76 | 0 | 0 |
| Tuesday | 0 | 100 | 147 | 130 | 126 | 117 | 139 | 95 | 75 | 36 |
| Wednesday | 0 | 145 | 152 | 114 | 112 | 118 | 133 | 113 | 81 | 47 |
| Thursday | 39 | 8 | 17 | 24 | 20 | 33 | 51 | 26 | 0 | 0 |
| Friday | 137 | 97 | 122 | 94 | 84 | 112 | 112 | 72 | 0 | 0 |
| Saturday | 0 | 74 | 45 | 50 | 46 | 40 | 63 | 52 | 0 | 0 |
| Sunday | 0 | 157 | 62 | 69 | 41 | 37 | 45 | 33 | 0 | 0 |

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

**Typical lead time at Redmond:** median 16.0 days, p90 25.0 days

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

**Typical lead time at Sammamish:** median 5.0 days, p90 17.3 days

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
| 11am | 25% | ✅ Often available |
| 12pm | 25% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 0% | ✅ Often available |
| 4pm | 0% | ✅ Often available |
| 5pm | 25% | ✅ Often available |

**Typical lead time at Kingsgate:** median 14.0 days, p90 25.2 days

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

**Typical lead time at Issaquah:** median 13.5 days, p90 26.0 days

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

**Typical lead time at Bellevue:** median 16.0 days, p90 26.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 3,702 |
| redmond | 852 |
| sammamish | 178 |
| issaquah | 32 |
| woodinville | 30 |
| kingsgate | 29 |

## Data Quality Notes
- Total records: 4,823
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 0
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 0% fresh — grows toward 100% as initial batch ages out
