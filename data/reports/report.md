# KCLS Room Monitor Report
*Generated: 2026-07-05 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 36,046 |
| Date range | 2026-03-22 to 2026-08-02 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (13%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 6,159 |
| Tuesday | 6,762 |
| Wednesday | 6,352 |
| Thursday | 2,619 |
| Friday | 5,945 |
| Saturday | 3,994 |
| Sunday | 4,215 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 2,203 |
| 11am | 4,747 |
| 12pm | 4,831 |
| 1pm | 4,853 |
| 2pm | 4,648 |
| 3pm | 4,662 |
| 4pm | 4,962 |
| 5pm | 3,168 |
| 6pm | 1,288 |
| 7pm | 684 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 28.0 | 28.0 | 28.0 | 28.0 | 0.1% | 26682 (22980 / 3702) |
| issaquah | 28.0 | 7.0 | 28.0 | 28.0 | 16.2% | 222 (190 / 32) |
| kingsgate | 28.0 | 8.0 | 28.0 | 28.0 | 19.0% | 231 (202 / 29) |
| redmond | 28.0 | 28.0 | 28.0 | 28.0 | 1.3% | 5727 (4875 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 2.3% | 2991 (2813 / 178) |
| woodinville | 26.0 | 3.0 | 28.0 | 28.0 | 21.8% | 193 (163 / 30) |

*36,046 bookings total — 31,223 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 807 | 584 | 676 | 926 | 898 | 887 | 918 | 463 | 0 | 0 |
| Tuesday | 0 | 700 | 963 | 870 | 853 | 843 | 838 | 689 | 657 | 349 |
| Wednesday | 0 | 780 | 893 | 725 | 725 | 759 | 829 | 675 | 631 | 335 |
| Thursday | 446 | 243 | 302 | 352 | 332 | 348 | 392 | 204 | 0 | 0 |
| Friday | 950 | 728 | 764 | 779 | 769 | 798 | 754 | 403 | 0 | 0 |
| Saturday | 0 | 769 | 579 | 575 | 559 | 512 | 612 | 388 | 0 | 0 |
| Sunday | 0 | 943 | 654 | 626 | 512 | 515 | 619 | 346 | 0 | 0 |

## Saturday Availability Windows
*Based on 18 Saturdays observed (2026-03-28 to 2026-08-01):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 94% | ⚠️ Usually taken |
| 3pm | 89% | ⚠️ Usually taken |
| 4pm | 94% | ⚠️ Usually taken |
| 5pm | 94% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 28.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 72% | ⚠️ Usually taken |
| 12pm | 67% | 🟡 Moderate demand |
| 1pm | 61% | 🟡 Moderate demand |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 28% | ✅ Often available |
| 4pm | 72% | ⚠️ Usually taken |
| 5pm | 83% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 83% | ⚠️ Usually taken |
| 12pm | 83% | ⚠️ Usually taken |
| 1pm | 83% | ⚠️ Usually taken |
| 2pm | 83% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 83% | ⚠️ Usually taken |
| 5pm | 83% | ⚠️ Usually taken |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 17% | ✅ Often available |
| 1pm | 22% | ✅ Often available |
| 2pm | 22% | ✅ Often available |
| 3pm | 28% | ✅ Often available |
| 4pm | 33% | 🟡 Moderate demand |
| 5pm | 78% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 26.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 17% | ✅ Often available |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 39% | 🟡 Moderate demand |
| 4pm | 44% | 🟡 Moderate demand |
| 5pm | 72% | ⚠️ Usually taken |

**Typical lead time at Kingsgate:** median 28.0 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 44% | 🟡 Moderate demand |
| 12pm | 44% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 28% | ✅ Often available |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 50% | 🟡 Moderate demand |

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
| bellevue | 26,682 |
| redmond | 5,727 |
| sammamish | 2,991 |
| kingsgate | 231 |
| issaquah | 222 |
| woodinville | 193 |

## Data Quality Notes
- Total records: 36,046
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 31,223
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 87% fresh — grows toward 100% as initial batch ages out
