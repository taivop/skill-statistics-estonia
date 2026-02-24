---
name: procurement-review
description: Use Ministry of Finance procurement review pages for public procurement dispute handling, review procedures, and outcome context.
---

# Procurement Review

## Use when
- You need official procurement review procedures or outcomes context.
- You need structured extraction of procurement review materials.

## Avoid when
- You only need tender or award datasets.

## Inputs
- Review topic, period, and case/procedure scope.

## Outputs
- Structured procurement review references and outcome fields.

## Primary endpoints
- Public procurement review: https://www.fin.ee/en/public-procurement-state-aid-and-assets/public-procurement-policy/public-procurement-review

## Workflow
1. Identify relevant procurement review materials/case references.
2. Extract procedure stage and published outcomes.
3. Normalize fields across publication formats.
4. Return structured output with legal-context notes.

## Human setup (when needed)
- If case materials are document-only, guide user through retrieval and continue from files.

## Quality checks
- Keep case/review references unchanged.
- Distinguish procedural guidance from case outcomes.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.fin.ee/en/public-procurement-state-aid-and-assets/public-procurement-policy/public-procurement-review (HTTP 200, text/html;, file links detected: 1)

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
