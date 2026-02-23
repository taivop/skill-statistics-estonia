---
name: maritime-economy-statistics
description: Use Transport Administration maritime economy statistics for shipping-sector indicators and maritime operations context.
---

# Maritime Economy Statistics

## Use when
- You need shipping/maritime economy indicators.
- You need official maritime sector operations context.

## Avoid when
- You only need port registry metadata.

## Inputs
- Indicator scope, period, and maritime segment.

## Outputs
- Structured maritime economy indicators dataset.

## Primary endpoints
- Maritime economy statistics: https://www.transpordiamet.ee/en/maritime-and-waterways/bringing-ships-under-estonian-flag/maritime-economy-statistics

## Workflow
1. Locate relevant maritime statistics tables/publications.
2. Extract indicators by period/segment.
3. Normalize category and unit definitions.
4. Return trend-ready structured output.

## Human setup (when needed)
- If indicators are in downloadable reports, guide user through retrieval and continue from files.

## Quality checks
- Preserve metric definitions and units.
- Distinguish fleet, activity, and financial indicators.
