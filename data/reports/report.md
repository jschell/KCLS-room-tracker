# KCLS Room Monitor Report
*Generated: 2026-08-07 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 46,354 |
| Date range | 2026-03-22 to 2026-09-03 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (10%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 8,044 |
| Tuesday | 8,891 |
| Wednesday | 8,027 |
| Thursday | 3,359 |
| Friday | 7,518 |
| Saturday | 5,143 |
| Sunday | 5,372 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,827 |
| 11am | 6,072 |
| 12pm | 6,176 |
| 1pm | 6,187 |
| 2pm | 6,025 |
| 3pm | 6,040 |
| 4pm | 6,348 |
| 5pm | 4,077 |
| 6pm | 1,695 |
| 7pm | 907 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 34332 (30630 / 3702) |
| issaquah | 28.0 | 5.0 | 28.0 | 28.0 | 17.2% | 296 (264 / 32) |
| kingsgate | 28.0 | 5.0 | 28.0 | 28.0 | 21.8% | 308 (279 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 7335 (6483 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.0% | 3831 (3653 / 178) |
| woodinville | 28.0 | 1.0 | 28.0 | 28.0 | 24.2% | 252 (222 / 30) |

*46,354 bookings total — 41,531 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1045 | 758 | 875 | 1208 | 1178 | 1172 | 1204 | 604 | 0 | 0 |
| Tuesday | 0 | 910 | 1249 | 1129 | 1115 | 1112 | 1102 | 917 | 885 | 472 |
| Wednesday | 0 | 995 | 1123 | 906 | 919 | 955 | 1023 | 861 | 810 | 435 |
| Thursday | 580 | 313 | 383 | 440 | 434 | 453 | 495 | 261 | 0 | 0 |
| Friday | 1202 | 929 | 967 | 977 | 972 | 1004 | 960 | 507 | 0 | 0 |
| Saturday | 0 | 997 | 759 | 735 | 721 | 663 | 779 | 489 | 0 | 0 |
| Sunday | 0 | 1170 | 820 | 792 | 686 | 681 | 785 | 438 | 0 | 0 |

## Saturday Availability Windows
*Based on 22 Saturdays observed (2026-03-28 to 2026-08-29):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 86% | ⚠️ Usually taken |
| 12pm | 86% | ⚠️ Usually taken |
| 1pm | 86% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 77% | ⚠️ Usually taken |
| 12pm | 73% | ⚠️ Usually taken |
| 1pm | 64% | 🟡 Moderate demand |
| 2pm | 41% | 🟡 Moderate demand |
| 3pm | 36% | 🟡 Moderate demand |
| 4pm | 68% | 🟡 Moderate demand |
| 5pm | 82% | ⚠️ Usually taken |

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
| 11am | 59% | 🟡 Moderate demand |
| 12pm | 23% | ✅ Often available |
| 1pm | 23% | ✅ Often available |
| 2pm | 18% | ✅ Often available |
| 3pm | 27% | ✅ Often available |
| 4pm | 36% | 🟡 Moderate demand |
| 5pm | 82% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 68% | 🟡 Moderate demand |
| 12pm | 55% | 🟡 Moderate demand |
| 1pm | 18% | ✅ Often available |
| 2pm | 32% | 🟡 Moderate demand |
| 3pm | 36% | 🟡 Moderate demand |
| 4pm | 45% | 🟡 Moderate demand |
| 5pm | 73% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 36% | 🟡 Moderate demand |
| 3pm | 41% | 🟡 Moderate demand |
| 4pm | 59% | 🟡 Moderate demand |
| 5pm | 59% | 🟡 Moderate demand |

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
| bellevue | 34,332 |
| redmond | 7,335 |
| sammamish | 3,831 |
| kingsgate | 308 |
| issaquah | 296 |
| woodinville | 252 |

## Data Quality Notes
- Total records: 46,354
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 41,531
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 90% fresh — grows toward 100% as initial batch ages out
