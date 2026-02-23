---
name: querying-state-audit-reports
description: Query National Audit Office publications and audits to extract findings on public-sector performance and governance operations.
---

# State Audit Reports

## Use when
- You need independent audit findings about government operations.
- You need audit-level evidence for policy/governance analysis.

## Avoid when
- You need primary operational logs rather than audit conclusions.

## Inputs
- Audit topic, institution, period, and type.

## Outputs
- Audit list with findings metadata and links.

## Primary endpoint
- Audit list: https://www.riigikontroll.ee/en/audits

## Workflow
1. Filter audits by topic/type/date.
2. Extract title, institution, publication date, and report link.
3. Capture key findings/recommendations if needed.
4. Return structured audit evidence table.

## Human setup (when needed)
- If report documents require manual download, guide user through retrieval and continue from files.

## Quality checks
- Separate audit reports from press/news items.
- Keep publication date and audit type fields explicit.
