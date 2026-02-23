# Economic Study: Estonia's Economic Performance and Policy Effects

## Study Questions from Article Analysis

Based on Jüri Käo's interview (ERR, January 17, 2026), this study addresses five interconnected empirical questions:

1. **Consumer Confidence Paradox**: Why has Estonian consumer confidence remained critically low for four years despite improvements in other economic indicators?

2. **Tax Policy Effects**: How have recent tax increases (VAT, vehicle registration tax) affected economic activity, retail sales, and government revenues?

3. **Food Price Inflation**: What drives Estonia's persistently high food price inflation compared to EU peers?

4. **Retail Sector Performance**: What explains the four consecutive years of retail sales decline and January 2026 deterioration?

5. **Vehicle Market Response**: How has the motor vehicle registration tax impacted car sales and market structure?

## Methodological Approaches

### 1. Time Series Analysis with Structural Breaks

**Rationale**: Consumer confidence and retail sales exhibit potential structural breaks around policy changes and the Ukraine war onset (February 2022).

**Methods**:
- Bai-Perron sequential break test
- ARIMA models with intervention analysis
- Rolling correlation analysis between confidence and macro indicators

**Literature Foundation**:
- Consumer confidence as predictor: Conference Board (2024), University of Michigan (2026)
- Structural breaks in European economies: ECB Economic Bulletin (2024)

### 2. Difference-in-Differences (DiD) Analysis

**Rationale**: Compare Estonia's outcomes to Latvia and Lithuania (similar Baltic economies) around tax policy changes.

**Methods**:
- Parallel trends testing for pre-treatment periods
- Synthetic control method if parallel trends violated
- Event study estimates for dynamic treatment effects

**Literature Foundation**:
- VAT effects: CEPR (2024) - 42% pass-through rate finding
- Cross-country European tax studies: IMF WP/19/96 (2019)

### 3. Vector Autoregression (VAR) Models

**Rationale**: Understand dynamic relationships between consumer confidence, retail sales, unemployment, wages, and CPI.

**Methods**:
- Identify optimal lag structure using information criteria
- Granger causality tests
- Impulse response functions and variance decomposition

**Literature Foundation**:
- Geopolitical uncertainty effects: CEPR (2024), ScienceDirect (2024)
- Baltic economic dynamics: Luminor Economic Outlook (2024)

### 4. Panel Data Regression

**Rationale**: Decompose food price inflation drivers using cross-sectional variation.

**Methods**:
- Fixed effects models controlling for unobserved heterogeneity
- Decompose into: energy costs, commodity prices, wages, margins
- Comparison with EU member states

**Literature Foundation**:
- ECB (2024): Energy costs main driver, 15% peak inflation March 2023
- Climate impacts: Extreme heat added 0.8pp to food prices
- Domestic wage/profit factors increasingly important

### 5. Regression Discontinuity Design (RDD)

**Rationale**: Vehicle registration tax created sharp discontinuities in purchasing behavior.

**Methods**:
- Identify registration thresholds and tax rate changes
- Local polynomial estimation around discontinuities
- Examine market composition changes (new vs. used, emissions levels)

**Literature Foundation**:
- ScienceDirect (2025): €1000 incentive increases BEV sales 17-40%
- German study (2021): Circulation tax reduces sales 2-5%
- Italian "Superbollo" tax increased low-emission vehicle share

## Data Sources

### Statistics Estonia API

**Primary Tables**:
1. **KM00338** - Retail Sales Volume Index (quarterly)
2. **IA001** - Consumer Price Index, change over previous year
3. **IA021** - Consumer Price Index, change (monthly)
4. **TT445** - Unemployed persons by duration (quarterly)
5. **RAA0012** - GDP and GNI (quarterly, ESA 2010)
6. **RR024** - State budget tax revenues (quarterly)
7. **RR027** - State budget tax revenues (monthly)

