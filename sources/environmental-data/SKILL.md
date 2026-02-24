---
name: environmental-data
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

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.keskkonnaportaal.ee/en (HTTP 200, text/html;, file links detected: 0)

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
