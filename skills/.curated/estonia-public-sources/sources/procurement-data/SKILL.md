---
name: procurement-data
description: Analyze Estonian public procurement register data for tenders, contracts, and buyer-supplier market patterns.
---

# Estonia Procurement Data

## Use when
- You need public tender/contract activity by buyer, supplier, or sector.
- You need procurement trend or concentration analysis.
- You need tender pipeline and award monitoring from the procurement register.

## Avoid when
- You need broader budget-level reporting without tender detail.

## Inputs
- Time range, authority/buyer scope, and procedure type.

## Outputs
- Extracted procurement records and aggregation-ready fields.

## Primary endpoint
- Register: https://www.riigihanked.riik.ee/rhr-web/

## Workflow
1. Locate relevant procurement report/search view.
2. Filter by period and category.
3. Export available results and normalize entity names/IDs.
4. Build summary tables (count, value, concentration, repeat winners).

## Human setup (when needed)
- If export requires login or anti-bot interaction, walk the user through login/export steps and continue from provided files.

## Quality checks
- Separate notices, awards, and amendments.
- Track whether values are estimated or awarded.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.riigihanked.riik.ee/rhr-web/ (HTTP 200, text/html, file links detected: 0)

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
