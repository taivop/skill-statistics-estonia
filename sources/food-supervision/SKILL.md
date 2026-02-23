---
name: food-supervision
description: Use Agriculture and Food Board food supervision pages for inspection, compliance, and enforcement process context.
---

# Food Supervision

## Use when
- You need official food supervision/inspection context.
- You need structured extraction of food oversight materials.

## Avoid when
- You need food market price statistics.

## Inputs
- Supervision topic, period, and business type scope.

## Outputs
- Structured food supervision references and findings fields.

## Primary endpoints
- Food supervision: https://pta.agri.ee/en/food/supervision

## Workflow
1. Identify relevant supervision publications/guidance.
2. Extract inspection/compliance-related fields.
3. Normalize supervision taxonomy.
4. Return structured output with citations.

## Human setup (when needed)
- If details are in linked documents, guide user through retrieval and continue from files.

## Quality checks
- Distinguish process guidance from enforcement outcomes.
- Keep source date and publication context.
