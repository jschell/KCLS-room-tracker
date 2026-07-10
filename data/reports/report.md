# KCLS Room Monitor Report
*Generated: 2026-07-10 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 37,836 |
| Date range | 2026-03-22 to 2026-08-07 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (13%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 6,544 |
| Tuesday | 7,200 |
| Wednesday | 6,761 |
| Thursday | 2,758 |
| Friday | 6,348 |
| Saturday | 3,996 |
| Sunday | 4,229 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,337 |
| 11am | 4,934 |
| 12pm | 5,049 |
| 1pm | 5,076 |
| 2pm | 4,879 |
| 3pm | 4,902 |
| 4pm | 5,199 |
| 5pm | 3,341 |
| 6pm | 1,380 |
| 7pm | 739 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 27982 (24280 / 3702) |
| issaquah | 28.0 | 6.5 | 28.0 | 28.0 | 17.0% | 235 (203 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 19.6% | 245 (216 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.2% | 6042 (5190 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 3128 (2950 / 178) |
| woodinville | 26.5 | 2.8 | 28.0 | 28.0 | 22.5% | 204 (174 / 30) |

*37,836 bookings total — 33,013 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 856 | 620 | 717 | 984 | 954 | 943 | 978 | 492 | 0 | 0 |
| Tuesday | 0 | 745 | 1025 | 922 | 905 | 900 | 891 | 736 | 702 | 374 |
| Wednesday | 0 | 825 | 947 | 771 | 771 | 804 | 873 | 727 | 678 | 365 |
| Thursday | 468 | 253 | 315 | 367 | 352 | 371 | 415 | 217 | 0 | 0 |
| Friday | 1013 | 778 | 812 | 824 | 822 | 856 | 810 | 433 | 0 | 0 |
| Saturday | 0 | 769 | 579 | 576 | 559 | 512 | 613 | 388 | 0 | 0 |
| Sunday | 0 | 944 | 654 | 632 | 516 | 516 | 619 | 348 | 0 | 0 |

## Saturday Availability Windows
*Based on 18 Saturdays observed (2026-03-28 to 2026-08-01):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 72% | ⚠️ Usually taken |
| 12pm | 67% | 🟡 Moderate demand |
| 1pm | 61% | 🟡 Moderate demand |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 28% | ✅ Often available |
| 4pm | 72% | ⚠️ Usually taken |
| 5pm | 83% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 83% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 83% | ⚠️ Usually taken |
| 5pm | 83% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 17% | ✅ Often available |
| 1pm | 22% | ✅ Often available |
| 2pm | 22% | ✅ Often available |
| 3pm | 28% | ✅ Often available |
| 4pm | 33% | 🟡 Moderate demand |
| 5pm | 78% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 26.5 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 17% | ✅ Often available |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 39% | 🟡 Moderate demand |
| 4pm | 44% | 🟡 Moderate demand |
| 5pm | 72% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 44% | 🟡 Moderate demand |
| 12pm | 44% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 28% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 50% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 27,982 |
| redmond | 6,042 |
| sammamish | 3,128 |
| kingsgate | 245 |
| issaquah | 235 |
| woodinville | 204 |

## Data Quality Notes
- Total records: 37,836
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 33,013
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 87% fresh — grows toward 100% as initial batch ages out
