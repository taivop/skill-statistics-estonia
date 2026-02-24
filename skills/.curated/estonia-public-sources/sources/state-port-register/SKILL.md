---
name: state-port-register
description: Use state port register sources for official port registry information and maritime infrastructure governance context.
---

# State Port Register

## Use when
- You need official state port registry context and records.
- You need structured port-level governance metadata.

## Avoid when
- You need ship-level register entries only.

## Inputs
- Port name, region, and record scope.

## Outputs
- Structured port registry extract and metadata.

## Primary endpoints
- State port register context: https://www.transpordiamet.ee/en/roads-waterways-airspace/ports/state-port-register
- State port register system: https://www.sadamaregister.ee/

## Workflow
1. Identify applicable port register entry/listing (policy page or `sadamaregister.ee`).
2. Extract core port fields and statuses.
3. Normalize port naming and location fields.
4. Return structured registry dataset.

## Human setup (when needed)
- If the register requires interactive search/export, guide user through exact actions and continue from provided results.

## Quality checks
- Preserve official port identifiers where available.
- Record data retrieval date and source endpoint.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.transpordiamet.ee/en/roads-waterways-airspace/ports/state-port-register (HTTP 200, text/html;, file links detected: 1)
- https://www.sadamaregister.ee/ (HTTP 200, text/html;, file links detected: 0)

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
