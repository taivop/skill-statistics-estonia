---
name: aviation-safety-reports
description: Use aviation safety report pages for official safety reporting outputs, trend context, and structured extraction of published materials.
---

# Aviation Safety Reports

## Use when
- You need official aviation safety reporting outputs and trends.
- You need structured extraction from published safety materials.

## Avoid when
- You need aircraft registration records only.

## Inputs
- Safety topic, period, and report scope.

## Outputs
- Structured aviation safety report indicators and references.

## Primary endpoints
- Aviation safety reports: https://www.transpordiamet.ee/en/aviation-and-aviation-safety/aviation-safety/reports

## Workflow
1. Retrieve relevant safety reports/publications.
2. Extract indicators/findings and period scope.
3. Normalize taxonomy and units.
4. Return structured output with source citations.

## Human setup (when needed)
- If reports are file-based only, guide user through download/retrieval and continue from files.

## Quality checks
- Keep report edition/date with every extracted metric.
- Distinguish incident counts from risk recommendations.
