---
name: state-aid-register
description: Query official Estonian state-aid policy and publication pages for aid framework, scheme references, and compliance context.
---

# State Aid Register Context

## Use when
- You need official state-aid scheme/policy references.
- You need compliance context for aid measures.

## Avoid when
- You need procurement tender-level records.

## Inputs
- Aid measure/scheme scope, period, and authority.

## Outputs
- State-aid scheme/context dataset with reference links.

## Primary endpoints
- State aid page: https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-aid
- State aid legislation: https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-aid/state-aid-legislation

## Workflow
1. Identify applicable aid framework and scheme references.
2. Extract linked guidance, legal basis, and reporting context.
3. Normalize scheme naming and period fields.
4. Return structured references plus limitations.

## Human setup (when needed)
- If specific scheme-level data is only available via linked documents or external systems, guide the user through retrieval and continue from supplied files.

## Quality checks
- Keep legal basis citations with each scheme reference.
- Separate policy guidance from quantitative disbursement data.

## Limitations
- A single openly queryable machine-readable register may not be exposed directly on this page; follow linked official materials.
