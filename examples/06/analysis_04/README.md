# Analysis 4: Food Price Inflation Drivers

This directory contains a comprehensive analysis of Estonia's food price inflation, examining why Estonia experienced Europe's highest food inflation rates during the 2022-2023 crisis period.

## Key Findings

- **Peak Inflation:** 29.75% (December 2022) - nearly double the EU average
- **Crisis Average:** 18.08% (2022-2023) vs ~10% EU average
- **Current Status:** 6.93% (2025) - converging toward EU norms

## Files

### Main Report
- **ANALYSIS.md** - Comprehensive 20KB report with:
  - Executive summary
  - Time series analysis (2020-2025)
  - Driver decomposition (energy, commodities, wages, market structure, climate)
  - Estonia vs EU comparison
  - Explanations for Estonia's exceptional rates
  - Policy recommendations

### Code and Data
- **analyze_food_inflation.py** - Main analysis script (13KB)
  - Fetches data from Statistics Estonia API (IA02 table)
  - Processes monthly CPI data by commodity group
  - Generates all visualizations
  - Calculates summary statistics

- **cpi_monthly_processed.csv** - Processed dataset (65KB)
  - Monthly CPI index values for all commodity groups (2020-2025)
  - Year-over-year and month-over-month inflation rates
  - 936 observations

- **cpi_monthly_raw.json** - Raw API response (14KB)
  - Original JSON-stat2 format data from Statistics Estonia

### Visualizations

1. **food_inflation_trend.png** (370KB)
   - Food inflation vs overall CPI for Estonia
   - Shows dramatic 2022-2023 spike and subsequent decline
   - Marks Ukraine war onset

2. **estonia_vs_eu_comparison.png** (341KB)
   - Estonia vs EU average food inflation
   - Demonstrates Estonia's ~15pp premium during crisis
   - Shows rapid convergence in 2024

3. **commodity_group_comparison.png** (698KB)
   - All 13 commodity groups inflation trends
   - Shows housing as highest category (30.83% avg 2022-2023)
   - Food as second-highest at 18.08%

### Supporting Files
- **ia02_structure.json** - API structure metadata for IA02 table
- **ia021_structure.json** - API structure metadata for IA021 table

## Running the Analysis

To reproduce the analysis:

```bash
cd examples/06/analysis_04
python3 analyze_food_inflation.py
```

This will:
1. Fetch latest CPI data from Statistics Estonia API
2. Process and calculate inflation rates
3. Generate all three visualizations
4. Output summary statistics to console
5. Save processed data to CSV

## Data Sources

- **Primary:** Statistics Estonia IA02 table (Monthly CPI by commodity group)
  - API: https://andmed.stat.ee/api/v1/en/stat/IA02
  - Format: JSON-stat2
  - Coverage: 2007-2025 (analysis focuses on 2020-2025)

- **Literature:** ECB Economic Bulletin (2024)
  - EU average peak: 15% (March 2023)
  - EU average Jan 2024: 5.7%
  - Climate impact: +0.8pp from 2022 heat

## Key Insights

### Why Estonia Had Europe's Highest Food Inflation

1. **Electricity Cost Volatility** - Estonia's power prices spiked to €300-400/MWh (vs €50 normal), directly impacting energy-intensive food sector

2. **Geographic Proximity** - Border state to conflict zone created supply chain disruption, security risk premium, and psychological impacts

3. **Import Dependency** - 60-70% of food imported; small market size amplifies global price shocks

4. **Market Concentration** - Top 3 retailers control ~70% market, reducing competitive pressure on pricing

5. **Wage-Price Spiral** - Tight labor market + 25% minimum wage increase (2022-2024) created feedback loop

### Policy Recommendations

**High Priority:**
- Accelerate renewable energy capacity to reduce electricity volatility
- Targeted VAT reductions and direct assistance for low-income households

**Medium Priority:**
- Enhance food retail competition through regulatory oversight
- Build supply chain resilience with strategic stockpiles

**Long-Term:**
- Increase agricultural self-sufficiency from 40% to 55%
- Develop regional Baltic cooperation on food security

## Methodology Notes

- **Inflation Calculation:** Year-over-year % change in CPI index (12-month lag)
- **Crisis Period:** Defined as 2022-01-01 to 2023-12-31
- **EU Comparison:** Based on ECB-reported reference points; full EU time series not available from Statistics Estonia
- **Statistical Significance:** All reported averages based on monthly observations; standard errors available in code output

## Contact

Part of the broader economic study examining Estonia's economic performance and policy effects (2020-2026).

Related analyses:
- Analysis 1: Consumer Confidence vs Economic Indicators
- Analysis 2: Tax Policy Impacts (planned)
- Analysis 3: Retail Sector Performance (planned)
- Analysis 5: Vehicle Market Response (planned)
