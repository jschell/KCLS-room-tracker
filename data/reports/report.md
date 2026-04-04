# KCLS Room Monitor Report
*Generated: 2026-04-04 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 8,967 |
| Date range | 2026-03-22 to 2026-05-02 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (54%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 1,682 |
| Tuesday | 1,762 |
| Wednesday | 1,769 |
| Thursday | 536 |
| Friday | 1,481 |
| Saturday | 1,022 |
| Sunday | 715 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 566 |
| 11am | 1,190 |
| 12pm | 1,219 |
| 1pm | 1,204 |
| 2pm | 1,129 |
| 3pm | 1,153 |
| 4pm | 1,230 |
| 5pm | 817 |
| 6pm | 301 |
| 7pm | 158 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 26.0 | 15.0 | 28.0 | 28.0 | 0.3% | 6742 (3040 / 3702) |
| issaquah | 17.0 | 6.5 | 27.0 | 28.0 | 10.9% | 55 (23 / 32) |
| kingsgate | 17.5 | 7.8 | 28.0 | 28.0 | 8.9% | 56 (27 / 29) |
| redmond | 23.0 | 15.0 | 28.0 | 28.0 | 0.4% | 1503 (651 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 4.3% | 560 (382 / 178) |
| woodinville | 19.0 | 7.0 | 28.0 | 28.0 | 9.8% | 51 (21 / 30) |

*8,967 bookings total — 4,144 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 227 | 159 | 188 | 251 | 233 | 235 | 256 | 133 | 0 | 0 |
| Tuesday | 0 | 185 | 261 | 239 | 242 | 222 | 228 | 171 | 144 | 70 |
| Wednesday | 0 | 235 | 264 | 203 | 200 | 213 | 219 | 190 | 157 | 88 |
| Thursday | 93 | 37 | 55 | 67 | 59 | 75 | 100 | 50 | 0 | 0 |
| Friday | 246 | 181 | 217 | 186 | 168 | 194 | 182 | 107 | 0 | 0 |
| Saturday | 0 | 188 | 137 | 149 | 147 | 134 | 158 | 109 | 0 | 0 |
| Sunday | 0 | 205 | 97 | 109 | 80 | 80 | 87 | 57 | 0 | 0 |

## Saturday Availability Windows
*Based on 6 Saturdays observed (2026-03-28 to 2026-05-02):*

### Redmond
**East Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 67% | 🟡 Moderate demand |
| 1pm | 67% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**East Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 67% | 🟡 Moderate demand |
| 1pm | 67% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Conference Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 67% | 🟡 Moderate demand |
| 1pm | 67% | 🟡 Moderate demand |
| 2pm | 100% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 100% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Redmond:** median 23.0 days, p90 28.0 days

### Sammamish
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 33% | 🟡 Moderate demand |
| 12pm | 33% | 🟡 Moderate demand |
| 1pm | 33% | 🟡 Moderate demand |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 33% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 83% | ⚠️ Usually taken |

**Sunset Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 50% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 50% | 🟡 Moderate demand |
| 2pm | 50% | 🟡 Moderate demand |
| 3pm | 50% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 50% | 🟡 Moderate demand |

**Typical lead time at Sammamish:** median 7.0 days, p90 7.0 days

### Woodinville
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 17% | ✅ Often available |
| 1pm | 0% | ✅ Often available |
| 2pm | 0% | ✅ Often available |
| 3pm | 17% | ✅ Often available |
| 4pm | 17% | ✅ Often available |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Woodinville:** median 19.0 days, p90 28.0 days

### Kingsgate
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 67% | 🟡 Moderate demand |
| 12pm | 50% | 🟡 Moderate demand |
| 1pm | 17% | ✅ Often available |
| 2pm | 33% | 🟡 Moderate demand |
| 3pm | 50% | 🟡 Moderate demand |
| 4pm | 50% | 🟡 Moderate demand |
| 5pm | 67% | 🟡 Moderate demand |

**Typical lead time at Kingsgate:** median 17.5 days, p90 28.0 days

### Issaquah
**Meeting Room**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 17% | ✅ Often available |
| 12pm | 17% | ✅ Often available |
| 1pm | 33% | 🟡 Moderate demand |
| 2pm | 17% | ✅ Often available |
| 3pm | 17% | ✅ Often available |
| 4pm | 33% | 🟡 Moderate demand |
| 5pm | 33% | 🟡 Moderate demand |

**Typical lead time at Issaquah:** median 17.0 days, p90 28.0 days

### Bellevue
**Meeting Room 1**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 83% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 83% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 2**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 83% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 83% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 3**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 83% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 83% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 4**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 83% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 83% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Meeting Room 5**

| Hour | Booking rate | Status |
|------|-------------|--------|
| 11am | 100% | ⚠️ Usually taken |
| 12pm | 100% | ⚠️ Usually taken |
| 1pm | 100% | ⚠️ Usually taken |
| 2pm | 83% | ⚠️ Usually taken |
| 3pm | 83% | ⚠️ Usually taken |
| 4pm | 83% | ⚠️ Usually taken |
| 5pm | 100% | ⚠️ Usually taken |

**Typical lead time at Bellevue:** median 26.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 6,742 |
| redmond | 1,503 |
| sammamish | 560 |
| kingsgate | 56 |
| issaquah | 55 |
| woodinville | 51 |

## Data Quality Notes
- Total records: 8,967
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 4,144
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 46% fresh — grows toward 100% as initial batch ages out
