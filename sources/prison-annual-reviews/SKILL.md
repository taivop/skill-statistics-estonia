---
name: prison-annual-reviews
description: Use prison service annual review publications for institutional performance, population, and operations context.
---

# Prison Annual Reviews

## Use when
- You need prison system annual operational context and indicators.
- You need year-over-year institutional performance summaries.

## Avoid when
- You need individual inmate case data.

## Inputs
- Target years and thematic focus.

## Outputs
- Structured annual indicators and narrative findings.

## Primary endpoints
- Annual reviews: https://www.vangla.ee/meist/uudised-ja-arvud/aasta-ulevaated

## Workflow
1. Retrieve annual review documents/pages for selected years.
2. Extract key metrics and recurring sections.
3. Normalize year-to-year terminology.
4. Return trend summaries and machine-readable tables.

## Human setup (when needed)
- If annual reviews are PDF-only, guide user through download and continue from files.

## Quality checks
- Record exact year and publication edition.
- Separate capacity, population, incidents, and program metrics.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.vangla.ee/meist/uudised-ja-arvud/aasta-ulevaated (HTTP 200, text/html;, file links detected: 1)

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
