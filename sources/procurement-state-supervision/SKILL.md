---
name: procurement-state-supervision
description: Use Ministry of Finance procurement state supervision pages for supervisory actions, compliance findings, and oversight process context.
---

# Procurement State Supervision

## Use when
- You need procurement supervision process and oversight context.
- You need structured extraction of supervision findings/actions.

## Avoid when
- You need procurement market analytics only.

## Inputs
- Supervision topic, period, and authority scope.

## Outputs
- Structured supervision references, actions, and findings.

## Primary endpoints
- State supervision: https://www.fin.ee/en/public-procurement-state-aid-and-assets/public-procurement-policy/state-supervision

## Workflow
1. Retrieve supervision-related publications/materials.
2. Extract action/finding details and dates.
3. Normalize supervisory action taxonomy.
4. Return structured outputs with citations.

## Human setup (when needed)
- If materials are PDF-based, guide user through retrieval and continue from extracted content.

## Quality checks
- Keep dates and reference IDs for each action.
- Separate policy guidance from actual supervisory findings.
