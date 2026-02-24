---
name: tartu-webaktid
description: Use Tartu WebAktid register for city legal acts and official municipal decision records.
---

# Tartu WebAktid

## Use when
- You need Tartu city legal acts and municipal legal decisions.

## Avoid when
- You need broader Tartu document workflow metadata outside legal acts.

## Inputs
- Act keywords, type, period.

## Outputs
- Tartu legal-act records with links/metadata.

## Primary endpoint
- WebAktid: https://info.raad.tartu.ee/webaktid.nsf

## Workflow
1. Search WebAktid by keywords/type/date.
2. Extract act metadata and document links.
3. Standardize identifiers and dates.
4. Return legal-acts table for analysis.

## Human setup (when needed)
- If UI requires manual query forms, guide user through exact form inputs and continue from result links.

## Quality checks
- Preserve original Tartu act identifiers.
- Keep validity/effective dates when published.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://info.raad.tartu.ee/webaktid.nsf (HTTP 200, text/html;, file links detected: 0)

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
