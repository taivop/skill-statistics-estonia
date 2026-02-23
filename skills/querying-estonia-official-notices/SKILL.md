---
name: querying-estonia-official-notices
description: Query Ametlikud Teadaanded official notices for public announcements, summons, insolvency, and statutory publication workflows.
---

# Estonia Official Notices

## Use when
- You need official publication notices and statutory announcements.
- You need organization/person/process-level notice tracking.

## Avoid when
- You need detailed court-case documents beyond notice publication.

## Inputs
- Notice type, party/entity name, date range.

## Outputs
- Notice list with publication metadata and links.

## Primary endpoint
- URI search: https://www.ametlikudteadaanded.ee/avalik/uriotsing

## Workflow
1. Search by entity/name/type/date.
2. Open notice entries and capture publication fields.
3. Normalize notice type and status for analysis.
4. Return structured notice dataset.

## Human setup (when needed)
- If query flow requires interactive form inputs/captcha, guide user step-by-step and continue from resulting notice links.

## Quality checks
- Preserve publication date and notice category exactly.
- Distinguish notices from underlying legal actions.
