---
name: party-funding-data
description: Query ERJK open data and finance report views for Estonian political party funding, revenues, expenditures, and transparency monitoring.
---

# Party Funding Data (ERJK)

## Use when
- You need party revenue/expenditure data and financing transparency records.
- You need reporting-period comparisons across parties.

## Avoid when
- You need party membership totals only.

## Inputs
- Party, period, report type, and grouping dimensions.

## Outputs
- Funding dataset and normalized period-party metrics.

## Primary endpoints
- Open data entry point: https://www.erjk.ee/en/open-data
- Revenue reports view: https://www.erjk.ee/en/financing-reports/revenue-reports?period=show_all&period_to=&party=all&person=&group=111&quarter=&quarter_to=

## Workflow
1. Locate relevant ERJK open-data/report endpoint.
2. Extract party-period financial fields.
3. Normalize party names and reporting periods.
4. Return structured funding table and caveats.

## Human setup (when needed)
- If data export is only available via web controls, guide user through filter/export steps and continue from file.

## Quality checks
- Distinguish revenue vs expenditure streams.
- Preserve source period and report type metadata.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.erjk.ee/en/open-data (HTTP 200, text/html;, file links detected: 0)
- https://www.erjk.ee/en/financing-reports/revenue-reports?period=show_all&period_to=&party=all&person=&group=111&quarter=&quarter_to= (HTTP 200, text/html;, file links detected: 0)

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
