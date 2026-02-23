---
name: querying-government-office-document-register
description: Query the Government Office document register for official central-government document records and administrative traceability.
---

# Government Office Document Register

## Use when
- You need Government Office (Riigikantselei) document records.
- You need central-government correspondence and process references.

## Avoid when
- You need only policy outcomes, not record-level documents.

## Inputs
- Keywords, date range, record number, topic.

## Outputs
- Document-register result set with metadata and links.

## Primary endpoint
- Register page: https://www.riigikantselei.ee/asutus-uudised-ja-kontakt/dokumendiregister

## Workflow
1. Open document register page and locate search entry point.
2. Run focused query by date and keyword.
3. Extract identifiers, dates, and titles.
4. Return structured records with source links.

## Human setup (when needed)
- If the register opens in a UI module without deep-linkable queries, guide the user click-by-click and continue from screenshots/exports or shared links.

## Quality checks
- Preserve official document numbers.
- Record exact publication/registration dates.
