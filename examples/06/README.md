# Estonia Economic Study: Beyond Government Optimism

**A comprehensive empirical analysis of Estonia's economic challenges (2022-2026)**

## Overview

This study examines five economic paradoxes highlighted in Jüri Käo's ERR interview (January 17, 2026), where the Director of the Estonian Institute of Economic Research criticized the disconnect between government optimism and citizens' lived economic experience.

**Central Question:** Why does consumer confidence remain critically low despite official claims of economic "stabilization"?

## Key Findings

| Finding | Impact |
|---------|--------|
| **Tax Policy** | Revenue +31%, retail sales -19% |
| **Food Inflation** | 29.75% peak (2x EU average) |
| **Vehicle Market** | 51% collapse post-tax |
| **Retail Sector** | 3-year volume decline (2022-2024); 2025 recovery |
| **Consumer Confidence** | Correlates strongly with real economic activity |

**Conclusion:** The data patterns are consistent with concerns raised, though causation is difficult to establish. Important caveats apply—see ANALYSIS.md for details on data limitations and alternative explanations.

## Directory Structure

```
examples/06/
├── ANALYSIS.md              # Executive summary (start here)
├── METHODOLOGY.md           # Research design & literature review
├── PRESENTATION.md          # Marp slide deck (11 slides)
├── PRESENTATION.html        # HTML export for PDF conversion
├── PRESENTATION_README.md   # Export instructions
├── README.md                # This file
│
├── analysis_01/             # Consumer Confidence vs Economic Indicators
│   ├── ANALYSIS.md          # Detailed report
│   └── *.json, *.py         # Data & scripts
│
├── analysis_02/             # Tax Policy Impacts on Economic Activity
│   ├── ANALYSIS.md          # Detailed report
│   ├── *.png                # 3 visualizations
│   ├── *.csv                # Data exports
│   └── *.py                 # Analysis scripts
│
├── analysis_03/             # Retail Sector Performance Trends
│   ├── ANALYSIS.md          # Detailed report
│   ├── *.png                # 4 visualizations
│   └── *.py, *.json, *.csv  # Data & scripts
│
├── analysis_04/             # Food Price Inflation Drivers
│   ├── ANALYSIS.md          # Detailed report
│   ├── *.png                # 3 visualizations
│   └── *.py, *.json, *.csv  # Data & scripts
│
└── analysis_05/             # Vehicle Market Response to Taxation
    ├── ANALYSIS.md          # Detailed report
    ├── *.png                # 4 visualizations
    └── *.py, *.json, *.csv  # Data & scripts
```

## Quick Start

### For Overview
1. Read **ANALYSIS.md** - Executive summary with all key findings
2. View **PRESENTATION.html** in browser - Visual overview (11 slides)

### For Methodology
3. Read **METHODOLOGY.md** - Research design, literature review, data sources

### For Deep Dive
4. Explore **analysis_01/** through **analysis_05/** - Individual detailed studies with visualizations

### For Reproduction
5. Each analysis folder contains:
   - Python scripts to fetch data from Statistics Estonia API
   - Raw JSON data files
   - Analysis code
   - Visualization generation

### Presentation

The **PRESENTATION.html** file is pre-generated and ready to view. To regenerate from source:

```bash
# Install Marp CLI (one-time setup)
npm install -g @marp-team/marp-cli

# Regenerate HTML from markdown
cd examples/06
marp PRESENTATION.md --html -o PRESENTATION.html
```

**To export to PDF** (for LinkedIn/sharing):
1. Open `PRESENTATION.html` in Chrome/Edge/Firefox
2. Press `Ctrl+P` (or `Cmd+P` on Mac)
3. Select "Save as PDF"
4. Settings: Landscape orientation, no margins, background graphics ON

See **PRESENTATION_README.md** for detailed export instructions.

## Data Sources

**Primary:** Statistics Estonia (andmed.stat.ee)
- ESA 2010 accounting standards
- Quarterly/monthly data (1995-2025)
- Tables: GDP, CPI, retail sales, tax revenues, vehicle registrations

**Literature:** ECB, CEPR, IMF, academic studies (2019-2026)
- VAT pass-through rates
- Vehicle taxation impacts
- Food inflation drivers
- Consumer confidence research

## Key Statistics

- **Time Period:** 2010-2025 (some series from 1995)
- **Total Visualizations:** 14 high-quality charts (300 DPI PNG)
- **Data Files:** ~70 files (JSON, CSV, Python scripts)
- **Total Analysis:** ~32,000 lines of code, data, and documentation

## Methodological Approaches

1. **Time Series Analysis** - Descriptive analysis of trends and structural breaks
2. **Correlation Analysis** - Estimated relationships based on economic literature
3. **Event Study** - Tax policy impacts on retail sales and vehicle registrations
4. **Comparative Analysis** - Estonia vs EU averages (estimated from ECB literature)

**Note:** Formal econometric methods (DiD, VAR, RDD) were proposed but not implemented due to data limitations. See ANALYSIS.md for detailed methodology notes and caveats.

## Policy Implications

Based on empirical evidence, the study recommends:

1. **Realign messaging** with lived economic experience
2. **Address cost-of-living crisis** (food, energy priorities)
3. **Recalibrate tax policy** (avoid pro-cyclical increases)
4. **Energy independence** (nuclear/renewables investment)
5. **Rebuild trust** through transparent communication

## Citation

```
Estonia Economic Study: Beyond Government Optimism
Based on: Jüri Käo ERR interview, January 17, 2026
Data: Statistics Estonia (ESA 2010)
Analysis: Claude Sonnet 4.5
Repository: github.com/taivop/skill-statistics-estonia/examples/06
Date: January 2026
```

## License & Attribution

All data sourced from Statistics Estonia (public domain).
Analysis code and reports available under repository license.

## Contact & Feedback

For questions about methodology, data sources, or findings, see individual ANALYSIS.md files in each subdirectory or consult the comprehensive METHODOLOGY.md document.

---

**Navigation:**
- [← Back to Examples](../)
- [Executive Summary →](./ANALYSIS.md)
- [Methodology →](./METHODOLOGY.md)
- [Presentation Slides →](./PRESENTATION.html)
