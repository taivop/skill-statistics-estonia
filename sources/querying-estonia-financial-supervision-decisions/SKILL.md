---
name: querying-estonia-financial-supervision-decisions
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
