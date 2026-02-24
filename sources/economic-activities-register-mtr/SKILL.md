---
name: economic-activities-register-mtr
description: Query Estonia Economic Activities Register (MTR) for licensed activity records, operator details, and sector-specific authorization context.
---

# Economic Activities Register (MTR)

## Use when
- You need operator/license information from MTR.
- You need activity-authorization context by sector.

## Avoid when
- You only need broad business population snapshots.

## Inputs
- Company identifier, activity class, sector, and time scope.

## Outputs
- MTR activity-license records and normalized fields.

## Primary endpoints
- Register portal: https://mtr.ttja.ee/

## Workflow
1. Select relevant search view in MTR.
2. Filter by entity/activity class/time.
3. Extract registration, status, and authorization details.
4. Return structured table with status semantics.

## Human setup (when needed)
- If export is UI-only, walk the user through exact filters and export actions, then continue from the provided file.

## Quality checks
- Preserve original MTR reference identifiers.
- Distinguish active, suspended, and terminated records.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://mtr.ttja.ee/ (HTTP 200, text/html;, file links detected: 0)

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
