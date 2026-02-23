---
name: fairway-dues
description: Use fairway dues sources for maritime fee policy, charge structure, and extractable official tariff information.
---

# Fairway Dues

## Use when
- You need official fairway dues policy/tariff context.
- You need structured extraction of dues-related fields.

## Avoid when
- You need broad maritime economy trend data only.

## Inputs
- Vessel/category scope, period, and dues component.

## Outputs
- Structured dues/tariff references and extracted values.

## Primary endpoints
- Fairway dues: https://www.transpordiamet.ee/en/fairway-dues

## Workflow
1. Retrieve dues policy/tariff materials.
2. Extract charge components, exemptions, and period applicability.
3. Normalize tariff units and categories.
4. Return structured output with source references.

## Human setup (when needed)
- If tariff details are in linked docs, guide user through retrieval and continue from files.

## Quality checks
- Keep tariff applicability period explicit.
- Separate statutory basis from derived interpretation.
