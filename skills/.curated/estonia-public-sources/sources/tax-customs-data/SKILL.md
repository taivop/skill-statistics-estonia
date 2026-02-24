---
name: tax-customs-data
description: Retrieve and use Estonian Tax and Customs Board public statistics and open-data files for tax and trade related analyses.
---

# Estonia Tax and Customs Data

## Use when
- You need official tax/customs statistics from EMTA.
- You need downloadable open files for reproducible analysis.

## Avoid when
- You need confidential taxpayer-level data.

## Inputs
- Indicator/topic and period.

## Outputs
- Downloaded file(s), cleaned dataset, and field mapping.

## Primary endpoints
- Statistics page: https://www.emta.ee/en/business-client/statistics-and-open-data
- Example direct files:
  - `https://ncfailid.emta.ee/s/e4DneiWeKFfje6d/download/tasutud_maksud_kaesolev_aasta_eng.csv`
  - `https://ncfailid.emta.ee/s/K8snLYNdZnqJCRn/download/tasutud_maksud_varasemad_aastad_eng.csv`

## Workflow
1. Start from EMTA statistics page and pick current/prior period file.
2. Download CSV/XLSX and verify delimiter/encoding.
3. Normalize column names and date formats.
4. Return cleaned table with explicit source URL.

## Human setup (when needed)
- If a file is gated or moved, ask the user to open the EMTA page and share the latest direct link; then continue automatically.

## Quality checks
- Check language-specific column names.
- Verify whether figures are cumulative or period-specific.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.emta.ee/en/business-client/statistics-and-open-data (HTTP 200, text/html;, file links detected: 5)
- https://ncfailid.emta.ee/s/e4DneiWeKFfje6d/download/tasutud_maksud_kaesolev_aasta_eng.csv` (HTTP 200, text/csv;charset=UTF-8, file links detected: 0)
- https://ncfailid.emta.ee/s/K8snLYNdZnqJCRn/download/tasutud_maksud_varasemad_aastad_eng.csv` (HTTP 200, text/csv;charset=UTF-8, file links detected: 0)

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
