---
name: querying-environmental-data
description: Use Estonian Environmental Portal datasets and services for air, water, nature, and environmental indicator analysis.
---

# Estonia Environmental Data

## Use when
- You need environmental indicators from official state sources.
- You need portal-routed datasets for ESG or policy analysis.

## Avoid when
- You need only weather forecasts (use weather skill).

## Inputs
- Domain (air/water/waste/nature), location, and period.

## Outputs
- Selected datasets with provenance and update cadence.

## Primary endpoint
- Portal: https://www.keskkonnaportaal.ee/en

## Workflow
1. Find the relevant environmental sub-domain.
2. Select official dataset/service with clear metadata.
3. Export or query available machine-readable output.
4. Return normalized data with unit and location metadata.

## Human setup (when needed)
- If a source is UI-only, provide exact steps for user export and then continue from local file(s).

## Quality checks
- Preserve measurement units and monitoring station metadata.
- Flag gaps or method changes across years.
