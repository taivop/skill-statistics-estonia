---
name: healthcare-professionals-register
description: Use Health Board healthcare professionals registration pages for registry-process context and official registration evidence extraction.
---

# Healthcare Professionals Register

## Use when
- You need official registration process context for healthcare professionals.
- You need structured extraction of publicly available registration outputs.

## Avoid when
- You need private personnel records not publicly accessible.

## Inputs
- Profession type, registration scope, and period.

## Outputs
- Structured registration-process/output references.

## Primary endpoints
- Registration of professionals: https://www.terviseamet.ee/en/healthcare/registration-of-health-care-professionals

## Workflow
1. Identify register route and eligibility/output scope.
2. Extract public registration-related fields and references.
3. Normalize profession categories.
4. Return structured output and access caveats.

## Human setup (when needed)
- If lookup/verification requires interactive forms, guide user step-by-step and continue from provided outputs.

## Quality checks
- Separate process guidance from register results.
- Keep official category and status labels unchanged.
