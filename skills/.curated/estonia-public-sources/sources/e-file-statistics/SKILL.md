---
name: e-file-statistics
description: Use RIK e-File statistics environment for public case-flow and procedural trend indicators across justice workflows.
---

# E-File Statistics

## Use when
- You need justice process statistics from the e-File environment.
- You need case-flow trend context across courts/procedure types.

## Avoid when
- You need case documents or party-level records.

## Inputs
- Procedure type, time period, and metric scope.

## Outputs
- Structured justice-process statistics with source metadata.

## Primary endpoints
- Statistics environment: https://www.rik.ee/en/e-file/statistics-environment

## Workflow
1. Open the statistics environment and identify relevant indicators.
2. Filter by period/procedure dimensions.
3. Extract values and normalize labels/units.
4. Return trend-ready dataset and caveats.

## Human setup (when needed)
- If indicators are only visible in interactive charts, guide the user through export/copy steps and continue from provided files.

## Quality checks
- Keep original metric definitions and period granularity.
- Separate counts, durations, and rate metrics.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.rik.ee/en/e-file/statistics-environment (HTTP 200, text/html;, file links detected: 1)

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
