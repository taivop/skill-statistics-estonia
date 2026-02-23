---
name: analyzing-estonia-election-results-data
description: Analyze Estonian election archive and open election datasets from valimised.ee for turnout, vote shares, and historical election trends.
---

# Estonia Election Results Data

## Use when
- You need historical election results, turnout, or e-voting statistics.
- You need multi-election comparisons.

## Avoid when
- You need parliamentary voting records (use Riigikogu open data skill).

## Inputs
- Election type, years, geography, and metric.

## Outputs
- Election result dataset and harmonized comparison table.

## Primary endpoints
- Main site: https://www.valimised.ee/en
- Elections archive (ET): https://www.valimised.ee/et/toimunud-valimiste-arhiiv
- Election open data (ET): https://www.valimised.ee/et/valimiste-arhiiv/valimiste-avaandmed

## Workflow
1. Choose election type and years from archive/open-data pages.
2. Download available machine-readable files.
3. Harmonize geography and party/candidate naming across years.
4. Return trend-ready dataset with caveats.

## Human setup (when needed)
- If only Estonian-language navigation is available, walk user through the exact ET menu path and what file to download.

## Quality checks
- Keep election-type boundaries separate (EP, parliamentary, local, referendum).
- Track boundary or constituency changes before trend comparisons.
