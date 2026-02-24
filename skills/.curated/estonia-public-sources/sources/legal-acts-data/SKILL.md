---
name: legal-acts-data
description: Query Riigi Teataja legal acts API and related endpoints for Estonian legislation search, retrieval, and legal text linking.
---

# Estonia Legal Acts Data (Riigi Teataja)

## Use when
- You need official legal acts, metadata, and structured legal search.
- You need regulation references for compliance-aware analysis.

## Avoid when
- You only need plain-language summaries without legal text retrieval.

## Inputs
- Query terms, legal act type, effective-date constraints.

## Outputs
- Legal search results and retrieved act links/text references.

## Primary endpoints
- Portal: https://www.riigiteataja.ee/
- Search API example: `https://www.riigiteataja.ee/api/oigusakt_otsing/1/otsi?leht=1`

## Workflow
1. Query legal acts API with relevant search filters.
2. Parse results and capture `url`/ID fields.
3. Fetch referenced act representations as needed.
4. Return legal dataset with citation-ready links.

## Human setup (when needed)
- Usually none.

## Quality checks
- Distinguish current vs historical validity periods.
- Preserve original legal identifiers and publication context.

## Access reality
- Public access type: API or structured endpoint access.
- Verification run: 2026-02-24.
- https://www.riigiteataja.ee/ (HTTP 200, text/html;charset=UTF-8, file links detected: 2)
- https://www.riigiteataja.ee/api/oigusakt_otsing/1/otsi?leht=1` (HTTP 400, text/html;charset=utf-8, file links detected: 0)

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
