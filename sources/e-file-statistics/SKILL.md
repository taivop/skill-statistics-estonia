---
name: e-file-statistics
description: Use RIK e-File statistics environment for public case-flow and procedural trend indicators across justice workflows.
---

# E-File Statistics

## Use when
- You need justice process statistics from the e-File environment.
- You need case-flow trend context across courts/procedure types.

## Avoid when
- You need case documents or party-level records.

## Inputs
- Procedure type, time period, and metric scope.

## Outputs
- Structured justice-process statistics with source metadata.

## Primary endpoints
- Statistics environment: https://www.rik.ee/en/e-file/statistics-environment

## Workflow
1. Open the statistics environment and identify relevant indicators.
2. Filter by period/procedure dimensions.
3. Extract values and normalize labels/units.
4. Return trend-ready dataset and caveats.

## Human setup (when needed)
- If indicators are only visible in interactive charts, guide the user through export/copy steps and continue from provided files.

## Quality checks
- Keep original metric definitions and period granularity.
- Separate counts, durations, and rate metrics.
