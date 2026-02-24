---
name: public-finance-data
description: Analyze Estonian state finance transparency data from RiigiRaha for budget, spending, and public-sector financial overviews.
---

# Estonia Public Finance Data (RiigiRaha)

## Use when
- You need budget and expenditure transparency data.
- You need ministry/program-level public finance context.

## Avoid when
- You need tax administration microdata (use EMTA-oriented skill).

## Inputs
- Institution/program scope and period.

## Outputs
- Finance dataset extract and metric definitions used.

## Primary endpoint
- Portal: https://riigiraha.fin.ee/

## Workflow
1. Identify target dashboard section and metric definition.
2. Export available table view to machine-readable format.
3. Standardize codes, units, and period labels.
4. Return extract with clear interpretation notes.

## Human setup (when needed)
- RiigiRaha is UI-heavy; if direct API is unavailable, walk the user through exact export clicks and continue from the downloaded file.

## Quality checks
- Distinguish budgeted vs executed values.
- Preserve institution hierarchy codes when present.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://riigiraha.fin.ee/ (HTTP 200, text/html;, file links detected: 0)

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
