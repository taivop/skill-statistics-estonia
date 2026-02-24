---
name: open-data
description: Discover and triage Estonian public datasets via andmed.eesti.ee; use for cross-agency dataset discovery, filtering, and routing to source-specific APIs/downloads.
---

# Estonia Open Data Discovery

## Use when
- You need the best dataset source for a topic across agencies.
- You need to identify owner, refresh cadence, and access method.

## Avoid when
- You already have a specific source API and dataset ID.

## Inputs
- Topic and policy/business question.
- Preferred format (API, CSV, GeoJSON, etc.).

## Outputs
- Ranked shortlist of datasets.
- Recommended primary dataset and fallback alternatives.

## Primary endpoints
- Portal: https://andmed.eesti.ee/
- RSS updates: https://andmed.eesti.ee/api/rss/feed

## Workflow
1. Search with both Estonian and English keywords.
2. Collect metadata: owner, update date, coverage, format, license.
3. Keep only machine-usable and recently updated datasets.
4. Return shortlist with direct next step (API call or file download).

## Human setup (when needed)
- If a dataset page requires browser interaction, walk the user through exact clicks and ask them to share the final direct file/API URL.

## Quality checks
- Prefer official publishers and open licenses.
- De-prioritize stale or undocumented datasets.

## Access reality
- Public access type: API or structured endpoint access.
- Verification run: 2026-02-24.
- https://andmed.eesti.ee/ (HTTP 200, text/html, file links detected: 0)
- https://andmed.eesti.ee/api/rss/feed (HTTP 200, application/rss+xml;, file links detected: 0)

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
