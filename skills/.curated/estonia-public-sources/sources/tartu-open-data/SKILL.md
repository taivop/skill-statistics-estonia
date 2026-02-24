---
name: tartu-open-data
description: Locate and use Tartu city open datasets via Tartu open data page and national portal organization listings.
---

# Tartu Open Data

## Use when
- You need Tartu municipal datasets.
- You need organization-scoped discovery for Tartu city data.

## Avoid when
- You need Tallinn-specific direct API querying.

## Inputs
- Topic and desired dataset granularity.

## Outputs
- Tartu dataset shortlist with direct data links.

## Primary endpoints
- City open data page: https://www.tartu.ee/en/open-data
- Organization discovery on national portal: https://andmed.eesti.ee/en/search?organization=tartu-linnavalitsus

## Workflow
1. Start from Tartu open data page and collect linked catalog references.
2. Discover Tartu-owned datasets on the national portal.
3. Select datasets with machine-readable access and recent updates.
4. Return prioritized list with concrete extraction steps.

## Human setup (when needed)
- If a dataset is only downloadable via browser flow, provide precise click path and request the downloaded file for continuation.

## Quality checks
- Confirm dataset owner is Tartu city (or clearly linked municipal entity).
- Keep source URL and refresh date in final metadata.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.tartu.ee/en/open-data (HTTP 200, text/html;, file links detected: 0)
- https://andmed.eesti.ee/en/search?organization=tartu-linnavalitsus (HTTP 200, text/html, file links detected: 0)

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
