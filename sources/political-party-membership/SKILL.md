---
name: political-party-membership
description: Analyze Estonian political party membership trends using official Business Register party statistics and related public records.
---

# Political Party Membership Analysis

## Use when
- You need party membership trend context by party and period.
- You need official organization-level party statistics.

## Avoid when
- You need campaign finance flows (use ERJK funding skill).

## Inputs
- Party scope and analysis period.

## Outputs
- Membership trend dataset and summary indicators.

## Primary endpoint
- Party statistics page: https://ariregister.rik.ee/eng/statistics/political_parties

## Workflow
1. Retrieve party statistics for selected periods.
2. Extract membership-related fields.
3. Harmonize party naming and period labels.
4. Return trend-ready table and interpretation notes.

## Human setup (when needed)
- If tables require manual download, walk user through exact clicks and continue from exported file.

## Quality checks
- Preserve official party identifiers where available.
- Clearly mark whether counts are point-in-time or annual summaries.

## Access reality
- Public access type: Public webpage/document extraction.
- Verification run: 2026-02-24.
- https://ariregister.rik.ee/eng/statistics/political_parties (HTTP 200, text/html;, file links detected: 0)

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
