---
name: vaccination-statistics
description: Use Health Board vaccination statistics pages for immunization coverage trends and operational public-health monitoring context.
---

# Vaccination Statistics

## Use when
- You need vaccination coverage and trend indicators.
- You need official immunization monitoring context.

## Avoid when
- You need broader health service finance metrics.

## Inputs
- Vaccine group, period, and population scope.

## Outputs
- Structured vaccination indicator dataset and metadata.

## Primary endpoints
- Vaccination statistics: https://www.terviseamet.ee/en/nakkushaigused/statistika/vaktsineerimine

## Workflow
1. Retrieve relevant vaccination datasets/tables.
2. Extract indicators by group and period.
3. Normalize age/population categories.
4. Return trend-ready output with definitions.

## Human setup (when needed)
- If data is UI-table or report-only, guide user through export/download and continue from files.

## Quality checks
- Keep denominator definitions with coverage values.
- Mark updates/revisions explicitly.
