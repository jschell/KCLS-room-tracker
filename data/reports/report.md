# KCLS Room Monitor Report
*Generated: 2026-10-20 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 68,487 |
| Date range | 2026-03-22 to 2026-11-16 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (7%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 11,621 |
| Tuesday | 13,045 |
| Wednesday | 11,159 |
| Thursday | 4,980 |
| Friday | 11,690 |
| Saturday | 7,982 |
| Sunday | 8,010 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 4,601 |
| 11am | 9,061 |
| 12pm | 9,119 |
| 1pm | 9,136 |
| 2pm | 8,899 |
| 3pm | 8,910 |
| 4pm | 9,212 |
| 5pm | 5,911 |
| 6pm | 2,376 |
| 7pm | 1,262 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.0% | 50512 (46810 / 3702) |
| issaquah | 28.0 | 7.0 | 28.0 | 28.0 | 16.4% | 438 (406 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 18.8% | 451 (422 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.1% | 11091 (10239 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 1.9% | 5625 (5447 / 178) |
| woodinville | 28.0 | 4.2 | 28.0 | 28.0 | 21.1% | 370 (340 / 30) |

*68,487 bookings total — 63,664 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 1501 | 1085 | 1259 | 1748 | 1707 | 1714 | 1740 | 867 | 0 | 0 |
| Tuesday | 260 | 1373 | 1801 | 1631 | 1641 | 1621 | 1521 | 1299 | 1240 | 658 |
| Wednesday | 194 | 1400 | 1545 | 1236 | 1257 | 1269 | 1357 | 1161 | 1136 | 604 |
| Thursday | 826 | 433 | 596 | 653 | 657 | 688 | 740 | 387 | 0 | 0 |
| Friday | 1820 | 1433 | 1502 | 1523 | 1514 | 1564 | 1526 | 808 | 0 | 0 |
| Saturday | 0 | 1600 | 1197 | 1144 | 1080 | 1009 | 1195 | 757 | 0 | 0 |
| Sunday | 0 | 1737 | 1219 | 1201 | 1043 | 1045 | 1133 | 632 | 0 | 0 |

## Saturday Availability Windows
*Based on 33 Saturdays observed (2026-03-28 to 2026-11-14):*

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
| 12pm | 73% | ⚠️ Usually taken |
| 1pm | 70% | 🟡 Moderate demand |
| 2pm | 42% | 🟡 Moderate demand |
| 3pm | 39% | 🟡 Moderate demand |
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
| 11am | 58% | 🟡 Moderate demand |
| 12pm | 24% | ✅ Often available |
| 1pm | 24% | ✅ Often available |
| 2pm | 24% | ✅ Often available |
| 3pm | 30% | 🟡 Moderate demand |
| 4pm | 42% | 🟡 Moderate demand |
| 5pm | 82% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 28.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 64% | 🟡 Moderate demand |
| 12pm | 52% | 🟡 Moderate demand |
| 1pm | 18% | ✅ Often available |
| 2pm | 39% | 🟡 Moderate demand |
| 3pm | 45% | 🟡 Moderate demand |
| 4pm | 52% | 🟡 Moderate demand |
| 5pm | 79% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 61% | 🟡 Moderate demand |
| 12pm | 61% | 🟡 Moderate demand |
| 1pm | 48% | 🟡 Moderate demand |
| 2pm | 36% | 🟡 Moderate demand |
| 3pm | 36% | 🟡 Moderate demand |
| 4pm | 58% | 🟡 Moderate demand |
| 5pm | 61% | 🟡 Moderate demand |

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
| bellevue | 50,512 |
| redmond | 11,091 |
| sammamish | 5,625 |
| kingsgate | 451 |
| issaquah | 438 |
| woodinville | 370 |

## Data Quality Notes
- Total records: 68,487
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 63,664
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 93% fresh — grows toward 100% as initial batch ages out
