---
name: health-statistics
description: Query Estonia Health Statistics database (TAI) for official health indicators, outcomes, and utilization metrics.
---

# Estonia Health Statistics (TAI)

## Use when
- You need official health indicators from TAI statistics database.
- You need demographic or service-utilization breakdowns.

## Avoid when
- You need patient-level records (not public).

## Inputs
- Indicator topic, geography, demographic cuts, and period.

## Outputs
- Extracted health indicator table with definitions.

## Primary endpoint
- Database: https://statistika.tai.ee/

## Workflow
1. Locate indicator table and dimensions.
2. Apply filters in the query interface.
3. Export to machine-readable format.
4. Clean labels and produce analysis-ready table.

## Human setup (when needed)
- If export is browser-only, guide user through exact menu/filter/export actions and continue from the downloaded file.

## Quality checks
- Confirm denominator/population base for rates.
- Note methodology revisions and breaks in series.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://statistika.tai.ee/ (HTTP 200, text/html;, file links detected: 0)

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
