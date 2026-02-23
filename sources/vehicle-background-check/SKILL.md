---
name: vehicle-background-check
description: Use official vehicle background check service for vehicle registry status context and public vehicle record validation.
---

# Vehicle Background Check

## Use when
- You need public vehicle registry status checks.
- You need vehicle background validation from official transport services.

## Avoid when
- You need private owner-level data not publicly exposed.

## Inputs
- Vehicle identifier(s) supported by service.

## Outputs
- Structured vehicle status/background results.

## Primary endpoints
- Vehicle background check: https://eteenindus.mnt.ee/public/soidukTaustakontroll.jsf?lang=en

## Workflow
1. Validate supported search identifier.
2. Run check and capture returned fields.
3. Normalize status/technical fields.
4. Return structured output with query timestamp.

## Human setup (when needed)
- If captcha/session controls appear, guide user through form submission and continue from returned output.

## Quality checks
- Preserve original registry status labels.
- Keep query timestamp and identifier used.
