---
name: querying-estonia-police-operational-statistics
description: Query Police and Border Guard Board public publications for operational statistics context, annual reporting, and incident-related indicators.
---

# Police Operational Statistics

## Use when
- You need official police operational statistics context.
- You need annual publication-based indicators from PPA sources.

## Avoid when
- You need court-level procedural outcomes.

## Inputs
- Topic scope (crime, border, response), period, and region.

## Outputs
- Extracted police operational indicators with source citations.

## Primary endpoints
- Police and Border Guard Board portal: https://www.politsei.ee/en

## Workflow
1. Locate relevant statistics/news/report publication within official PPA pages.
2. Extract comparable indicators and periods.
3. Normalize category labels and definitions.
4. Return structured table plus source notes.

## Human setup (when needed)
- If statistics are published only via downloadable reports or press releases, guide user through retrieval and continue from provided files.

## Quality checks
- Keep indicator definitions tied to each source.
- Do not infer missing values; mark unknowns explicitly.

## Limitations
- A dedicated public API/statistics endpoint may not be exposed from the main entry page; use official published reports/pages as evidence sources.
