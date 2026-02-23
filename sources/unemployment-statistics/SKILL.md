---
name: unemployment-statistics
description: Query Estonian Unemployment Insurance Fund statistics and studies for labor-market, unemployment, and employment-service indicators.
---

# Unemployment Statistics (Töötukassa)

## Use when
- You need unemployment and labor-market indicators from Töötukassa.
- You need employment-service trend context.

## Avoid when
- You only need macro labor indicators already in Stats Estonia tables.

## Inputs
- Period, region, demographic scope, and indicator set.

## Outputs
- Unemployment/labor dataset and trend summaries.

## Primary endpoints
- Statistics and studies: https://www.tootukassa.ee/et/statistika-ja-uuringud

## Workflow
1. Locate target indicator publication/table.
2. Extract period and regional dimensions.
3. Normalize metric definitions and units.
4. Return analysis-ready table with metadata notes.

## Human setup (when needed)
- If data must be downloaded manually from portal widgets, guide user through exact selections and continue from exported files.

## Quality checks
- Preserve indicator definitions per publication.
- Distinguish stock vs flow metrics.
