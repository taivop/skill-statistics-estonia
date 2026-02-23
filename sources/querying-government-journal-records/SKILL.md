---
name: querying-government-journal-records
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
