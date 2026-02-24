---
name: financial-supervision-decisions
description: Query financial supervision decision-related publications, including court decisions tied to supervisory activities.
---

# Financial Supervision Decisions

## Use when
- You need supervisory/court decision context in financial regulation.
- You need enforcement-related outcome references.

## Avoid when
- You need market statistics rather than supervisory outcomes.

## Inputs
- Institution/entity, decision topic, period.

## Outputs
- Decision/publication list with links and metadata.

## Primary endpoint
- Court decisions page: https://www.fi.ee/en/court-decisions-related-supervision-activities

## Workflow
1. Collect decision entries and linked court-register references.
2. Extract dates, case/subject metadata.
3. Normalize for timeline analysis.
4. Return structured supervisory-outcomes dataset.

## Human setup (when needed)
- If details require following external court links manually, walk user through and continue from those URLs.

## Quality checks
- Distinguish supervisory actions from court outcomes.
- Preserve case/decision identifiers as published.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://www.fi.ee/en/court-decisions-related-supervision-activities (HTTP 200, text/html;, file links detected: 0)

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
