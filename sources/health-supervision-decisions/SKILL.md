---
name: health-supervision-decisions
description: Query Health Board supervision and precept pages for regulatory decisions, enforcement actions, and public-health oversight context.
---

# Health Supervision Decisions

## Use when
- You need Health Board supervision/enforcement decision context.
- You need official precept/public oversight publications.

## Avoid when
- You only need disease incidence trends.

## Inputs
- Supervision topic, entity scope, and period.

## Outputs
- Structured supervision-decision dataset and evidence links.

## Primary endpoints
- Precepts page: https://www.terviseamet.ee/ettekirjutused
- Supervision page: https://www.terviseamet.ee/jarelevalve

## Workflow
1. Retrieve relevant supervision/precept publication entries.
2. Extract decision date, subject, and enforcement details.
3. Normalize entity/topic categories.
4. Return structured output with legal-context notes.

## Human setup (when needed)
- If decision details are document-based and not directly exportable, guide user through downloading/opening the files and continue from provided content.

## Quality checks
- Keep decision date and reference IDs where available.
- Separate announcement text from enforceable decision details.
