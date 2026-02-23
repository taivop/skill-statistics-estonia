---
name: rescue-incident-data
description: Query Rescue Board statistics pages for emergency incidents, response activity, and operational risk context.
---

# Rescue Incident Data

## Use when
- You need incident/response statistics from Rescue Board publications.
- You need operational emergency trend context.

## Avoid when
- You need police criminal-case data.

## Inputs
- Incident type, region, and time window.

## Outputs
- Incident-response statistics dataset and summary indicators.

## Primary endpoints
- Rescue Board statistics: https://www.rescue.ee/et/statistika

## Workflow
1. Locate relevant incident statistics publication/dashboard.
2. Extract period, region, and incident-type metrics.
3. Normalize category labels for consistent comparison.
4. Return trend-ready table with source annotations.

## Human setup (when needed)
- If data is chart-only or embedded in downloadable reports, guide user through export/copy steps and continue from provided files.

## Quality checks
- Keep incident-category definitions with extracted values.
- Separate incident counts from response-time metrics.
