---
name: marital-property-register
description: Use e-marital property register public service context for official lookup workflows and registry evidence extraction.
---

# Marital Property Register

## Use when
- You need official marital property register workflow/context.
- You need structured extraction from publicly available registry outputs.

## Avoid when
- You need private records not publicly accessible.

## Inputs
- Query purpose, allowed identifiers, and legal context.

## Outputs
- Structured register outputs and access constraints metadata.

## Primary endpoints
- E-marital property register: https://www.rik.ee/en/other-services/e-marital-property-register

## Workflow
1. Determine what output is publicly available.
2. Execute lookup flow within allowed scope.
3. Extract structured fields and legal references.
4. Return output with access limitations.

## Human setup (when needed)
- If lookup needs authentication/role rights, walk user through the required steps and continue from resulting data.

## Quality checks
- Clearly label public vs restricted data boundaries.
- Preserve official registry references.
