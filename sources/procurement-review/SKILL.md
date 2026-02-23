---
name: procurement-review
description: Use Ministry of Finance procurement review pages for public procurement dispute handling, review procedures, and outcome context.
---

# Procurement Review

## Use when
- You need official procurement review procedures or outcomes context.
- You need structured extraction of procurement review materials.

## Avoid when
- You only need tender or award datasets.

## Inputs
- Review topic, period, and case/procedure scope.

## Outputs
- Structured procurement review references and outcome fields.

## Primary endpoints
- Public procurement review: https://www.fin.ee/en/public-procurement-state-aid-and-assets/public-procurement-policy/public-procurement-review

## Workflow
1. Identify relevant procurement review materials/case references.
2. Extract procedure stage and published outcomes.
3. Normalize fields across publication formats.
4. Return structured output with legal-context notes.

## Human setup (when needed)
- If case materials are document-only, guide user through retrieval and continue from files.

## Quality checks
- Keep case/review references unchanged.
- Distinguish procedural guidance from case outcomes.
