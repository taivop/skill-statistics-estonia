---
name: health-statistics
description: Query Estonia Health Statistics database (TAI) for official health indicators, outcomes, and utilization metrics.
---

# Estonia Health Statistics (TAI)

## Use when
- You need official health indicators from TAI statistics database.
- You need demographic or service-utilization breakdowns.

## Avoid when
- You need patient-level records (not public).

## Inputs
- Indicator topic, geography, demographic cuts, and period.

## Outputs
- Extracted health indicator table with definitions.

## Primary endpoint
- Database: https://statistika.tai.ee/

## Workflow
1. Locate indicator table and dimensions.
2. Apply filters in the query interface.
3. Export to machine-readable format.
4. Clean labels and produce analysis-ready table.

## Human setup (when needed)
- If export is browser-only, guide user through exact menu/filter/export actions and continue from the downloaded file.

## Quality checks
- Confirm denominator/population base for rates.
- Note methodology revisions and breaks in series.
