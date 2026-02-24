---
name: court-system-statistics
description: Query Estonian court-system statistics and annual reporting pages for caseload, throughput, and procedural performance indicators.
---

# Court System Statistics

## Use when
- You need official court caseload/performance indicators.
- You need annual trend context for court operations.

## Avoid when
- You need case-level judgments text (use court/judgment skills).

## Inputs
- Court level, case type, period, and metric scope.

## Outputs
- Court-statistics dataset with period/court-level dimensions.

## Primary endpoints
- Court system statistics: https://www.kohus.ee/eesti-kohtud/kohtute-menetlusstatistika
- Court yearbook context: https://www.kohus.ee/eesti-kohtud/huvitavat-kohtutest/kohtute-aastaraamat

## Workflow
1. Select statistics/yearbook source by metric needed.
2. Extract periodized indicators by court/case type.
3. Normalize metric names and units.
4. Return structured dataset and trend-ready output.

## Human setup (when needed)
- If indicators are presented in embedded dashboards or PDF-only reports, guide the user through export/download and continue from supplied files.

## Quality checks
- Keep court-level hierarchy explicit.
- Distinguish workload, duration, and outcome metrics.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.kohus.ee/eesti-kohtud/kohtute-menetlusstatistika (HTTP 200, text/html;, file links detected: 0)
- https://www.kohus.ee/eesti-kohtud/huvitavat-kohtutest/kohtute-aastaraamat (HTTP 200, text/html;, file links detected: 0)

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
