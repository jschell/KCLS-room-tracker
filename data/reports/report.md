# KCLS Room Monitor Report
*Generated: 2026-07-02 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 35,078 |
| Date range | 2026-03-22 to 2026-07-30 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (14%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 6,158 |
| Tuesday | 6,762 |
| Wednesday | 6,351 |
| Thursday | 2,618 |
| Friday | 5,591 |
| Saturday | 3,650 |
| Sunday | 3,948 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,157 |
| 11am | 4,576 |
| 12pm | 4,706 |
| 1pm | 4,731 |
| 2pm | 4,521 |
| 3pm | 4,528 |
| 4pm | 4,802 |
| 5pm | 3,086 |
| 6pm | 1,287 |
| 7pm | 684 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 25947 (22245 / 3702) |
| issaquah | 28.0 | 7.2 | 28.0 | 28.0 | 15.9% | 214 (182 / 32) |
| kingsgate | 28.0 | 7.8 | 28.0 | 28.0 | 19.2% | 224 (195 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.3% | 5583 (4731 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 2920 (2742 / 178) |
| woodinville | 26.0 | 3.2 | 28.0 | 28.0 | 22.1% | 190 (160 / 30) |

*35,078 bookings total — 30,255 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 807 | 583 | 676 | 926 | 898 | 887 | 918 | 463 | 0 | 0 |
| Tuesday | 0 | 700 | 963 | 870 | 853 | 843 | 838 | 689 | 657 | 349 |
| Wednesday | 0 | 780 | 893 | 725 | 725 | 759 | 829 | 675 | 630 | 335 |
| Thursday | 446 | 243 | 302 | 352 | 332 | 348 | 391 | 204 | 0 | 0 |
| Friday | 904 | 694 | 729 | 734 | 719 | 739 | 698 | 374 | 0 | 0 |
| Saturday | 0 | 701 | 523 | 528 | 512 | 470 | 557 | 359 | 0 | 0 |
| Sunday | 0 | 875 | 620 | 596 | 482 | 482 | 571 | 322 | 0 | 0 |

## Saturday Availability Windows
*Based on 17 Saturdays observed (2026-03-28 to 2026-07-25):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 71% | ⚠️ Usually taken |
| 12pm | 65% | 🟡 Moderate demand |
| 1pm | 59% | 🟡 Moderate demand |
| 2pm | 35% | 🟡 Moderate demand |
| 3pm | 29% | ✅ Often available |
| 4pm | 71% | ⚠️ Usually taken |
| 5pm | 82% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 82% | ⚠️ Usually taken |
| 12pm | 82% | ⚠️ Usually taken |
| 1pm | 82% | ⚠️ Usually taken |
| 2pm | 82% | ⚠️ Usually taken |
| 3pm | 82% | ⚠️ Usually taken |
| 4pm | 82% | ⚠️ Usually taken |
| 5pm | 82% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 53% | 🟡 Moderate demand |
| 12pm | 18% | ✅ Often available |
| 1pm | 18% | ✅ Often available |
| 2pm | 18% | ✅ Often available |
| 3pm | 24% | ✅ Often available |
| 4pm | 29% | ✅ Often available |
| 5pm | 76% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 26.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 65% | 🟡 Moderate demand |
| 12pm | 47% | 🟡 Moderate demand |
| 1pm | 18% | ✅ Often available |
| 2pm | 29% | ✅ Often available |
| 3pm | 35% | 🟡 Moderate demand |
| 4pm | 41% | 🟡 Moderate demand |
| 5pm | 71% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 41% | 🟡 Moderate demand |
| 12pm | 41% | 🟡 Moderate demand |
| 1pm | 47% | 🟡 Moderate demand |
| 2pm | 24% | ✅ Often available |
| 3pm | 29% | ✅ Often available |
| 4pm | 47% | 🟡 Moderate demand |
| 5pm | 47% | 🟡 Moderate demand |

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
| bellevue | 25,947 |
| redmond | 5,583 |
| sammamish | 2,920 |
| kingsgate | 224 |
| issaquah | 214 |
| woodinville | 190 |

## Data Quality Notes
- Total records: 35,078
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 30,255
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 86% fresh — grows toward 100% as initial batch ages out
