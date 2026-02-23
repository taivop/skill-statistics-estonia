---
name: competition-authority-decisions
description: Query Competition Authority public materials for decisions, precepts, and competition/market governance enforcement context.
---

# Competition Authority Decisions

## Use when
- You need competition/market regulation enforcement context.
- You need public decisions or precept-related records.

## Avoid when
- You need procurement contract data rather than enforcement outcomes.

## Inputs
- Sector, entity, enforcement topic, date range.

## Outputs
- Decision/precept publication references with links.

## Primary endpoint
- Authority homepage: https://www.konkurentsiamet.ee/en

## Workflow
1. Locate decision-related sections/news/publications.
2. Filter by topic/entity/date.
3. Extract metadata and links.
4. Return enforcement-context record set.

## Human setup (when needed)
- Some pages may block automated access. If blocked, instruct user to open the target page in browser and share links/files; continue from provided material.

## Quality checks
- Mark whether each item is a formal decision, precept, or news summary.
- Keep publication dates and entity names exactly.
