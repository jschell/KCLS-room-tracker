# KCLS Room Monitor Report
*Generated: 2026-04-06 UTC*

## Dataset Summary
| Metric | Value |
|--------|-------|
| Total records | 9,597 |
| Date range | 2026-03-22 to 2026-05-04 |
| Libraries | bellevue, issaquah, kingsgate, redmond, sammamish, woodinville |
| Missing `created` (affects lead time) | 4,823 (50%) |

## Booking Volume by Day of Week
| Day | Bookings |
|-----|---------|
| Monday | 2,065 |
| Tuesday | 1,762 |
| Wednesday | 1,770 |
| Thursday | 536 |
| Friday | 1,482 |
| Saturday | 1,031 |
| Sunday | 951 |

## Booking Volume by Hour (All Libraries)
| Hour | Bookings |
|------|---------|
| 10am | 614 |
| 11am | 1,277 |
| 12pm | 1,315 |
| 1pm | 1,307 |
| 2pm | 1,218 |
| 3pm | 1,235 |
| 4pm | 1,313 |
| 5pm | 859 |
| 6pm | 301 |
| 7pm | 158 |

## Booking Lead Times
*How far in advance meeting rooms are reserved, inferred from first-seen date.*

> **Methodology:** `lead_days = booking_date − first_seen_date`. For bookings caught fresh (source=`grid_inferred`), first_seen ≈ creation date (accurate to ~12 hours). For the initial batch (source=`grid`), first_seen is a lower bound — true lead times may be longer.

| Library | Median days | p25 | p75 | p90 | % same-day | N (direct / lower-bound) |
|---------|------------|-----|-----|-----|------------|--------------------------|
| bellevue | 27.0 | 15.0 | 28.0 | 28.0 | 0.3% | 7132 (3430 / 3702) |
| issaquah | 17.0 | 5.5 | 27.0 | 28.0 | 10.2% | 59 (27 / 32) |
| kingsgate | 18.5 | 7.8 | 28.0 | 28.0 | 10.0% | 60 (31 / 29) |
| redmond | 26.0 | 15.0 | 28.0 | 28.0 | 0.5% | 1671 (819 / 852) |
| sammamish | 7.0 | 7.0 | 7.0 | 7.0 | 3.9% | 621 (443 / 178) |
| woodinville | 18.5 | 6.5 | 28.0 | 28.0 | 11.1% | 54 (24 / 30) |

*9,597 bookings total — 4,774 fresh-caught (accurate), 4,823 initial batch (lower bounds). Accuracy improves as the dataset matures.*

## Day × Hour Heatmap (Booking Counts)
| Day | 10am | 11am | 12pm | 1pm | 2pm | 3pm | 4pm | 5pm | 6pm | 7pm |
|-----|----|----|----|----|----|----|----|----|----|----|
| Monday | 275 | 195 | 230 | 311 | 289 | 291 | 313 | 161 | 0 | 0 |
| Tuesday | 0 | 185 | 261 | 239 | 242 | 222 | 228 | 171 | 144 | 70 |
| Wednesday | 0 | 235 | 264 | 203 | 201 | 213 | 219 | 190 | 157 | 88 |
| Thursday | 93 | 37 | 55 | 67 | 59 | 75 | 100 | 50 | 0 | 0 |
| Friday | 246 | 181 | 217 | 186 | 168 | 194 | 182 | 108 | 0 | 0 |
| Saturday | 0 | 188 | 143 | 152 | 147 | 134 | 158 | 109 | 0 | 0 |
| Sunday | 0 | 256 | 145 | 149 | 112 | 106 | 113 | 70 | 0 | 0 |

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

**Typical lead time at Redmond:** median 26.0 days, p90 28.0 days

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

**Typical lead time at Woodinville:** median 18.5 days, p90 28.0 days

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

**Typical lead time at Kingsgate:** median 18.5 days, p90 28.0 days

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

**Typical lead time at Bellevue:** median 27.0 days, p90 28.0 days


## Booking Frequency by Library
| Library | Bookings |
|---------|---------|
| bellevue | 7,132 |
| redmond | 1,671 |
| sammamish | 621 |
| kingsgate | 60 |
| issaquah | 59 |
| woodinville | 54 |

## Data Quality Notes
- Total records: 9,597
- Records missing `created` timestamp: 4,823
- Lead time coverage: 100% of records have lead time data (direct or inferred)
- Fresh-caught bookings (lead time accurate ±12h): 4,774
- Initial-batch bookings (lead time is lower bound — true lead may be longer): 4,823
- Data maturity: 50% fresh — grows toward 100% as initial batch ages out
