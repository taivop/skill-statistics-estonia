---
name: tartu-document-register
description: Query Tartu city document register (DHS) for municipal document workflow, records, and operational traceability.
---

# Tartu Document Register (DHS)

## Use when
- You need Tartu municipal document-level operational records.
- You need incoming/outgoing document and workflow references.

## Avoid when
- You only need legal acts (use Tartu WebAktid skill).

## Inputs
- Document keywords, departments, date range.

## Outputs
- Document register extract and metadata mapping.

## Primary endpoint
- DHS register: https://info.raad.tartu.ee/dhs.nsf

## Workflow
1. Search register by keyword/date/department.
2. Capture document references, dates, and status fields.
3. Normalize metadata for analysis.
4. Return structured register table.

## Human setup (when needed)
- If register navigation is manual-only, walk user through exact search form entries and ask for result links.

## Quality checks
- Preserve document reference numbers exactly.
- Keep published status as-is; do not infer confidentiality flags.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://info.raad.tartu.ee/dhs.nsf (HTTP 200, text/html;, file links detected: 0)

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
