---
name: local-council-volis
description: Use VOLIS municipal council information system for local council agendas, decisions, minutes, and voting records.
---

# Local Council Data (VOLIS)

## Use when
- You need municipal council operations (agendas, decisions, minutes, votes).
- You need cross-municipality council data where available in VOLIS.

## Avoid when
- You need city-specific systems that are outside VOLIS.

## Inputs
- Municipality, period, and document type.

## Outputs
- Council operation records with links and metadata.

## Primary endpoint
- VOLIS: https://www.volis.ee/

## Workflow
1. Select municipality and document area.
2. Filter by date/document type.
3. Extract decision/minute/agenda records.
4. Return normalized local-governance dataset.

## Human setup (when needed)
- VOLIS is UI-first; guide user through municipality and filter selection when direct machine endpoint is unavailable.

## Quality checks
- Keep municipality identifiers and document IDs.
- Do not mix draft and final decisions unless explicitly labeled.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.volis.ee/ (HTTP 200, text/html;charset=utf-8, file links detected: 0)

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
