---
name: government-office-document-register
description: Query the Government Office document register for official central-government document records and administrative traceability.
---

# Government Office Document Register

## Use when
- You need Government Office (Riigikantselei) document records.
- You need central-government correspondence and process references.

## Avoid when
- You need only policy outcomes, not record-level documents.

## Inputs
- Keywords, date range, record number, topic.

## Outputs
- Document-register result set with metadata and links.

## Primary endpoint
- Register page: https://www.riigikantselei.ee/asutus-uudised-ja-kontakt/dokumendiregister

## Workflow
1. Open document register page and locate search entry point.
2. Run focused query by date and keyword.
3. Extract identifiers, dates, and titles.
4. Return structured records with source links.

## Human setup (when needed)
- If the register opens in a UI module without deep-linkable queries, guide the user click-by-click and continue from screenshots/exports or shared links.

## Quality checks
- Preserve official document numbers.
- Record exact publication/registration dates.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.riigikantselei.ee/asutus-uudised-ja-kontakt/dokumendiregister (HTTP 200, text/html;, file links detected: 1)

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
