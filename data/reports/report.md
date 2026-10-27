# KCLS Room Monitor Report
*Generated: 2026-10-27 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 70,891 |
| Date range | 2026-03-22 to 2026-11-24 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (7%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 12,001 |
| Tuesday | 14,056 |
| Wednesday | 11,208 |
| Thursday | 5,119 |
| Friday | 12,019 |
| Saturday | 8,220 |
| Sunday | 8,268 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 4,870 |
| 11am | 9,352 |
| 12pm | 9,405 |
| 1pm | 9,429 |
| 2pm | 9,195 |
| 3pm | 9,219 |
| 4pm | 9,511 |
| 5pm | 6,133 |
| 6pm | 2,466 |
| 7pm | 1,311 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 52187 (48485 / 3702) |
| issaquah | 28.0 | 7.0 | 28.0 | 28.0 | 16.3% | 449 (417 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 18.7% | 466 (437 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.0% | 11532 (10680 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 1.8% | 5873 (5695 / 178) |
| woodinville | 28.0 | 4.8 | 28.0 | 28.0 | 20.6% | 384 (354 / 30) |

*70,891 bookings total — 66,068 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1550 | 1121 | 1302 | 1804 | 1763 | 1770 | 1796 | 895 | 0 | 0 |
| Tuesday | 398 | 1485 | 1913 | 1743 | 1749 | 1727 | 1619 | 1394 | 1326 | 702 |
| Wednesday | 205 | 1405 | 1551 | 1239 | 1258 | 1274 | 1361 | 1166 | 1140 | 609 |
| Thursday | 851 | 442 | 611 | 674 | 679 | 709 | 757 | 396 | 0 | 0 |
| Friday | 1866 | 1467 | 1540 | 1564 | 1561 | 1613 | 1572 | 836 | 0 | 0 |
| Saturday | 0 | 1647 | 1231 | 1169 | 1109 | 1041 | 1233 | 790 | 0 | 0 |
| Sunday | 0 | 1785 | 1257 | 1236 | 1076 | 1085 | 1173 | 656 | 0 | 0 |

## Saturday Availability Windows
*Based on 34 Saturdays observed (2026-03-28 to 2026-11-21):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 91% | ⚠️ Usually taken |
| 12pm | 91% | ⚠️ Usually taken |
| 1pm | 91% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 91% | ⚠️ Usually taken |
| 12pm | 91% | ⚠️ Usually taken |
| 1pm | 91% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 91% | ⚠️ Usually taken |
| 12pm | 91% | ⚠️ Usually taken |
| 1pm | 91% | ⚠️ Usually taken |
| 2pm | 97% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 97% | ⚠️ Usually taken |
| 5pm | 97% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 79% | ⚠️ Usually taken |
| 12pm | 74% | ⚠️ Usually taken |
| 1pm | 71% | ⚠️ Usually taken |
| 2pm | 41% | 🟡 Moderate demand |
| 3pm | 38% | 🟡 Moderate demand |
| 4pm | 82% | ⚠️ Usually taken |
| 5pm | 88% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 91% | ⚠️ Usually taken |
| 12pm | 91% | ⚠️ Usually taken |
| 1pm | 91% | ⚠️ Usually taken |
| 2pm | 91% | ⚠️ Usually taken |
| 3pm | 91% | ⚠️ Usually taken |
| 4pm | 91% | ⚠️ Usually taken |
| 5pm | 91% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 59% | 🟡 Moderate demand |
| 12pm | 26% | ✅ Often available |
| 1pm | 24% | ✅ Often available |
| 2pm | 24% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 44% | 🟡 Moderate demand |
| 5pm | 82% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 65% | 🟡 Moderate demand |
| 12pm | 53% | 🟡 Moderate demand |
| 1pm | 18% | ✅ Often available |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 44% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 79% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 62% | 🟡 Moderate demand |
| 12pm | 62% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 38% | 🟡 Moderate demand |
| 4pm | 59% | 🟡 Moderate demand |
| 5pm | 62% | 🟡 Moderate demand |

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
| bellevue | 52,187 |
| redmond | 11,532 |
| sammamish | 5,873 |
| kingsgate | 466 |
| issaquah | 449 |
| woodinville | 384 |

## Data Quality Notes
- Total records: 70,891
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 66,068
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 93% fresh — grows toward 100% as initial batch ages out
