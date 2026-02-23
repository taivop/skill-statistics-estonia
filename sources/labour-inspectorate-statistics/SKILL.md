---
name: labour-inspectorate-statistics
description: Use Labour Inspectorate statistics publications for workplace safety, labour compliance, and inspection trend analysis.
---

# Labour Inspectorate Statistics

## Use when
- You need official labour inspection/safety statistics.
- You need trend context for workplace violations or incidents.

## Avoid when
- You need individual case-level confidential files.

## Inputs
- Period, sector, region, and indicator scope.

## Outputs
- Structured labour-inspection statistics dataset.

## Primary endpoints
- Statistics page: https://www.tooinspektsioon.ee/asutus-uudised-ja-kontaktid/kontakt/statistika

## Workflow
1. Locate relevant statistics publication/table.
2. Extract periodized indicators and categories.
3. Normalize labels, units, and dimensions.
4. Return analysis-ready dataset with source notes.

## Human setup (when needed)
- If data is in downloadable documents only, guide user through download and continue from files.

## Quality checks
- Keep incident/inspection/enforcement metrics separate.
- Preserve official category names before regrouping.
