# Estonia Population Pyramid by Age Group and Sex (Latest Year)

## Executive summary

- Latest available year in RV021 is **2025** (population as at 1 January 2025).
- Total population covered by the selected age groups: **1,369,995** (males 649,753, females 720,242).
- Working-age (15-64) population is **63.5%** of total; children (0-14) **15.6%**; older adults (65+) **20.9%**.
- Largest cohorts are ages **35-39** and **40-44**, indicating a bulge in mid-working ages.

## Data sources and methodology

- Source: Statistics Estonia API (andmed.stat.ee), table **RV021: Population by sex and age group, 1 January**.
- Metadata: ESMS metadata fetched via `get_metadata.py` (metadata ID 30101) and saved locally for context.
- Data query: year **2025**, sexes **Males** and **Females**, all age-group codes from RV021.
- Cleaning: excluded aggregate rows **"Age groups total"**, **"85 and older"** (overlaps with 85-89, 90-94, 95-99, 100+), and **"Age unknown"** to avoid double counting.
- Output files saved under `examples/04/` as required (JSON response, CSV export, PNG chart, and this report).

## Key findings

### Population totals by sex (1 January 2025)

| Sex | Population | Share of total |
|---|---:|---:|
| Males | 649,753 | 47.4% |
| Females | 720,242 | 52.6% |
| **Total** | **1,369,995** | **100.0%** |

### Age structure summary

| Age group block | Population | Share of total |
|---|---:|---:|
| 0-14 | 213,728 | 15.6% |
| 15-64 | 869,824 | 63.5% |
| 65+ | 286,443 | 20.9% |

| Dependency ratio (per 100 working-age 15-64) | Value |
|---|---:|
| Children (0-14) | 24.6 |
| Older adults (65+) | 32.9 |

### Largest age cohorts (total population)

| Rank | Age group | Population | Share of total |
|---:|---|---:|---:|
| 1 | 35-39 | 108,672 | 7.9% |
| 2 | 40-44 | 100,437 | 7.3% |
| 3 | 45-49 | 94,159 | 6.9% |
| 4 | 50-54 | 93,392 | 6.8% |
| 5 | 30-34 | 88,157 | 6.4% |

### Population by age group and sex (1 January 2025)

| Age group | Males | Females | Total |
|---|---:|---:|---:|
| 0 | 4,939 | 4,787 | 9,726 |
| 1-4 | 26,197 | 25,008 | 51,205 |
| 5-9 | 38,912 | 36,698 | 75,610 |
| 10-14 | 39,468 | 37,719 | 77,187 |
| 15-19 | 40,682 | 38,277 | 78,959 |
| 20-24 | 34,455 | 33,839 | 68,294 |
| 25-29 | 34,702 | 33,051 | 67,753 |
| 30-34 | 45,731 | 42,426 | 88,157 |
| 35-39 | 56,684 | 51,988 | 108,672 |
| 40-44 | 51,648 | 48,789 | 100,437 |
| 45-49 | 48,027 | 46,132 | 94,159 |
| 50-54 | 46,471 | 46,921 | 93,392 |
| 55-59 | 40,210 | 43,496 | 83,706 |
| 60-64 | 39,653 | 46,642 | 86,295 |
| 65-69 | 35,263 | 47,537 | 82,800 |
| 70-74 | 27,338 | 43,337 | 70,675 |
| 75-79 | 18,748 | 35,244 | 53,992 |
| 80-84 | 11,305 | 26,550 | 37,855 |
| 85-89 | 6,765 | 21,010 | 27,775 |
| 90-94 | 2,175 | 8,422 | 10,597 |
| 95-99 | 352 | 2,146 | 2,498 |
| 100 and older | 28 | 223 | 251 |

## Data visualizations

![Population pyramid](./population_pyramid_2025.png)

## Conclusions and insights

- The population pyramid shows a **pronounced middle-age bulge**, with the largest cohorts in 35-44, indicating past higher birth rates or migration inflows for these ages.
- **Females outnumber males** in older ages, especially 70+, which is consistent with higher female longevity.
- The **older-age dependency ratio (32.9 per 100 working-age)** exceeds the child dependency ratio (24.6), highlighting aging-population pressures.
- The **working-age share (63.5%)** remains the majority but is below two-thirds, suggesting ongoing demographic aging trends.