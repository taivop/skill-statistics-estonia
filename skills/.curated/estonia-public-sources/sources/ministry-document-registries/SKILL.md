---
name: ministry-document-registries
description: Query Estonia's official ministry and agency document registries (ADR network) for operational records, incoming/outgoing documents, and workflow traceability.
---

# Ministry Document Registries

## Use when
- You need official document-level operational records from ministries/agencies.
- You need a trace of administrative workflow (registration, correspondence, routing).

## Avoid when
- You need enacted legal texts only.

## Inputs
- Institution, date range, document keywords, registry identifiers.

## Outputs
- Registry search results with document metadata and source links.

## Primary endpoints
- ADR network root: https://adr.rik.ee/
- RIK agency document register: https://www.rik.ee/en/agency/document-register

## Workflow
1. Identify target institution's registry from ADR network.
2. Query by keyword/date/document number.
3. Include RIK agency document register where institution context requires it.
4. Extract core metadata (registry number, dates, sender/recipient, subject).
5. Return normalized records and links.

## Human setup (when needed)
- ADR pages are often UI-first. Walk the user through selecting the institution and entering filters, then ask for the resulting search URL or exported file and continue.

## Quality checks
- Keep original registry identifiers unchanged.
- Separate incoming vs outgoing records where provided.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://adr.rik.ee/ (HTTP 200, text/html, file links detected: 0)
- https://www.rik.ee/en/agency/document-register (HTTP 200, text/html;, file links detected: 0)

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
