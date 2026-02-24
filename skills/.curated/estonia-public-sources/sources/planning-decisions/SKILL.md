---
name: planning-decisions
description: Query national planning register for spatial planning decisions, planning process stages, and plan document records.
---

# Estonia Planning Decisions

## Use when
- You need plan lifecycle data (initiated, approved, in force, etc.).
- You need planning decision records by municipality/region.

## Avoid when
- You need only base geospatial layers.

## Inputs
- Planning type, location, and date range.

## Outputs
- Planning records with stage/status and document links.

## Primary endpoint
- Planning register: https://www.planeeringud.ee/

## Workflow
1. Search planning records by location/type.
2. Capture plan identifiers, responsible authority, and stages.
3. Extract linked documents and decision references.
4. Return normalized planning-process dataset.

## Human setup (when needed)
- If export is UI-only, guide user through exact filters and export/download actions.

## Quality checks
- Preserve plan IDs and stage timestamps.
- Clearly separate draft/planned vs approved/in-force plans.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.planeeringud.ee/ (HTTP 200, text/html;charset=ISO-8859-1, file links detected: 0)

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
