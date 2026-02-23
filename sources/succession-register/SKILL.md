---
name: succession-register
description: Use official succession register service context for inheritance-related register workflows and structured output extraction.
---

# Succession Register

## Use when
- You need succession register process/context and available public outputs.
- You need structured extraction of official succession-register evidence.

## Avoid when
- You need confidential case details not publicly available.

## Inputs
- Query scope, allowed identifiers, and legal basis.

## Outputs
- Structured succession-register outputs and constraints notes.

## Primary endpoints
- Succession register: https://www.rik.ee/en/other-services/succession-register

## Workflow
1. Identify permitted lookup/output route.
2. Retrieve accessible record/result details.
3. Normalize identifiers and status fields.
4. Return structured output plus access caveats.

## Human setup (when needed)
- If access requires authenticated workflow, guide user step-by-step and continue from provided result material.

## Quality checks
- Preserve official references and timestamps.
- Separate process guidance from register output.
