---
name: medicines-register
description: Query Estonia Medicines Register for medicinal-product records, authorization metadata, and regulatory status context.
---

# Medicines Register

## Use when
- You need medicinal-product registry details and status.
- You need authorization/registration metadata for medicines.

## Avoid when
- You need broad public-health incidence statistics.

## Inputs
- Product name, active substance, authorization holder, or registry ID.

## Outputs
- Structured medicines-register extract and status fields.

## Primary endpoints
- Medicines register: https://www.ravimiregister.ee/

## Workflow
1. Query by product/substance/holder criteria.
2. Extract authorization and status metadata.
3. Normalize identifiers and naming variants.
4. Return structured registry records with source dates.

## Human setup (when needed)
- If interactive filters require manual operation, guide user through the search/export path and continue from shared outputs.

## Quality checks
- Keep official register identifiers untouched.
- Separate active vs withdrawn/suspended statuses.
