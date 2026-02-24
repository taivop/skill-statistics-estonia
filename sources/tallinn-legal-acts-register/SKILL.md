---
name: tallinn-legal-acts-register
description: Query Tallinn legal acts register for municipal regulations, orders, and official city legal documents.
---

# Tallinn Legal Acts Register

## Use when
- You need official Tallinn municipal legal acts.
- You need city-level regulation tracking and reference links.

## Avoid when
- You need broader national legal corpus only.

## Inputs
- Legal act keywords, type, issuing body, date range.

## Outputs
- Tallinn legal acts dataset with citations.

## Primary endpoint
- Register: https://oigusaktid.tallinn.ee/

## Workflow
1. Search acts by topic/type/date.
2. Capture identifiers, dates, and validity metadata.
3. Extract links to full act text.
4. Return structured act list.

## Human setup (when needed)
- If results are only browsable via UI widgets, guide user through exact search and have them share the resulting filtered URL.

## Quality checks
- Preserve act identifier and effective date.
- Separate current and repealed acts.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://oigusaktid.tallinn.ee/ (HTTP 200, text/html, file links detected: 0)

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
