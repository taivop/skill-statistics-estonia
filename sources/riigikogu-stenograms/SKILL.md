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
