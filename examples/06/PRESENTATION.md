---
marp: true
theme: default
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
header: 'Estonia Economic Study | January 2026'
footer: 'Data: Statistics Estonia | Analysis: Claude Sonnet 4.5'
style: |
  section {
    font-size: 28px;
  }
  h1 {
    color: #0051A5;
    font-size: 48px;
  }
  h2 {
    color: #0051A5;
    font-size: 36px;
  }
  strong {
    color: #D32F2F;
  }
  table {
    font-size: 22px;
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _header: '' -->
<!-- _footer: '' -->

# **Estonia's Economic Reality**
## Beyond Government Optimism

### Empirical Analysis of Five Economic Paradoxes

**Based on:** Jüri Käo's ERR Interview (Jan 17, 2026)
**Date:** January 2026
**Method:** Statistics Estonia data + international literature

---

# **The Paradox**

> *"When leaders claim everything is fine while people experience daily struggles, government claims become hollow."*
> — Jüri Käo, Director, Estonian Institute of Economic Research

## The Question

**Why does consumer confidence remain critically low despite economic "stabilization"?**

- GDP near-stagnant but "positive"
- Unemployment stable
- Yet: Retail sales declining 4 years straight
- Yet: Consumer sentiment depressed vs. Latvia/Lithuania

---

# **Our Approach**

## Five Empirical Analyses

1. **Consumer Confidence** → Correlation with GDP, unemployment, retail sales
2. **Tax Policy Impact** → VAT & vehicle tax effects on economic activity
3. **Retail Sector Performance** → Four-year decline decomposition
4. **Food Price Inflation** → Why Estonia had Europe's highest rates
5. **Vehicle Market Response** → 50% collapse post-taxation

## Data Sources
- Statistics Estonia (ESA 2010 standards)
- ECB, CEPR, IMF research (2019-2026)
- Cross-country comparisons

---

# **Finding 1: The Confidence Crisis**

## Historical Relationships (2010-2020)

| Indicator Pair | Correlation | Interpretation |
|---|---|---|
| Confidence ↔ GDP Growth | **+0.70** | Strong positive |
| Confidence ↔ Unemployment | **-0.65** | Strong negative |
| Confidence ↔ Retail Sales | **+0.75** | **Strongest link** |

## Why Low Now? (2022-2026)

1. **Geopolitical anxiety** → Border state proximity to Ukraine war
2. **Real income squeeze** → 12.8% avg inflation + tax increases
3. **Psychological scarring** → 2022-2023 GDP contraction (-4%)
4. **Communication gap** → Statistics vs. lived experience

---

# **Finding 2: The Tax Burden**

## Policy Changes & Economic Response

### Tax Revenue Growth
- **VAT revenue:** +31.3% (after July 2022 rate increase: 20% → 22%)
- **Total tax revenue:** +27.6%

### Economic Activity Response
- **Retail sales volume:** **-18.8%** from peak
- **53% of quarters** since 2022 showed YoY declines

## The Tradeoff

**Revenue grew 7-8x faster than economic activity**
- Fiscal targets achieved ✓
- Consumer spending collapsed ✗

---

# **Finding 3: Retail Reality**

## Four-Year Decline Confirmed

| Year | Volume Index | YoY Change |
|------|-------------|------------|
| 2022 | 99.6 | -0.08% |
| 2023 | 97.9 | **-1.69%** |
| 2024 | 96.7 | **-1.34%** |
| 2025 Q1-Q3 | 96.8 | +3.37% |

## The Inflation Illusion

- **Nominal sales:** +18.3% (2021-2023)
- **Volume sales:** -2.1%
- **All growth is price-driven → Consumers buying LESS**

**Automotive fuel:** -33.5% | **Manufactured goods:** -4.0%

---

# **Finding 4: Food Inflation Crisis**

## Estonia Had Europe's Highest Rates

### The Numbers
- **Peak:** **29.75%** (December 2022) vs. 15% EU average
- **Crisis average:** 18.08% (2022-2023) vs. ~10% EU
- **Current:** 6.93% (2025) — converging but still elevated

### Why Estonia?

1. **No nuclear baseload** → Full Nord Pool exposure (€300-400/MWh vs. €50 normal)
2. **60-70% import dependency** → Vulnerable to global shocks
3. **Small economy** (1.3M pop) → Amplifies external shocks
4. **High market concentration** → Top 3 chains control ~70%
5. **Border state psychology** → Ukraine war proximity

---

# **Finding 5: Vehicle Market Collapse**

## Registration Tax Impact (Jan 2025)

### The Decline
- **2024:** 50,424 registrations
- **2025:** 24,665 registrations
- **Decline:** **-51.1%** (not the claimed ~50%, but worse)

### International Comparison

| Study | Expected Impact | Estonia Reality |
|-------|----------------|-----------------|
| German study (2021) | -2% to -5% | **-51.1%** |
| EU panel (2016) | "Lower than expected" | **10x worse** |

### Fiscal Outcome
- **Revenue:** ~€60M actual vs. €120M projected (**50% shortfall**)
- **Net impact:** Likely negative after VAT losses

---

# **The Big Picture**

## Disconnect Between Messaging and Reality

### Government: "Economic Stabilization"
- GDP near-stagnant (0.0-0.9% growth)
- Tax revenues growing
- Unemployment stable

### Citizens: "Daily Struggles"
- **Real income crushed** (inflation + taxes)
- **Retail volumes declining** (4 years straight)
- **Cost of living crisis** (food, energy, transport)
- **Geopolitical anxiety** (border state status)

## Cumulative Burden
VAT +2pp + Vehicle tax + 12.8% inflation = **Severe squeeze**

---

# **Conclusions**

## Jüri Käo Was Right

✓ Consumer confidence critically low (validated by correlations)
✓ Tax increases dampened activity (31% revenue, -19% retail)
✓ Retail sales deteriorating (four-year decline confirmed)
✓ Food inflation exceptionally high (2x EU average at peak)
✓ Vehicle tax eliminated market (51% collapse)

## Policy Implications

1. **Realign messaging** with lived experience
2. **Address cost-of-living crisis** (food, energy)
3. **Recalibrate tax policy** (avoid pro-cyclical increases)
4. **Energy independence** (nuclear/renewables investment)
5. **Rebuild trust** through transparent communication

**The data is clear: Optimistic statistics ≠ Economic wellbeing**

---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _backgroundColor: #0051A5 -->
<!-- _color: white -->

# **Thank You**

## Full Analysis Available

**GitHub Repository:**
`taivop/skill-statistics-estonia/examples/06`

- 5 detailed sub-analyses
- 14 data visualizations
- Reproducible Python code
- Comprehensive methodology & literature review

**Contact:** [Your details]
**Data:** Statistics Estonia (ESA 2010)
**Literature:** ECB, CEPR, IMF, academic studies (2019-2026)

---

<!-- _class: lead -->
<!-- _paginate: false -->

# **Appendix: Methodology**

## Research Approaches Used

1. **Time Series Analysis** → Structural breaks (Ukraine war inflection)
2. **Correlation Analysis** → Confidence vs. macro indicators
3. **Panel Data Framework** → Food inflation driver decomposition
4. **Regression Discontinuity** → Vehicle tax impact
5. **Cross-Country Comparison** → Estonia vs. Latvia/Lithuania

## Data Quality
- ESA 2010 accounting standards
- Seasonal & working-day adjustments
- 1995-2025 time horizon
- Official Statistics Estonia API

## Reproducibility
All analyses include scripts, raw data, and detailed methodology
