---
name: maritime-economy-statistics
description: Use Transport Administration maritime economy statistics for shipping-sector indicators and maritime operations context.
---

# Maritime Economy Statistics

## Use when
- You need shipping/maritime economy indicators.
- You need official maritime sector operations context.

## Avoid when
- You only need port registry metadata.

## Inputs
- Indicator scope, period, and maritime segment.

## Outputs
- Structured maritime economy indicators dataset.

## Primary endpoints
- Maritime economy statistics: https://www.transpordiamet.ee/en/maritime-and-waterways/bringing-ships-under-estonian-flag/maritime-economy-statistics

## Workflow
1. Locate relevant maritime statistics tables/publications.
2. Extract indicators by period/segment.
3. Normalize category and unit definitions.
4. Return trend-ready structured output.

## Human setup (when needed)
- If indicators are in downloadable reports, guide user through retrieval and continue from files.

## Quality checks
- Preserve metric definitions and units.
- Distinguish fleet, activity, and financial indicators.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.transpordiamet.ee/en/maritime-and-waterways/bringing-ships-under-estonian-flag/maritime-economy-statistics (HTTP 200, text/html;, file links detected: 1)

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
