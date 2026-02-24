---
name: public-sector-it-systems-riha
description: Query RIHA information-systems registry for official metadata about Estonian public-sector IT systems, owners, and integration context.
---

# Public-Sector IT Systems (RIHA)

## Use when
- You need official registry metadata on state information systems.
- You need system-owner and interoperability context.

## Avoid when
- You need runtime operational logs rather than registry metadata.

## Inputs
- System keywords, institution, domain.

## Outputs
- RIHA system metadata list with links.

## Primary endpoint
- Search page: https://riha.eesti.ee/riha/main/infSystem/search

## Workflow
1. Search systems by institution/topic.
2. Extract system name, owner, purpose, and status metadata.
3. Capture links to related documentation where available.
4. Return normalized catalog table.

## Human setup (when needed)
- If detailed records require manual expansion, guide user through selecting records and sharing links/screenshots.

## Quality checks
- Preserve unique system IDs and owner fields.
- Separate active vs historical/deprecated records.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://riha.eesti.ee/riha/main/infSystem/search (HTTP 200, text/html;charset=UTF-8, file links detected: 0)

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
