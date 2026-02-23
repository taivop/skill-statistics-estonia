---
name: e-ship-register-rik
description: Use RIK e-ship register service context for registry workflow guidance and extraction of publicly accessible register evidence.
---

# E-Ship Register (RIK)

## Use when
- You need RIK e-ship register workflow context.
- You need structured outputs from publicly available register views.

## Avoid when
- You only need Transport Administration ship-register publications.

## Inputs
- Vessel/query scope and allowed identifiers.

## Outputs
- Structured e-ship register outputs with provenance.

## Primary endpoints
- E-ship register: https://www.rik.ee/en/other-services/e-ship-register

## Workflow
1. Determine accessible register route and lookup parameters.
2. Extract available vessel/register fields.
3. Normalize identifiers and statuses.
4. Return structured dataset and limitations.

## Human setup (when needed)
- If register access is authenticated/UI-driven, guide user through the process and continue from exported/copied results.

## Quality checks
- Keep source system and retrieval route explicit.
- Preserve original register references.
