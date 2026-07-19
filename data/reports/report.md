# KCLS Room Monitor Report
*Generated: 2026-07-19 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 40,604 |
| Date range | 2026-03-22 to 2026-08-16 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (12%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 6,928 |
| Tuesday | 7,608 |
| Wednesday | 6,955 |
| Thursday | 2,938 |
| Friday | 6,765 |
| Saturday | 4,650 |
| Sunday | 4,760 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,474 |
| 11am | 5,354 |
| 12pm | 5,425 |
| 1pm | 5,430 |
| 2pm | 5,262 |
| 3pm | 5,292 |
| 4pm | 5,593 |
| 5pm | 3,570 |
| 6pm | 1,434 |
| 7pm | 770 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 29952 (26250 / 3702) |
| issaquah | 28.0 | 6.0 | 28.0 | 28.0 | 17.3% | 255 (223 / 32) |
| kingsgate | 28.0 | 7.0 | 28.0 | 28.0 | 20.4% | 265 (236 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.2% | 6549 (5697 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.1% | 3363 (3185 / 178) |
| woodinville | 27.0 | 1.0 | 28.0 | 28.0 | 22.7% | 220 (190 / 30) |

*40,604 bookings total — 35,781 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 904 | 656 | 758 | 1043 | 1010 | 1002 | 1034 | 521 | 0 | 0 |
| Tuesday | 0 | 785 | 1078 | 975 | 964 | 959 | 945 | 772 | 736 | 394 |
| Wednesday | 0 | 870 | 983 | 783 | 787 | 821 | 889 | 748 | 698 | 376 |
| Thursday | 494 | 267 | 334 | 388 | 379 | 400 | 445 | 231 | 0 | 0 |
| Friday | 1076 | 828 | 863 | 875 | 881 | 914 | 867 | 461 | 0 | 0 |
| Saturday | 0 | 895 | 679 | 666 | 651 | 603 | 714 | 442 | 0 | 0 |
| Sunday | 0 | 1053 | 730 | 700 | 590 | 593 | 699 | 395 | 0 | 0 |

## Saturday Availability Windows
*Based on 20 Saturdays observed (2026-03-28 to 2026-08-15):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 95% | ⚠️ Usually taken |
| 3pm | 90% | ⚠️ Usually taken |
| 4pm | 95% | ⚠️ Usually taken |
| 5pm | 95% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 75% | ⚠️ Usually taken |
| 12pm | 70% | 🟡 Moderate demand |
| 1pm | 65% | 🟡 Moderate demand |
| 2pm | 35% | 🟡 Moderate demand |
| 3pm | 30% | 🟡 Moderate demand |
| 4pm | 70% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 85% | ⚠️ Usually taken |
| 12pm | 85% | ⚠️ Usually taken |
| 1pm | 85% | ⚠️ Usually taken |
| 2pm | 85% | ⚠️ Usually taken |
| 3pm | 85% | ⚠️ Usually taken |
| 4pm | 85% | ⚠️ Usually taken |
| 5pm | 85% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 55% | 🟡 Moderate demand |
| 12pm | 20% | ✅ Often available |
| 1pm | 25% | ✅ Often available |
| 2pm | 20% | ✅ Often available |
| 3pm | 30% | 🟡 Moderate demand |
| 4pm | 40% | 🟡 Moderate demand |
| 5pm | 80% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 27.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 70% | 🟡 Moderate demand |
| 12pm | 55% | 🟡 Moderate demand |
| 1pm | 15% | ✅ Often available |
| 2pm | 30% | 🟡 Moderate demand |
| 3pm | 35% | 🟡 Moderate demand |
| 4pm | 45% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 35% | 🟡 Moderate demand |
| 3pm | 40% | 🟡 Moderate demand |
| 4pm | 55% | 🟡 Moderate demand |
| 5pm | 55% | 🟡 Moderate demand |

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
| bellevue | 29,952 |
| redmond | 6,549 |
| sammamish | 3,363 |
| kingsgate | 265 |
| issaquah | 255 |
| woodinville | 220 |

## Data Quality Notes
- Total records: 40,604
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 35,781
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 88% fresh — grows toward 100% as initial batch ages out
