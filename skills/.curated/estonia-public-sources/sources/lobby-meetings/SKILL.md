---
name: lobby-meetings
description: Track published lobbying meetings and related transparency records from the Estonian Government Office.
---

# Lobby Meetings Tracking

## Use when
- You need transparency data on meetings with lobbyists.
- You need influence-context records around policy decisions.

## Avoid when
- You need formal legal acts without stakeholder context.

## Inputs
- Institution/official, time range, topic/entity keywords.

## Outputs
- Meeting timeline with participant/topic metadata.

## Primary endpoint
- Lobby meetings page: https://www.riigikantselei.ee/asutus-uudised-ja-kontakt/lobitegevus/lobistidega-kohtumised

## Workflow
1. Open lobbying meetings publication view.
2. Collect meeting records and attached context where available.
3. Normalize dates, participants, and topics.
4. Return analysis-ready timeline.

## Human setup (when needed)
- If records are split across downloadable files/pages, walk user through retrieval and continue from downloaded files.

## Quality checks
- Distinguish meeting announcements from retrospective disclosures.
- Keep names and organization labels exactly as published.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.riigikantselei.ee/asutus-uudised-ja-kontakt/lobitegevus/lobistidega-kohtumised (HTTP 200, text/html;, file links detected: 9)

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
