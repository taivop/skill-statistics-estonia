---
name: riigikogu-draft-laws
description: Track Riigikogu draft laws and proceedings status from the parliamentary draft-law portal.
---

# Riigikogu Draft Laws Tracker

## Use when
- You need bill-level progress in parliament.
- You need linked materials (initiators, committee stage, readings).

## Avoid when
- You need voting-level machine API records (use Riigikogu open data API skill).

## Inputs
- Draft number, title, sponsor, or date range.

## Outputs
- Bill status summary and action timeline.

## Primary endpoint
- Draft laws page: https://www.riigikogu.ee/tegevus/eelnoud/

## Workflow
1. Find bill by number/title.
2. Capture stage, committee references, and event dates.
3. Collect linked documents and related proceedings entries.
4. Return machine-friendly status table.

## Human setup (when needed)
- If bill details require manual filtering in UI, walk user through exact filters and ask for target bill URL.

## Quality checks
- Preserve original bill identifiers.
- Distinguish initiated, in process, and concluded statuses.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.riigikogu.ee/tegevus/eelnoud/ (HTTP 200, text/html;, file links detected: 0)

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
