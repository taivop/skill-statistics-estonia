---
name: government-journal-records
description: Query public Government Office journal records for official registry-log style entries and operational trace data.
---

# Government Journal Records

## Use when
- You need central journal-style operational entries.
- You need public records by journal key/registry sequence.

## Avoid when
- You need full document content where only metadata is published.

## Inputs
- Journal key, date range, topic keywords.

## Outputs
- Journal entries with IDs, dates, and summary fields.

## Primary endpoint
- Public journal view: https://dhs.riigikantselei.ee/avalikteave.nsf/byjournalkey?open

## Workflow
1. Query by journal/date/topic.
2. Extract listed record metadata and links.
3. Normalize into tabular event log.
4. Return filtered operational trace.

## Human setup (when needed)
- If navigation depends on dynamic UI controls, guide the user through the exact query steps and continue from the resulting page URL.

## Quality checks
- Keep journal key and entry order.
- Record retrieval timestamp for reproducibility.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://dhs.riigikantselei.ee/avalikteave.nsf/byjournalkey?open (HTTP 200, text/xml, file links detected: 0)

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
