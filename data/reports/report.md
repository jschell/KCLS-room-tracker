# KCLS Room Monitor Report
*Generated: 2026-07-29 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 43,870 |
| Date range | 2026-03-22 to 2026-08-26 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (11%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 7,663 |
| Tuesday | 8,425 |
| Wednesday | 7,655 |
| Thursday | 3,038 |
| Friday | 7,120 |
| Saturday | 4,907 |
| Sunday | 5,062 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,649 |
| 11am | 5,746 |
| 12pm | 5,837 |
| 1pm | 5,845 |
| 2pm | 5,692 |
| 3pm | 5,727 |
| 4pm | 6,035 |
| 5pm | 3,872 |
| 6pm | 1,605 |
| 7pm | 862 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 32552 (28850 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.5% | 275 (243 / 32) |
| kingsgate | 28.0 | 5.0 | 28.0 | 28.0 | 21.3% | 291 (262 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.2% | 6918 (6066 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 3596 (3418 / 178) |
| woodinville | 27.5 | 1.0 | 28.0 | 28.0 | 23.5% | 238 (208 / 30) |

*43,870 bookings total — 39,047 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 996 | 722 | 833 | 1152 | 1122 | 1116 | 1146 | 576 | 0 | 0 |
| Tuesday | 0 | 865 | 1185 | 1073 | 1058 | 1056 | 1046 | 865 | 830 | 447 |
| Wednesday | 0 | 950 | 1071 | 861 | 874 | 908 | 977 | 824 | 775 | 415 |
| Thursday | 520 | 277 | 341 | 397 | 391 | 415 | 459 | 238 | 0 | 0 |
| Friday | 1133 | 872 | 909 | 920 | 928 | 958 | 916 | 484 | 0 | 0 |
| Saturday | 0 | 951 | 724 | 701 | 685 | 633 | 746 | 467 | 0 | 0 |
| Sunday | 0 | 1109 | 774 | 741 | 634 | 641 | 745 | 418 | 0 | 0 |

## Saturday Availability Windows
*Based on 21 Saturdays observed (2026-03-28 to 2026-08-22):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 76% | ⚠️ Usually taken |
| 12pm | 71% | ⚠️ Usually taken |
| 1pm | 62% | 🟡 Moderate demand |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 29% | ✅ Often available |
| 4pm | 67% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 86% | ⚠️ Usually taken |
| 3pm | 86% | ⚠️ Usually taken |
| 4pm | 86% | ⚠️ Usually taken |
| 5pm | 86% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 57% | 🟡 Moderate demand |
| 12pm | 19% | ✅ Often available |
| 1pm | 24% | ✅ Often available |
| 2pm | 19% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 38% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 27.5 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 14% | ✅ Often available |
| 2pm | 29% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 43% | 🟡 Moderate demand |
| 5pm | 71% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 52% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 52% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 43% | 🟡 Moderate demand |
| 4pm | 57% | 🟡 Moderate demand |
| 5pm | 57% | 🟡 Moderate demand |

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
| bellevue | 32,552 |
| redmond | 6,918 |
| sammamish | 3,596 |
| kingsgate | 291 |
| issaquah | 275 |
| woodinville | 238 |

## Data Quality Notes
- Total records: 43,870
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 39,047
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 89% fresh — grows toward 100% as initial batch ages out
