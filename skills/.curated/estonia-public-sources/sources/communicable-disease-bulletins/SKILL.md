---
name: communicable-disease-bulletins
description: Use Health Board communicable disease bulletins for outbreak, surveillance, and public-health operations indicators.
---

# Communicable Disease Bulletins

## Use when
- You need infectious disease surveillance bulletins and trend indicators.
- You need official public-health operational context.

## Avoid when
- You need healthcare financing indicators.

## Inputs
- Disease group, period, and geographic scope.

## Outputs
- Structured bulletin-derived disease indicators and metadata.

## Primary endpoints
- Bulletins: https://www.terviseamet.ee/en/communicable-diseases/statistics/communicable-disease-bulletins

## Workflow
1. Retrieve relevant bulletin files/pages.
2. Extract disease indicators by period/location.
3. Normalize disease names and units.
4. Return structured dataset with bulletin references.

## Human setup (when needed)
- If indicators are only in downloadable bulletins, guide user through retrieval and continue from files.

## Quality checks
- Keep disease taxonomy and case definitions with values.
- Distinguish provisional from finalized counts.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.terviseamet.ee/en/communicable-diseases/statistics/communicable-disease-bulletins (HTTP 200, text/html;, file links detected: 26)

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
