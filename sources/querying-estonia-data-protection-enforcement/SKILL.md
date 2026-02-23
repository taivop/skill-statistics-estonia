---
name: querying-estonia-data-protection-enforcement
description: Query Data Protection Inspectorate public materials for enforcement, guidance, and privacy-governance operational context.
---

# Data Protection Enforcement Context

## Use when
- You need public privacy enforcement or guidance context.
- You need operational data-protection oversight references.

## Avoid when
- You need private complaint details not publicly disclosed.

## Inputs
- Topic, controller/sector, timeframe.

## Outputs
- Public enforcement/guidance references with metadata.

## Primary endpoint
- AKI homepage: https://www.aki.ee/en

## Workflow
1. Locate relevant enforcement/guidance sections.
2. Extract entries by date/topic.
3. Normalize titles, dates, and links.
4. Return oversight-context dataset.

## Human setup (when needed)
- If site navigation is not directly machine-queryable, walk the user through exact clicks and continue from shared URLs/files.

## Quality checks
- Distinguish guidance from sanctions/enforcement actions.
- Preserve original publication wording and dates.
