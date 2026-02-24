---
name: official-notices
description: Query Ametlikud Teadaanded official notices for public announcements, summons, insolvency, and statutory publication workflows.
---

# Estonia Official Notices

## Use when
- You need official publication notices and statutory announcements.
- You need organization/person/process-level notice tracking.

## Avoid when
- You need detailed court-case documents beyond notice publication.

## Inputs
- Notice type, party/entity name, date range.

## Outputs
- Notice list with publication metadata and links.

## Primary endpoint
- URI search: https://www.ametlikudteadaanded.ee/avalik/uriotsing

## Workflow
1. Search by entity/name/type/date.
2. Open notice entries and capture publication fields.
3. Normalize notice type and status for analysis.
4. Return structured notice dataset.

## Human setup (when needed)
- If query flow requires interactive form inputs/captcha, guide user step-by-step and continue from resulting notice links.

## Quality checks
- Preserve publication date and notice category exactly.
- Distinguish notices from underlying legal actions.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.ametlikudteadaanded.ee/avalik/uriotsing (HTTP 200, text/html;, file links detected: 1)

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
