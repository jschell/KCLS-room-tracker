# KCLS Room Monitor Report
*Generated: 2026-11-20 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 78,024 |
| Date range | 2026-03-22 to 2026-12-18 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (6%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 13,063 |
| Tuesday | 15,421 |
| Wednesday | 12,772 |
| Thursday | 5,556 |
| Friday | 13,165 |
| Saturday | 8,931 |
| Sunday | 9,116 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 5,701 |
| 11am | 10,289 |
| 12pm | 10,300 |
| 1pm | 10,331 |
| 2pm | 10,091 |
| 3pm | 10,019 |
| 4pm | 10,367 |
| 5pm | 6,717 |
| 6pm | 2,754 |
| 7pm | 1,455 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 57387 (53685 / 3702) |
| issaquah | 28.0 | 7.5 | 28.0 | 28.0 | 15.2% | 487 (455 / 32) |
| kingsgate | 28.0 | 9.0 | 28.0 | 28.0 | 17.9% | 504 (475 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 0.9% | 12843 (11991 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 1.7% | 6390 (6212 / 178) |
| woodinville | 28.0 | 6.0 | 28.0 | 28.0 | 19.4% | 413 (383 / 30) |

*78,024 bookings total — 73,201 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1688 | 1219 | 1416 | 1966 | 1922 | 1920 | 1957 | 975 | 0 | 0 |
| Tuesday | 602 | 1638 | 2059 | 1885 | 1894 | 1865 | 1751 | 1515 | 1449 | 763 |
| Wednesday | 423 | 1566 | 1724 | 1413 | 1436 | 1412 | 1496 | 1305 | 1305 | 692 |
| Thursday | 937 | 483 | 661 | 723 | 732 | 762 | 827 | 431 | 0 | 0 |
| Friday | 2051 | 1617 | 1690 | 1706 | 1711 | 1750 | 1724 | 916 | 0 | 0 |
| Saturday | 0 | 1811 | 1354 | 1267 | 1196 | 1113 | 1333 | 857 | 0 | 0 |
| Sunday | 0 | 1955 | 1396 | 1371 | 1200 | 1197 | 1279 | 718 | 0 | 0 |

## Saturday Availability Windows
*Based on 37 Saturdays observed (2026-03-28 to 2026-12-12):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 73% | ⚠️ Usually taken |
| 12pm | 68% | 🟡 Moderate demand |
| 1pm | 65% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 35% | 🟡 Moderate demand |
| 4pm | 76% | ⚠️ Usually taken |
| 5pm | 81% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 92% | ⚠️ Usually taken |
| 12pm | 92% | ⚠️ Usually taken |
| 1pm | 92% | ⚠️ Usually taken |
| 2pm | 92% | ⚠️ Usually taken |
| 3pm | 92% | ⚠️ Usually taken |
| 4pm | 92% | ⚠️ Usually taken |
| 5pm | 92% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 59% | 🟡 Moderate demand |
| 12pm | 27% | ✅ Often available |
| 1pm | 24% | ✅ Often available |
| 2pm | 24% | ✅ Often available |
| 3pm | 30% | ✅ Often available |
| 4pm | 41% | 🟡 Moderate demand |
| 5pm | 78% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 68% | 🟡 Moderate demand |
| 12pm | 57% | 🟡 Moderate demand |
| 1pm | 19% | ✅ Often available |
| 2pm | 41% | 🟡 Moderate demand |
| 3pm | 46% | 🟡 Moderate demand |
| 4pm | 54% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 62% | 🟡 Moderate demand |
| 12pm | 62% | 🟡 Moderate demand |
| 1pm | 51% | 🟡 Moderate demand |
| 2pm | 41% | 🟡 Moderate demand |
| 3pm | 41% | 🟡 Moderate demand |
| 4pm | 54% | 🟡 Moderate demand |
| 5pm | 57% | 🟡 Moderate demand |

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
| bellevue | 57,387 |
| redmond | 12,843 |
| sammamish | 6,390 |
| kingsgate | 504 |
| issaquah | 487 |
| woodinville | 413 |

## Data Quality Notes
- Total records: 78,024
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 73,201
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 94% fresh — grows toward 100% as initial batch ages out
