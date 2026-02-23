---
name: labour-inspectorate-enforcement
description: Use Labour Inspectorate enforcement/proceedings pages for supervision actions, procedural steps, and compliance outcomes.
---

# Labour Inspectorate Enforcement

## Use when
- You need supervision/enforcement process context from the Labour Inspectorate.
- You need structured extraction of proceedings-related outputs.

## Avoid when
- You only need aggregate labour market statistics.

## Inputs
- Enforcement topic, period, and action type.

## Outputs
- Structured enforcement/proceedings records and summaries.

## Primary endpoints
- Proceedings page: https://www.tooinspektsioon.ee/jarelevalve/menetlustoimingud

## Workflow
1. Identify relevant enforcement action pages/documents.
2. Extract action type, dates, and outcomes.
3. Normalize enforcement taxonomy.
4. Return structured dataset with procedural caveats.

## Human setup (when needed)
- If source evidence is PDF/document based, guide user through obtaining files and continue from them.

## Quality checks
- Distinguish guidance text from actual enforcement outcomes.
- Keep action dates and references where available.
