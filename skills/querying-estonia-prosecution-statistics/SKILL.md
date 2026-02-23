---
name: querying-estonia-prosecution-statistics
description: Query Estonian Prosecutor's Office statistical and annual reporting materials for prosecution workload, outcomes, and enforcement context.
---

# Prosecution Statistics

## Use when
- You need prosecutor workload/outcome statistics.
- You need annual prosecutorial performance context.

## Avoid when
- You need police incident-level logs.

## Inputs
- Period, offence category, and prosecution-stage scope.

## Outputs
- Prosecution metrics dataset with periodized dimensions.

## Primary endpoints
- Prosecutor's year/interesting facts: https://www.prokuratuur.ee/en/about-prosecutors-office/interesting-facts/procecutors-year

## Workflow
1. Locate relevant annual/statistics publication.
2. Extract comparable indicators across years.
3. Normalize offence and outcome categories.
4. Return trend table with source citations.

## Human setup (when needed)
- If data is only in narrative pages/PDFs, walk user through obtaining files and continue from uploaded documents.

## Quality checks
- Preserve official category labels before any regrouping.
- Keep charge/prosecution/outcome stages separate.
