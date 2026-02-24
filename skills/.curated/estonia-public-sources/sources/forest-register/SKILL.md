---
name: forest-register
description: Use official forest register for forestry records, forest-unit context, and governance-relevant registry extraction.
---

# Forest Register

## Use when
- You need official forestry register records or metadata.
- You need forest-unit level context for governance/environment workflows.

## Avoid when
- You only need general environmental indicators.

## Inputs
- Forest area/unit identifier, location scope, and period.

## Outputs
- Structured forest register extract with provenance.

## Primary endpoints
- Forest register: https://register.metsad.ee/

## Workflow
1. Identify lookup mode and target forest unit/area.
2. Extract available registry attributes.
3. Normalize location and classification fields.
4. Return structured dataset and caveats.

## Human setup (when needed)
- If interactive map/portal controls block direct extraction, guide user through export/copy steps and continue from provided files.

## Quality checks
- Preserve official unit identifiers and classes.
- Record retrieval date and source view.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://register.metsad.ee/ (HTTP 200, text/html, file links detected: 1)

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
