---
name: rescue-incident-data
description: Query Rescue Board statistics pages for emergency incidents, response activity, and operational risk context.
---

# Rescue Incident Data

## Use when
- You need incident/response statistics from Rescue Board publications.
- You need operational emergency trend context.

## Avoid when
- You need police criminal-case data.

## Inputs
- Incident type, region, and time window.

## Outputs
- Incident-response statistics dataset and summary indicators.

## Primary endpoints
- Rescue Board statistics: https://www.rescue.ee/et/statistika

## Workflow
1. Locate relevant incident statistics publication/dashboard.
2. Extract period, region, and incident-type metrics.
3. Normalize category labels for consistent comparison.
4. Return trend-ready table with source annotations.

## Human setup (when needed)
- If data is chart-only or embedded in downloadable reports, guide user through export/copy steps and continue from provided files.

## Quality checks
- Keep incident-category definitions with extracted values.
- Separate incident counts from response-time metrics.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.rescue.ee/et/statistika (HTTP 200, text/html, file links detected: 1)

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
