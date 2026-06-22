# KCLS Room Monitor Report
*Generated: 2026-06-22 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 31,751 |
| Date range | 2026-03-22 to 2026-07-20 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (15%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 5,773 |
| Tuesday | 5,827 |
| Wednesday | 5,616 |
| Thursday | 2,232 |
| Friday | 5,241 |
| Saturday | 3,384 |
| Sunday | 3,678 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 1,993 |
| 11am | 4,154 |
| 12pm | 4,242 |
| 1pm | 4,264 |
| 2pm | 4,113 |
| 3pm | 4,118 |
| 4pm | 4,382 |
| 5pm | 2,785 |
| 6pm | 1,110 |
| 7pm | 590 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 23477 (19775 / 3702) |
| issaquah | 28.0 | 8.0 | 28.0 | 28.0 | 14.9% | 188 (156 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 18.2% | 203 (174 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 0.7% | 5082 (4230 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.2% | 2628 (2450 / 178) |
| woodinville | 25.0 | 3.0 | 28.0 | 28.0 | 22.0% | 173 (143 / 30) |

*31,751 bookings total — 26,928 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 758 | 547 | 633 | 869 | 838 | 831 | 862 | 435 | 0 | 0 |
| Tuesday | 0 | 610 | 838 | 751 | 741 | 730 | 724 | 586 | 554 | 293 |
| Wednesday | 0 | 690 | 793 | 637 | 645 | 670 | 731 | 597 | 556 | 297 |
| Thursday | 385 | 188 | 241 | 286 | 292 | 307 | 349 | 184 | 0 | 0 |
| Friday | 850 | 650 | 684 | 685 | 672 | 694 | 654 | 352 | 0 | 0 |
| Saturday | 0 | 652 | 483 | 489 | 476 | 434 | 521 | 329 | 0 | 0 |
| Sunday | 0 | 817 | 570 | 547 | 449 | 452 | 541 | 302 | 0 | 0 |

## Saturday Availability Windows
*Based on 16 Saturdays observed (2026-03-28 to 2026-07-18):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 94% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 69% | 🟡 Moderate demand |
| 12pm | 62% | 🟡 Moderate demand |
| 1pm | 56% | 🟡 Moderate demand |
| 2pm | 38% | 🟡 Moderate demand |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 69% | 🟡 Moderate demand |
| 5pm | 81% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 88% | ⚠️ Usually taken |
| 12pm | 88% | ⚠️ Usually taken |
| 1pm | 88% | ⚠️ Usually taken |
| 2pm | 88% | ⚠️ Usually taken |
| 3pm | 88% | ⚠️ Usually taken |
| 4pm | 88% | ⚠️ Usually taken |
| 5pm | 88% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 19% | ✅ Often available |
| 1pm | 19% | ✅ Often available |
| 2pm | 19% | ✅ Often available |
| 3pm | 25% | ✅ Often available |
| 4pm | 31% | 🟡 Moderate demand |
| 5pm | 75% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 25.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 62% | 🟡 Moderate demand |
| 12pm | 44% | 🟡 Moderate demand |
| 1pm | 12% | ✅ Often available |
| 2pm | 25% | ✅ Often available |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 38% | 🟡 Moderate demand |
| 5pm | 69% | 🟡 Moderate demand |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 38% | 🟡 Moderate demand |
| 12pm | 38% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 25% | ✅ Often available |
| 3pm | 31% | 🟡 Moderate demand |
| 4pm | 44% | 🟡 Moderate demand |
| 5pm | 44% | 🟡 Moderate demand |

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
| bellevue | 23,477 |
| redmond | 5,082 |
| sammamish | 2,628 |
| kingsgate | 203 |
| issaquah | 188 |
| woodinville | 173 |

## Data Quality Notes
- Total records: 31,751
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 26,928
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 85% fresh — grows toward 100% as initial batch ages out
