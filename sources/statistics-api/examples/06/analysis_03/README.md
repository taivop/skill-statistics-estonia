# Analysis 3: Retail Sector Performance Trends

## Overview

This analysis examines Estonia's retail sector performance from 2001-2025, with focus on the four consecutive years of decline (2022-2025) mentioned in Jüri Käo's ERR interview.

## Key Findings

- **Four-year decline confirmed**: Retail sales volume index fell from 100.0 (2021) to 96.8 average (2025 through Q3)
- **Nominal vs. real disconnect**: Nominal sales rose 33.7% (2020-2023) but volumes fell 2.1%, indicating all growth is price-driven
- **Structural weakness**: Three consecutive years of YoY volume decline (2022: -0.08%, 2023: -1.69%, 2024: -1.34%)
- **Commodity patterns**: Food sales inflation-driven (+11.4% nominal, negative volume), automotive fuel collapsed (-33.5%), manufactured goods weak (-4.0%)

## Files in This Directory

### Analysis Reports
- **ANALYSIS.md** - Comprehensive 25KB report with executive summary, decomposition, policy implications

### Data Scripts
- **fetch_data.py** - Downloads retail data from Statistics Estonia API
- **analyze.py** - Processes data, generates visualizations, exports CSV files

### Raw Data (JSON)
- **km00338_retail_sales_index.json** - Retail sales volume index (quarterly, 2001 Q1 - 2025 Q3)
- **km00338_structure.json** - Metadata for KM00338 table
- **km0061_retail_by_commodity.json** - Retail sales by commodity group (annual, 2005-2023)
- **km0061_structure.json** - Metadata for KM0061 table

### Processed Data (CSV)
- **retail_sales_analysis_data.csv** - Full quarterly time series with calculated metrics (YoY change, deviation from baseline, QoQ change)
- **commodity_sales_by_year.csv** - Annual sales by 12 commodity groups (2005-2023, thousand euros)
- **commodity_yoy_change.csv** - Year-over-year percentage changes by commodity group

### Visualizations (PNG)

1. **retail_sales_index_timeseries.png** (437KB)
   - Full historical index (2001-2025) with major events marked
   - Year-over-year change panel showing decline periods

2. **retail_sales_recent_analysis.png** (609KB)
   - Four-panel analysis (2019-2025):
     - Index level with 2019 peak and 2021 baseline
     - Year-over-year quarterly changes
     - Deviation from 2021 baseline
     - 4-quarter moving average

3. **retail_sales_seasonal_patterns.png** (144KB)
   - Average index by quarter (Q1-Q4)
   - Average quarter-over-quarter change patterns

4. **retail_sales_commodity_breakdown.png** (257KB)
   - Sales by commodity group (2020-2023)
   - Market share evolution over time

## Methodology

- **Data source**: Statistics Estonia (andmed.stat.ee API)
- **Volume vs. value**: KM00338 measures volume (2021=100), KM0061 measures nominal euros
- **Adjustments**: Seasonal and working-day adjusted
- **Time periods**:
  - Long-term: 2001 Q1 - 2025 Q3 (99 quarters)
  - Recent focus: 2019-2025 (captures pre-pandemic baseline, COVID, war impact)

## Reproduction

To reproduce this analysis:

```bash
# Fetch data from Statistics Estonia API
python3 fetch_data.py

# Run analysis and generate visualizations
python3 analyze.py
```

## Connection to Other Analyses

- **Analysis 1**: Consumer confidence correlation with retail sales
- **Analysis 2**: Tax policy impacts (VAT, vehicle registration) on retail volumes
- **Analysis 4**: Food price inflation driving nominal food sales growth despite volume weakness

## Date Created

January 17, 2026
