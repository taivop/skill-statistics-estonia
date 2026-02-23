---
name: querying-transport-traffic-data
description: Retrieve Estonia transport and road traffic frequency data from Transport Administration sources for mobility and infrastructure analysis.
---

# Estonia Transport Traffic Data

## Use when
- You need road traffic intensity/frequency indicators.
- You need transport-side explanatory data for regional analysis.

## Avoid when
- You need only city-level municipal mobility datasets.

## Inputs
- Road/network scope, location, and period.

## Outputs
- Traffic dataset extract and metadata on counting context.

## Primary endpoints
- Agency site: https://www.transpordiamet.ee/en
- Traffic frequency page (ET): https://www.transpordiamet.ee/liiklussagedus

## Workflow
1. Open traffic frequency resources and identify the relevant table/map export.
2. Download available files and parse location identifiers.
3. Normalize units and temporal aggregation.
4. Return cleaned data with source mapping.

## Human setup (when needed)
- If data is published only via interactive map/UI, provide exact user steps to export/download, then continue automatically from supplied files.

## Quality checks
- Preserve road segment/site IDs.
- Distinguish annual average vs point-in-time measurements.
