# KCLS Room Monitor Report
*Generated: 2026-09-11 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 57,035 |
| Date range | 2026-03-22 to 2026-10-08 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (8%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 9,519 |
| Tuesday | 10,861 |
| Wednesday | 9,758 |
| Thursday | 4,159 |
| Friday | 9,506 |
| Saturday | 6,524 |
| Sunday | 6,708 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 3,448 |
| 11am | 7,503 |
| 12pm | 7,599 |
| 1pm | 7,619 |
| 2pm | 7,443 |
| 3pm | 7,497 |
| 4pm | 7,772 |
| 5pm | 4,994 |
| 6pm | 2,059 |
| 7pm | 1,101 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 42317 (38615 / 3702) |
| issaquah | 28.0 | 5.0 | 28.0 | 28.0 | 17.9% | 379 (347 / 32) |
| kingsgate | 28.0 | 6.0 | 28.0 | 28.0 | 21.0% | 377 (348 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 9027 (8175 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 4623 (4445 / 178) |
| woodinville | 28.0 | 1.0 | 28.0 | 28.0 | 22.8% | 312 (282 / 30) |

*57,035 bookings total — 52,212 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1229 | 890 | 1027 | 1432 | 1396 | 1397 | 1431 | 717 | 0 | 0 |
| Tuesday | 0 | 1130 | 1535 | 1386 | 1375 | 1369 | 1305 | 1119 | 1071 | 571 |
| Wednesday | 0 | 1210 | 1353 | 1105 | 1125 | 1165 | 1237 | 1045 | 988 | 530 |
| Thursday | 711 | 380 | 484 | 538 | 539 | 567 | 615 | 325 | 0 | 0 |
| Friday | 1508 | 1175 | 1218 | 1239 | 1226 | 1272 | 1222 | 646 | 0 | 0 |
| Saturday | 0 | 1269 | 967 | 923 | 909 | 852 | 995 | 609 | 0 | 0 |
| Sunday | 0 | 1449 | 1015 | 996 | 873 | 875 | 967 | 533 | 0 | 0 |

## Saturday Availability Windows
*Based on 27 Saturdays observed (2026-03-28 to 2026-10-03):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 89% | ⚠️ Usually taken |
| 12pm | 89% | ⚠️ Usually taken |
| 1pm | 89% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 89% | ⚠️ Usually taken |
| 12pm | 89% | ⚠️ Usually taken |
| 1pm | 89% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 89% | ⚠️ Usually taken |
| 12pm | 89% | ⚠️ Usually taken |
| 1pm | 89% | ⚠️ Usually taken |
| 2pm | 96% | ⚠️ Usually taken |
| 3pm | 93% | ⚠️ Usually taken |
| 4pm | 96% | ⚠️ Usually taken |
| 5pm | 96% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 78% | ⚠️ Usually taken |
| 12pm | 74% | ⚠️ Usually taken |
| 1pm | 70% | ⚠️ Usually taken |
| 2pm | 48% | 🟡 Moderate demand |
| 3pm | 44% | 🟡 Moderate demand |
| 4pm | 81% | ⚠️ Usually taken |
| 5pm | 89% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 89% | ⚠️ Usually taken |
| 12pm | 89% | ⚠️ Usually taken |
| 1pm | 89% | ⚠️ Usually taken |
| 2pm | 89% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 89% | ⚠️ Usually taken |
| 5pm | 89% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 63% | 🟡 Moderate demand |
| 12pm | 22% | ✅ Often available |
| 1pm | 22% | ✅ Often available |
| 2pm | 22% | ✅ Often available |
| 3pm | 30% | ✅ Often available |
| 4pm | 44% | 🟡 Moderate demand |
| 5pm | 85% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 59% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 19% | ✅ Often available |
| 2pm | 41% | 🟡 Moderate demand |
| 3pm | 44% | 🟡 Moderate demand |
| 4pm | 52% | 🟡 Moderate demand |
| 5pm | 78% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 59% | 🟡 Moderate demand |
| 12pm | 59% | 🟡 Moderate demand |
| 1pm | 52% | 🟡 Moderate demand |
| 2pm | 41% | 🟡 Moderate demand |
| 3pm | 41% | 🟡 Moderate demand |
| 4pm | 59% | 🟡 Moderate demand |
| 5pm | 63% | 🟡 Moderate demand |

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
| bellevue | 42,317 |
| redmond | 9,027 |
| sammamish | 4,623 |
| issaquah | 379 |
| kingsgate | 377 |
| woodinville | 312 |

## Data Quality Notes
- Total records: 57,035
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 52,212
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 92% fresh — grows toward 100% as initial batch ages out
