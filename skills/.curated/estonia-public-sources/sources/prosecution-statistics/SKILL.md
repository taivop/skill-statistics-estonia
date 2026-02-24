---
name: prosecution-statistics
description: Query Estonian Prosecutor's Office statistical and annual reporting materials for prosecution workload, outcomes, and enforcement context.
---

# Prosecution Statistics

## Use when
- You need prosecutor workload/outcome statistics.
- You need annual prosecutorial performance context.

## Avoid when
- You need police incident-level logs.

## Inputs
- Period, offence category, and prosecution-stage scope.

## Outputs
- Prosecution metrics dataset with periodized dimensions.

## Primary endpoints
- Prosecutor's year/interesting facts: https://www.prokuratuur.ee/en/about-prosecutors-office/interesting-facts/procecutors-year

## Workflow
1. Locate relevant annual/statistics publication.
2. Extract comparable indicators across years.
3. Normalize offence and outcome categories.
4. Return trend table with source citations.

## Human setup (when needed)
- If data is only in narrative pages/PDFs, walk user through obtaining files and continue from uploaded documents.

## Quality checks
- Preserve official category labels before any regrouping.
- Keep charge/prosecution/outcome stages separate.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.prokuratuur.ee/en/about-prosecutors-office/interesting-facts/procecutors-year (HTTP 200, text/html;, file links detected: 1)

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
