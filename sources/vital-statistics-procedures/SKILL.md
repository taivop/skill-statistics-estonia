---
name: vital-statistics-procedures
description: Use Ministry of Interior vital statistics procedures pages for official civil-registration process context and structured policy extraction.
---

# Vital Statistics Procedures

## Use when
- You need official civil/vital-statistics procedural context.
- You need structured extraction from published procedure materials.

## Avoid when
- You need person-level registry data.

## Inputs
- Procedure topic, legal context, and period.

## Outputs
- Structured procedure references, responsibilities, and workflow notes.

## Primary endpoints
- Vital statistics procedures: https://www.siseministeerium.ee/en/activities/population-procedures/vital-statistics-procedures

## Workflow
1. Locate relevant procedure/legal guidance pages.
2. Extract process steps, roles, and official references.
3. Normalize terminology across documents.
4. Return structured process map with citations.

## Human setup (when needed)
- If procedures reference external forms/registries, guide user through obtaining those materials and continue from them.

## Quality checks
- Keep process/legal references linked to each step.
- Separate administrative procedure from statistical outputs.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.siseministeerium.ee/en/activities/population-procedures/vital-statistics-procedures (HTTP 200, text/html;, file links detected: 1)

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
