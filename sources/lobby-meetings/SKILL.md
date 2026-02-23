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
