---
name: education-data
description: Query HaridusSilm education indicators for school system, outcomes, staffing, and regional education analysis in Estonia.
---

# Estonia Education Data (HaridusSilm)

## Use when
- You need education-system indicators by level, region, or institution.
- You need dashboard data exports for analysis.

## Avoid when
- You need student-level data (not public).

## Inputs
- Topic, education level, geography, and period.

## Outputs
- Education indicator extracts and metadata notes.

## Primary endpoint
- Portal: https://www.haridussilm.ee/ee/avaleht

## Workflow
1. Navigate to relevant indicator view.
2. Apply filters and choose comparable slices.
3. Export available table data.
4. Normalize field names and period keys.

## Human setup (when needed)
- If data is only exportable via UI interactions, walk the user through precise filter and export steps.

## Quality checks
- Confirm definitions (e.g., completion vs participation).
- Check whether figures represent school year or calendar year.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.haridussilm.ee/ee/avaleht (HTTP 200, text/html, file links detected: 0)

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
