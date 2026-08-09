# KCLS Room Monitor Report
*Generated: 2026-08-09 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 47,435 |
| Date range | 2026-03-22 to 2026-09-06 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (10%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 8,045 |
| Tuesday | 8,891 |
| Wednesday | 8,027 |
| Thursday | 3,359 |
| Friday | 7,952 |
| Saturday | 5,460 |
| Sunday | 5,701 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,895 |
| 11am | 6,240 |
| 12pm | 6,322 |
| 1pm | 6,337 |
| 2pm | 6,172 |
| 3pm | 6,196 |
| 4pm | 6,509 |
| 5pm | 4,162 |
| 6pm | 1,695 |
| 7pm | 907 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 35112 (31410 / 3702) |
| issaquah | 28.0 | 5.2 | 28.0 | 28.0 | 17.2% | 302 (270 / 32) |
| kingsgate | 28.0 | 5.0 | 28.0 | 28.0 | 21.7% | 313 (284 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 7542 (6690 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.0% | 3912 (3734 / 178) |
| woodinville | 28.0 | 1.0 | 28.0 | 28.0 | 24.0% | 254 (224 / 30) |

*47,435 bookings total — 42,612 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1045 | 758 | 875 | 1209 | 1178 | 1172 | 1204 | 604 | 0 | 0 |
| Tuesday | 0 | 910 | 1249 | 1129 | 1115 | 1112 | 1102 | 917 | 885 | 472 |
| Wednesday | 0 | 995 | 1123 | 906 | 919 | 955 | 1023 | 861 | 810 | 435 |
| Thursday | 580 | 313 | 383 | 440 | 434 | 453 | 495 | 261 | 0 | 0 |
| Friday | 1270 | 985 | 1023 | 1035 | 1028 | 1060 | 1016 | 535 | 0 | 0 |
| Saturday | 0 | 1054 | 805 | 781 | 768 | 707 | 828 | 517 | 0 | 0 |
| Sunday | 0 | 1225 | 864 | 837 | 730 | 737 | 841 | 467 | 0 | 0 |

## Saturday Availability Windows
*Based on 23 Saturdays observed (2026-03-28 to 2026-09-05):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 87% | ⚠️ Usually taken |
| 12pm | 87% | ⚠️ Usually taken |
| 1pm | 87% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 87% | ⚠️ Usually taken |
| 12pm | 87% | ⚠️ Usually taken |
| 1pm | 87% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 87% | ⚠️ Usually taken |
| 12pm | 87% | ⚠️ Usually taken |
| 1pm | 87% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 74% | ⚠️ Usually taken |
| 12pm | 70% | 🟡 Moderate demand |
| 1pm | 61% | 🟡 Moderate demand |
| 2pm | 39% | 🟡 Moderate demand |
| 3pm | 35% | 🟡 Moderate demand |
| 4pm | 65% | 🟡 Moderate demand |
| 5pm | 78% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 87% | ⚠️ Usually taken |
| 12pm | 87% | ⚠️ Usually taken |
| 1pm | 87% | ⚠️ Usually taken |
| 2pm | 87% | ⚠️ Usually taken |
| 3pm | 87% | ⚠️ Usually taken |
| 4pm | 87% | ⚠️ Usually taken |
| 5pm | 87% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 57% | 🟡 Moderate demand |
| 12pm | 22% | ✅ Often available |
| 1pm | 22% | ✅ Often available |
| 2pm | 17% | ✅ Often available |
| 3pm | 30% | 🟡 Moderate demand |
| 4pm | 39% | 🟡 Moderate demand |
| 5pm | 83% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 70% | 🟡 Moderate demand |
| 12pm | 57% | 🟡 Moderate demand |
| 1pm | 17% | ✅ Often available |
| 2pm | 35% | 🟡 Moderate demand |
| 3pm | 39% | 🟡 Moderate demand |
| 4pm | 48% | 🟡 Moderate demand |
| 5pm | 74% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 52% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 52% | 🟡 Moderate demand |
| 2pm | 39% | 🟡 Moderate demand |
| 3pm | 43% | 🟡 Moderate demand |
| 4pm | 61% | 🟡 Moderate demand |
| 5pm | 61% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 96% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 35,112 |
| redmond | 7,542 |
| sammamish | 3,912 |
| kingsgate | 313 |
| issaquah | 302 |
| woodinville | 254 |

## Data Quality Notes
- Total records: 47,435
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 42,612
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 90% fresh — grows toward 100% as initial batch ages out
