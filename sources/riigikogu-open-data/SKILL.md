---
name: riigikogu-open-data
description: Query Riigikogu open data API for parliamentary votings, members, and legislative activity.
---

# Riigikogu Open Data API

## Use when
- You need parliamentary voting and member-level open data.
- You need machine-readable legislative process signals.

## Avoid when
- You need election outcomes (use election archive skill).

## Inputs
- Date range, language, and endpoint family.

## Outputs
- API JSON extract and cleaned analysis tables.

## Primary endpoints
- API root: https://api.riigikogu.ee/
- Swagger: https://api.riigikogu.ee/swagger-ui.html
- Example votings endpoint: `https://api.riigikogu.ee/api/votings?startDate=YYYY-MM-DD&endDate=YYYY-MM-DD&lang=en`

## Workflow
1. Inspect endpoint contract in Swagger.
2. Query bounded date ranges.
3. Normalize IDs, timestamps, and member/vote fields.
4. Return dataset with endpoint and query parameters used.

## Human setup (when needed)
- Usually none.

## Quality checks
- Keep stable IDs for members and votings.
- Store exact query window to ensure reproducibility.

## Access reality
- Public access type: API or structured endpoint access.
- Verification run: 2026-02-24.
- https://api.riigikogu.ee/ (HTTP 200, text/html, file links detected: 0)
- https://api.riigikogu.ee/swagger-ui.html (HTTP 200, text/html, file links detected: 0)
- https://api.riigikogu.ee/api/votings?startDate=YYYY-MM-DD&endDate=YYYY-MM-DD&lang=en` (HTTP 400, text/html;charset=utf-8, file links detected: 0)

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
