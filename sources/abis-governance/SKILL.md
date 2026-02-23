---
name: abis-governance
description: Use ABIS governance pages for official biometric identification system governance context, responsibilities, and public process references.
---

# ABIS Governance

## Use when
- You need official ABIS governance/process context.
- You need structured extraction of system governance references.

## Avoid when
- You need biometric personal data.

## Inputs
- Governance topic, period, and responsibility scope.

## Outputs
- Structured ABIS governance references and extracted fields.

## Primary endpoints
- ABIS page: https://www.siseministeerium.ee/en/activities/efficient-population-management/automated-biometric-identification-system-database-abis

## Workflow
1. Retrieve ABIS governance/public process materials.
2. Extract roles, responsibilities, and process references.
3. Normalize terminology for cross-source comparison.
4. Return structured governance map.

## Human setup (when needed)
- If details require linked legal/policy documents, guide user through retrieval and continue from files.

## Quality checks
- Keep institutional responsibilities clearly separated.
- Distinguish system governance from technical claims.
