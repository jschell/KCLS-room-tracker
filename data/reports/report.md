# KCLS Room Monitor Report
*Generated: 2026-09-26 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 61,762 |
| Date range | 2026-03-22 to 2026-10-24 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (8%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 10,229 |
| Tuesday | 11,673 |
| Wednesday | 10,390 |
| Thursday | 4,483 |
| Friday | 10,627 |
| Saturday | 7,276 |
| Sunday | 7,084 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 3,865 |
| 11am | 8,145 |
| 12pm | 8,261 |
| 1pm | 8,267 |
| 2pm | 8,071 |
| 3pm | 8,091 |
| 4pm | 8,365 |
| 5pm | 5,363 |
| 6pm | 2,175 |
| 7pm | 1,159 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 45727 (42025 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.5% | 405 (373 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 20.6% | 407 (378 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.0% | 9831 (8979 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.0% | 5052 (4874 / 178) |
| woodinville | 28.0 | 1.8 | 28.0 | 28.0 | 22.4% | 340 (310 / 30) |

*61,762 bookings total — 56,939 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1321 | 956 | 1105 | 1538 | 1501 | 1506 | 1533 | 769 | 0 | 0 |
| Tuesday | 64 | 1227 | 1651 | 1493 | 1487 | 1475 | 1387 | 1175 | 1119 | 595 |
| Wednesday | 63 | 1292 | 1443 | 1169 | 1188 | 1212 | 1299 | 1104 | 1056 | 564 |
| Thursday | 758 | 403 | 529 | 583 | 585 | 615 | 662 | 348 | 0 | 0 |
| Friday | 1659 | 1297 | 1364 | 1395 | 1384 | 1427 | 1376 | 725 | 0 | 0 |
| Saturday | 0 | 1431 | 1085 | 1025 | 1011 | 945 | 1098 | 681 | 0 | 0 |
| Sunday | 0 | 1539 | 1084 | 1064 | 915 | 911 | 1010 | 561 | 0 | 0 |

## Saturday Availability Windows
*Based on 30 Saturdays observed (2026-03-28 to 2026-10-24):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 90% | ⚠️ Usually taken |
| 12pm | 90% | ⚠️ Usually taken |
| 1pm | 90% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 90% | ⚠️ Usually taken |
| 12pm | 90% | ⚠️ Usually taken |
| 1pm | 90% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 90% | ⚠️ Usually taken |
| 12pm | 90% | ⚠️ Usually taken |
| 1pm | 90% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 77% | ⚠️ Usually taken |
| 12pm | 73% | ⚠️ Usually taken |
| 1pm | 70% | 🟡 Moderate demand |
| 2pm | 43% | 🟡 Moderate demand |
| 3pm | 40% | 🟡 Moderate demand |
| 4pm | 80% | ⚠️ Usually taken |
| 5pm | 87% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 90% | ⚠️ Usually taken |
| 12pm | 90% | ⚠️ Usually taken |
| 1pm | 90% | ⚠️ Usually taken |
| 2pm | 90% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 90% | ⚠️ Usually taken |
| 5pm | 90% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 57% | 🟡 Moderate demand |
| 12pm | 20% | ✅ Often available |
| 1pm | 20% | ✅ Often available |
| 2pm | 20% | ✅ Often available |
| 3pm | 27% | ✅ Often available |
| 4pm | 40% | 🟡 Moderate demand |
| 5pm | 83% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 17% | ✅ Often available |
| 2pm | 40% | 🟡 Moderate demand |
| 3pm | 47% | 🟡 Moderate demand |
| 4pm | 53% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 60% | 🟡 Moderate demand |
| 12pm | 60% | 🟡 Moderate demand |
| 1pm | 47% | 🟡 Moderate demand |
| 2pm | 37% | 🟡 Moderate demand |
| 3pm | 37% | 🟡 Moderate demand |
| 4pm | 57% | 🟡 Moderate demand |
| 5pm | 60% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 28.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 97% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 28.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 45,727 |
| redmond | 9,831 |
| sammamish | 5,052 |
| kingsgate | 407 |
| issaquah | 405 |
| woodinville | 340 |

## Data Quality Notes
- Total records: 61,762
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 56,939
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 92% fresh — grows toward 100% as initial batch ages out
