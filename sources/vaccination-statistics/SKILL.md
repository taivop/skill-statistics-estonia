---
name: vaccination-statistics
description: Use Health Board vaccination statistics pages for immunization coverage trends and operational public-health monitoring context.
---

# Vaccination Statistics

## Use when
- You need vaccination coverage and trend indicators.
- You need official immunization monitoring context.

## Avoid when
- You need broader health service finance metrics.

## Inputs
- Vaccine group, period, and population scope.

## Outputs
- Structured vaccination indicator dataset and metadata.

## Primary endpoints
- Vaccination statistics: https://www.terviseamet.ee/en/nakkushaigused/statistika/vaktsineerimine

## Workflow
1. Retrieve relevant vaccination datasets/tables.
2. Extract indicators by group and period.
3. Normalize age/population categories.
4. Return trend-ready output with definitions.

## Human setup (when needed)
- If data is UI-table or report-only, guide user through export/download and continue from files.

## Quality checks
- Keep denominator definitions with coverage values.
- Mark updates/revisions explicitly.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.terviseamet.ee/en/nakkushaigused/statistika/vaktsineerimine (HTTP 200, text/html;, file links detected: 1)

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
