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

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.transpordiamet.ee/en (HTTP 200, text/html;, file links detected: 1)
- https://www.transpordiamet.ee/liiklussagedus (HTTP 200, text/html;, file links detected: 3)
- https://www.transpordiamet.ee/en/safety-and-supervision/traffic-safety/traffic-safety-programme-2016-2025 (HTTP 200, text/html;, file links detected: 2)

## Request contract
- Use the listed primary endpoints as authoritative entry points.
- If API/query parameters are only visible in-browser, preserve exact request URL, params, and headers in output metadata.
- If endpoint is UI-only, document click path and extraction method used.

## Output schema expectations
- Keep at least: source URL, retrieval timestamp, publication/update date (if available), title/record label, and extracted governance-relevant fields.
- Preserve original field names when present in downloadable/API output.

## Limits and caveats
- Confirm whether data is open-download, UI-only, or authenticated before claiming full access.
- Separate narrative/guidance text from measurable records.

## Verification hooks
- Validate endpoint reachability and content type before extraction.
- Validate that each extracted claim is linked to a concrete source URL.
