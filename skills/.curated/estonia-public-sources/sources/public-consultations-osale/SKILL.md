---
name: public-consultations-osale
description: Track public policy consultations on OSALE, including consultation lifecycle, documents, and participation windows.
---

# Public Consultations (OSALE)

## Use when
- You need active or historical policy consultations.
- You need consultation-level documents, deadlines, and status.

## Avoid when
- You need enacted policy outcomes only.

## Inputs
- Topic keywords, ministry/policy area, date range.

## Outputs
- Consultation list with status, deadlines, and links.

## Primary endpoint
- OSALE share/home: https://www.osale.ee/main/mount/share/home

## Workflow
1. Search consultations by keyword/area.
2. Extract title, institution, dates, and stage.
3. Capture linked consultation docs.
4. Return timeline and current status summary.

## Human setup (when needed)
- If OSALE search UI blocks deep links, walk the user through filters and have them share resulting consultation URLs.

## Quality checks
- Keep open/closed status explicit.
- Preserve deadlines and publication dates exactly.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.osale.ee/main/mount/share/home (HTTP 200, text/html;charset=UTF-8, file links detected: 0)

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
