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
