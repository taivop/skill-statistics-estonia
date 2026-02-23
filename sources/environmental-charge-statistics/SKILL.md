---
name: environmental-charge-statistics
description: Use Environmental Board environmental charge statistics for supervision and environmental-fee related indicator extraction.
---

# Environmental Charge Statistics

## Use when
- You need environmental charge statistics and supervision context.
- You need official environmental fee-related indicators.

## Avoid when
- You need general environmental quality indicators only.

## Inputs
- Charge type, period, and regulated activity scope.

## Outputs
- Structured environmental charge statistics and metadata.

## Primary endpoints
- Environmental charge statistics: https://www.keskkonnaamet.ee/en/supervision-environmental-charge/environmental-charge/statistics

## Workflow
1. Locate charge statistics source tables/publications.
2. Extract periodized indicators and categories.
3. Normalize units and category names.
4. Return trend-ready structured data.

## Human setup (when needed)
- If statistics are document-based, guide user through retrieval and continue from files.

## Quality checks
- Keep charge category definitions with values.
- Distinguish assessed vs collected values when available.
