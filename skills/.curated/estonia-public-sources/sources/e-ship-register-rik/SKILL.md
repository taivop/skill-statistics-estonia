---
name: e-ship-register-rik
description: Use RIK e-ship register service context for registry workflow guidance and extraction of publicly accessible register evidence.
---

# E-Ship Register (RIK)

## Use when
- You need RIK e-ship register workflow context.
- You need structured outputs from publicly available register views.

## Avoid when
- You only need Transport Administration ship-register publications.

## Inputs
- Vessel/query scope and allowed identifiers.

## Outputs
- Structured e-ship register outputs with provenance.

## Primary endpoints
- E-ship register: https://www.rik.ee/en/other-services/e-ship-register

## Workflow
1. Determine accessible register route and lookup parameters.
2. Extract available vessel/register fields.
3. Normalize identifiers and statuses.
4. Return structured dataset and limitations.

## Human setup (when needed)
- If register access is authenticated/UI-driven, guide user through the process and continue from exported/copied results.

## Quality checks
- Keep source system and retrieval route explicit.
- Preserve original register references.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.rik.ee/en/other-services/e-ship-register (HTTP 200, text/html;, file links detected: 0)

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
