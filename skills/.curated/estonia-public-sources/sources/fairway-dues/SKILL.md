---
name: fairway-dues
description: Use fairway dues sources for maritime fee policy, charge structure, and extractable official tariff information.
---

# Fairway Dues

## Use when
- You need official fairway dues policy/tariff context.
- You need structured extraction of dues-related fields.

## Avoid when
- You need broad maritime economy trend data only.

## Inputs
- Vessel/category scope, period, and dues component.

## Outputs
- Structured dues/tariff references and extracted values.

## Primary endpoints
- Fairway dues: https://www.transpordiamet.ee/en/fairway-dues

## Workflow
1. Retrieve dues policy/tariff materials.
2. Extract charge components, exemptions, and period applicability.
3. Normalize tariff units and categories.
4. Return structured output with source references.

## Human setup (when needed)
- If tariff details are in linked docs, guide user through retrieval and continue from files.

## Quality checks
- Keep tariff applicability period explicit.
- Separate statutory basis from derived interpretation.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.transpordiamet.ee/en/fairway-dues (HTTP 200, text/html;, file links detected: 1)

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
