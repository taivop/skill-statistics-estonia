---
name: cultural-heritage-register
description: Query National Register of Cultural Monuments for protected heritage objects, status metadata, and historical protection context.
---

# Cultural Heritage Register

## Use when
- You need official records of protected cultural heritage objects.
- You need protection-status and location metadata.

## Avoid when
- You need modern land-use planning decisions only.

## Inputs
- Object name, type, location, registry identifier, and period.

## Outputs
- Heritage-register extract with object-level protection metadata.

## Primary endpoints
- Register portal: https://register.muinas.ee/

## Workflow
1. Search heritage register by object/location/type.
2. Extract registry IDs, protection status, and descriptive fields.
3. Normalize object types and location labels.
4. Return structured records with provenance.

## Human setup (when needed)
- If bot-protection blocks automated access, guide user through manual search/export and continue from provided files/results.

## Quality checks
- Preserve official monument identifiers.
- Record data-access method used (direct fetch vs manual export).

## Limitations
- Automated access may intermittently trigger anti-bot controls; use manual fallback when needed.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://register.muinas.ee/ (HTTP 200, text/html;, file links detected: 0)

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
