# KCLS Room Monitor Report
*Generated: 2026-07-11 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 38,171 |
| Date range | 2026-03-22 to 2026-08-08 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (13%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 6,544 |
| Tuesday | 7,200 |
| Wednesday | 6,761 |
| Thursday | 2,759 |
| Friday | 6,350 |
| Saturday | 4,325 |
| Sunday | 4,232 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,337 |
| 11am | 4,996 |
| 12pm | 5,099 |
| 1pm | 5,126 |
| 2pm | 4,932 |
| 3pm | 4,944 |
| 4pm | 5,252 |
| 5pm | 3,366 |
| 6pm | 1,380 |
| 7pm | 739 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 28247 (24545 / 3702) |
| issaquah | 28.0 | 6.2 | 28.0 | 28.0 | 17.2% | 238 (206 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 19.4% | 247 (218 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.2% | 6081 (5229 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 3151 (2973 / 178) |
| woodinville | 26.0 | 2.5 | 28.0 | 28.0 | 22.7% | 207 (177 / 30) |

*38,171 bookings total — 33,348 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 856 | 620 | 717 | 984 | 954 | 943 | 978 | 492 | 0 | 0 |
| Tuesday | 0 | 745 | 1025 | 922 | 905 | 900 | 891 | 736 | 702 | 374 |
| Wednesday | 0 | 825 | 947 | 771 | 771 | 804 | 873 | 727 | 678 | 365 |
| Thursday | 468 | 253 | 315 | 367 | 352 | 372 | 415 | 217 | 0 | 0 |
| Friday | 1013 | 778 | 812 | 824 | 823 | 856 | 811 | 433 | 0 | 0 |
| Saturday | 0 | 831 | 629 | 626 | 611 | 553 | 662 | 413 | 0 | 0 |
| Sunday | 0 | 944 | 654 | 632 | 516 | 516 | 622 | 348 | 0 | 0 |

## Saturday Availability Windows
*Based on 19 Saturdays observed (2026-03-28 to 2026-08-08):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 84% | ⚠️ Usually taken |
| 12pm | 84% | ⚠️ Usually taken |
| 1pm | 84% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 84% | ⚠️ Usually taken |
| 12pm | 84% | ⚠️ Usually taken |
| 1pm | 84% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 84% | ⚠️ Usually taken |
| 12pm | 84% | ⚠️ Usually taken |
| 1pm | 84% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 74% | ⚠️ Usually taken |
| 12pm | 68% | 🟡 Moderate demand |
| 1pm | 63% | 🟡 Moderate demand |
| 2pm | 37% | 🟡 Moderate demand |
| 3pm | 32% | 🟡 Moderate demand |
| 4pm | 74% | ⚠️ Usually taken |
| 5pm | 84% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 84% | ⚠️ Usually taken |
| 12pm | 84% | ⚠️ Usually taken |
| 1pm | 84% | ⚠️ Usually taken |
| 2pm | 84% | ⚠️ Usually taken |
| 3pm | 84% | ⚠️ Usually taken |
| 4pm | 84% | ⚠️ Usually taken |
| 5pm | 84% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 47% | 🟡 Moderate demand |
| 12pm | 16% | ✅ Often available |
| 1pm | 21% | ✅ Often available |
| 2pm | 21% | ✅ Often available |
| 3pm | 26% | ✅ Often available |
| 4pm | 32% | 🟡 Moderate demand |
| 5pm | 74% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 26.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 68% | 🟡 Moderate demand |
| 12pm | 53% | 🟡 Moderate demand |
| 1pm | 16% | ✅ Often available |
| 2pm | 32% | 🟡 Moderate demand |
| 3pm | 37% | 🟡 Moderate demand |
| 4pm | 47% | 🟡 Moderate demand |
| 5pm | 74% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 47% | 🟡 Moderate demand |
| 12pm | 47% | 🟡 Moderate demand |
| 1pm | 47% | 🟡 Moderate demand |
| 2pm | 32% | 🟡 Moderate demand |
| 3pm | 37% | 🟡 Moderate demand |
| 4pm | 53% | 🟡 Moderate demand |
| 5pm | 53% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 95% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 28,247 |
| redmond | 6,081 |
| sammamish | 3,151 |
| kingsgate | 247 |
| issaquah | 238 |
| woodinville | 207 |

## Data Quality Notes
- Total records: 38,171
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 33,348
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 87% fresh — grows toward 100% as initial batch ages out
