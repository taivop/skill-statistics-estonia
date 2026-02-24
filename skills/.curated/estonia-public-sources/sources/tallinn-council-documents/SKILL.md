---
name: tallinn-council-documents
description: Query Tallinn council document system (TEELE) for council acts, drafts, and proceeding documents.
---

# Tallinn Council Documents (TEELE)

## Use when
- You need Tallinn city council acts/drafts/proceeding docs.
- You need operational document flow by publication/submission dates.

## Avoid when
- You only need final legal acts already in Tallinn legal acts register.

## Inputs
- Document type, date range, sort criteria, and filters.

## Outputs
- Council document table with links and metadata.

## Primary endpoints
- Acts endpoint: https://teele.tallinn.ee/documents/council/acts?page=1&pageSize=10&sortColumn=publishedAt&sortDirection=desc
- Drafts endpoint: https://teele.tallinn.ee/documents/council/drafts?tableType=incouncilproceeding&page=1&pageSize=10&sortColumn=documentSubmission.acceptedAt&sortDirection=ASC

## Workflow
1. Query acts/drafts endpoints with bounded pagination.
2. Extract document IDs, publication/submission dates, and status fields.
3. Follow detail links for full document metadata.
4. Return normalized council-doc dataset.

## Human setup (when needed)
- If certain documents are not API-visible and require browser interaction, guide user to open the detail page and share URL.

## Quality checks
- Keep document IDs and source endpoint parameters.
- Distinguish drafts from adopted acts.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://teele.tallinn.ee/documents/council/acts?page=1&pageSize=10&sortColumn=publishedAt&sortDirection=desc (HTTP 200, text/html, file links detected: 0)
- https://teele.tallinn.ee/documents/council/drafts?tableType=incouncilproceeding&page=1&pageSize=10&sortColumn=documentSubmission.acceptedAt&sortDirection=ASC (HTTP 200, text/html, file links detected: 0)

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
