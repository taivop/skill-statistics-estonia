---
name: consumer-technical-regulator-decisions
description: Query Consumer Protection and Technical Regulatory Authority public materials for supervision and enforcement decision context.
---

# Consumer/Technical Regulator Decisions

## Use when
- You need TTJA supervision/enforcement publication context.
- You need sector-regulation operational outcome references.

## Avoid when
- You need unrelated market stats without regulatory context.

## Inputs
- Sector/topic, entity, and date range.

## Outputs
- Decision-related publication references and metadata.

## Primary endpoint
- TTJA homepage: https://ttja.ee/en

## Workflow
1. Identify decision/enforcement-related sections.
2. Extract relevant entries and links.
3. Normalize topic/date/entity fields.
4. Return structured regulatory-context table.

## Human setup (when needed)
- If direct scraping is blocked by site structure, guide user through browsing/filtering and continue from provided links/files.

## Quality checks
- Label items by type (decision, warning, guidance, news).
- Keep source links and publication dates exact.
