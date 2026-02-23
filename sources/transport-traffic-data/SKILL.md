---
name: transport-traffic-data
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
- Traffic safety programme context: https://www.transpordiamet.ee/en/safety-and-supervision/traffic-safety/traffic-safety-programme-2016-2025

## Workflow
1. Open traffic frequency resources and identify the relevant table/map export.
2. Use traffic safety programme indicators when policy-level context is requested.
3. Download available files and parse location identifiers.
4. Normalize units and temporal aggregation.
5. Return cleaned data with source mapping.

## Human setup (when needed)
- If data is published only via interactive map/UI, provide exact user steps to export/download, then continue automatically from supplied files.

## Quality checks
- Preserve road segment/site IDs.
- Distinguish annual average vs point-in-time measurements.
