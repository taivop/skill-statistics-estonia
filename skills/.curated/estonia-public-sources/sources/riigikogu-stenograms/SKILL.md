---
name: riigikogu-stenograms
description: Retrieve and analyze Riigikogu stenograms (parliamentary transcripts) for meeting-level and speaker-level operational records.
---

# Riigikogu Stenograms

## Use when
- You need official transcript text of sessions.
- You need speaker/date-based extraction from parliamentary debates.

## Avoid when
- You only need aggregate vote counts.

## Inputs
- Session date range, topic keywords, speaker names.

## Outputs
- Stenogram links and extracted text segments with citations.

## Primary endpoint
- Stenograms page: https://www.riigikogu.ee/tegevus/stenogrammid/

## Workflow
1. Locate target sessions by date/keyword.
2. Open stenogram entries and extract relevant passages.
3. Normalize metadata (date, sitting, speaker, segment).
4. Return evidence table with source links.

## Human setup (when needed)
- If content requires UI navigation only, guide the user to open the session page and share the exact link.

## Quality checks
- Keep direct links to transcript source pages.
- Attribute every extracted statement to session date and speaker.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.riigikogu.ee/tegevus/stenogrammid/ (HTTP 200, text/html;charset=UTF-8, file links detected: 0)

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
