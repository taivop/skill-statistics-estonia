---
name: environmental-charge-statistics
description: Use Environmental Board environmental charge statistics for supervision and environmental-fee related indicator extraction.
---

# Environmental Charge Statistics

## Use when
- You need environmental charge statistics and supervision context.
- You need official environmental fee-related indicators.

## Avoid when
- You need general environmental quality indicators only.

## Inputs
- Charge type, period, and regulated activity scope.

## Outputs
- Structured environmental charge statistics and metadata.

## Primary endpoints
- Environmental charge statistics: https://www.keskkonnaamet.ee/en/supervision-environmental-charge/environmental-charge/statistics

## Workflow
1. Locate charge statistics source tables/publications.
2. Extract periodized indicators and categories.
3. Normalize units and category names.
4. Return trend-ready structured data.

## Human setup (when needed)
- If statistics are document-based, guide user through retrieval and continue from files.

## Quality checks
- Keep charge category definitions with values.
- Distinguish assessed vs collected values when available.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.keskkonnaamet.ee/en/supervision-environmental-charge/environmental-charge/statistics (HTTP 200, text/html;, file links detected: 2)

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
