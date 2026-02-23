---
name: food-business-approvals
description: Use Agriculture and Food Board food business approval pages for licensing/approval workflows and official requirement extraction.
---

# Food Business Approvals

## Use when
- You need official approval/licensing process context for food businesses.
- You need structured extraction of approval requirements and statuses.

## Avoid when
- You need consumption or food-price indicators.

## Inputs
- Business type, approval stage, and period.

## Outputs
- Structured approval-process references and requirement fields.

## Primary endpoints
- Approval of operating enterprises: https://pta.agri.ee/en/food/approval-operating-enterprises

## Workflow
1. Determine applicable approval route by business type.
2. Extract requirement and procedural fields.
3. Normalize approval categories and statuses.
4. Return structured process output.

## Human setup (when needed)
- If approvals require interactive service usage, guide user through steps and continue from provided outputs.

## Quality checks
- Preserve official requirement references.
- Keep process stage and responsible authority explicit.
