---
name: vital-statistics-procedures
description: Use Ministry of Interior vital statistics procedures pages for official civil-registration process context and structured policy extraction.
---

# Vital Statistics Procedures

## Use when
- You need official civil/vital-statistics procedural context.
- You need structured extraction from published procedure materials.

## Avoid when
- You need person-level registry data.

## Inputs
- Procedure topic, legal context, and period.

## Outputs
- Structured procedure references, responsibilities, and workflow notes.

## Primary endpoints
- Vital statistics procedures: https://www.siseministeerium.ee/en/activities/population-procedures/vital-statistics-procedures

## Workflow
1. Locate relevant procedure/legal guidance pages.
2. Extract process steps, roles, and official references.
3. Normalize terminology across documents.
4. Return structured process map with citations.

## Human setup (when needed)
- If procedures reference external forms/registries, guide user through obtaining those materials and continue from them.

## Quality checks
- Keep process/legal references linked to each step.
- Separate administrative procedure from statistical outputs.
