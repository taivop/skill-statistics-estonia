---
name: medicines-register
description: Query Estonia Medicines Register for medicinal-product records, authorization metadata, and regulatory status context.
---

# Medicines Register

## Use when
- You need medicinal-product registry details and status.
- You need authorization/registration metadata for medicines.

## Avoid when
- You need broad public-health incidence statistics.

## Inputs
- Product name, active substance, authorization holder, or registry ID.

## Outputs
- Structured medicines-register extract and status fields.

## Primary endpoints
- Medicines register: https://www.ravimiregister.ee/

## Workflow
1. Query by product/substance/holder criteria.
2. Extract authorization and status metadata.
3. Normalize identifiers and naming variants.
4. Return structured registry records with source dates.

## Human setup (when needed)
- If interactive filters require manual operation, guide user through the search/export path and continue from shared outputs.

## Quality checks
- Keep official register identifiers untouched.
- Separate active vs withdrawn/suspended statuses.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.ravimiregister.ee/ (HTTP 200, text/html;, file links detected: 0)

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