**Supplementary Tables**:
- **KM0061** - Retail sales by economic activity and commodity
- **KM0011** - Motor vehicle sales and maintenance
- **TT0160** - Labour market indicators (quarterly)

### Eurostat (for cross-country comparisons)

- Consumer confidence harmonized indices (Latvia, Lithuania, Estonia)
- HICP food price indices by category
- Motor vehicle registration statistics

### Potential Scraping Sources

1. **Estonian Tax and Customs Board** (emta.ee)
   - Detailed tax revenue by category
   - VAT collection data
   - Vehicle registration statistics

2. **Bank of Estonia** (eestipank.ee)
   - Financial stability indicators
   - Credit statistics
   - Consumer sentiment surveys

3. **European Central Bank Statistical Data Warehouse**
   - Baltic economic indicators
   - Harmonized inflation measures
   - Interest rates

4. **ERR News Archive**
   - Policy announcement dates
   - Expert commentary timeline
   - Public discourse analysis

## Literature Review

### Consumer Confidence

- **Conference Board (2024)**: US CCI at 89.1 (Dec 2025), down from 92.9
- **University of Michigan (2026)**: Sentiment at 54.0 (Jan 2026), 25% below year prior
- **OECD**: CCI >100 signals increased confidence and spending inclination

### VAT and Tax Policy Effects

- **CEPR (2024)**: 1% VAT increase → 0.42% price increase (42% pass-through, "under-shifting")
- **IMF WP/19/96 (2019)**: VAT design matters for growth; base broadening vs. rate increases
- **ScienceDirect (2024)**: VAT changes have heterogeneous effects by product type
- **Keen & Lockwood (2010)**: VAT is a "money machine" for revenue generation

### Food Price Inflation

- **ECB Economic Bulletin (2024)**: Energy costs main driver (2021-2022)
- Peak inflation: 15% (March 2023), declined to 5.7% (January 2024)
- **ECB (2026)**: Domestic wage/profit factors increasingly important
- **Climate impacts**: Extreme heat summer 2022 added ~0.8pp to food prices

### Geopolitical Uncertainty

- **CEPR (2024)**: Geopolitical risks → pessimistic expectations, elevated income uncertainty
- **Baltic Times (2025)**: Estonian sentiment depressed vs. Latvia/Lithuania despite similar circumstances
- **Luminor (2024)**: Foreign investors committed but skeptical about growth prospects

### Vehicle Taxation

- **ScienceDirect (2025)**: €1000/year incentive increases PHEV sales 50-90%, BEV 17-40%
- **German study (2021)**: Circulation tax reduces sales 2-5%
- **Italian Superbollo**: Tax introduction increased low-emission vehicle share
- **EU study (2016)**: Tax-price relationships statistically significant but smaller than expected

## Analysis Plan

Each analysis will be conducted in a separate directory with:
- Data acquisition scripts
- Analysis code (Python/R)
- Output visualizations (PNG)
- Markdown report with findings

### Analysis 1: Consumer Confidence vs Economic Indicators
- Time series of confidence, unemployment, GDP, wages
- Correlation analysis over time
- Structural break identification

### Analysis 2: Tax Policy Impacts
- Tax revenue trends vs. VAT rate changes
- Retail sales response to tax increases
- Cross-country comparison (Estonia vs. Latvia/Lithuania)

### Analysis 3: Retail Sector Performance
- 4-year decline decomposition by category
- Seasonal patterns
- Relationship with consumer confidence

### Analysis 4: Food Price Inflation Drivers
- Decomposition of food CPI components
- Comparison with EU average
- Energy cost correlation

### Analysis 5: Vehicle Market Response
- Registration statistics before/after tax
- Market structure changes
- Revenue vs. sales trade-off

## Quality Standards

All analyses will:
- Document data sources and methodology
- Include reproducible code
- Present uncertainty quantification
- Acknowledge limitations
- Connect findings to policy implications
