---
name: labour-inspectorate-statistics
description: Use Labour Inspectorate statistics publications for workplace safety, labour compliance, and inspection trend analysis.
---

# Labour Inspectorate Statistics

## Use when
- You need official labour inspection/safety statistics.
- You need trend context for workplace violations or incidents.

## Avoid when
- You need individual case-level confidential files.

## Inputs
- Period, sector, region, and indicator scope.

## Outputs
- Structured labour-inspection statistics dataset.

## Primary endpoints
- Statistics page: https://www.tooinspektsioon.ee/asutus-uudised-ja-kontaktid/kontakt/statistika

## Workflow
1. Locate relevant statistics publication/table.
2. Extract periodized indicators and categories.
3. Normalize labels, units, and dimensions.
4. Return analysis-ready dataset with source notes.

## Human setup (when needed)
- If data is in downloadable documents only, guide user through download and continue from files.

## Quality checks
- Keep incident/inspection/enforcement metrics separate.
- Preserve official category names before regrouping.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.tooinspektsioon.ee/asutus-uudised-ja-kontaktid/kontakt/statistika (HTTP 200, text/html;, file links detected: 1)

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
