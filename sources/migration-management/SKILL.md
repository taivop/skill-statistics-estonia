---
name: migration-management
description: Use Ministry of Interior migration management pages for official policy/operations context and extractable migration-process information.
---

# Migration Management

## Use when
- You need official migration management process context.
- You need structured extraction from public migration-policy/operations materials.

## Avoid when
- You need person-level migration case files.

## Inputs
- Migration topic, period, and process scope.

## Outputs
- Structured migration-management references and indicators (when published).

## Primary endpoints
- Migration area: https://www.siseministeerium.ee/en/activities/efficient-population-management/migration
- Population management context: https://www.siseministeerium.ee/en/activities/efficient-population-management

## Workflow
1. Identify relevant migration policy/process materials.
2. Extract operationally useful fields/indicators.
3. Normalize topic categories and periods.
4. Return structured outputs with source citations.

## Human setup (when needed)
- If key data is only in linked publications, guide user through retrieval and continue from provided documents.

## Quality checks
- Distinguish policy statements from measurable indicators.
- Keep publication date for every extracted item.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.siseministeerium.ee/en/activities/efficient-population-management/migration (HTTP 200, text/html;, file links detected: 4)
- https://www.siseministeerium.ee/en/activities/efficient-population-management (HTTP 404, text/html;, file links detected: 1)

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
