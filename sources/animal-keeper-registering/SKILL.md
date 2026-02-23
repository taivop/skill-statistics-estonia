---
name: animal-keeper-registering
description: Use Agriculture and Food Board animal keeper registration sources for registry workflow context and extractable official outputs.
---

# Animal Keeper Registering

## Use when
- You need official animal-keeper registration workflow context.
- You need structured extraction from publicly available registration materials.

## Avoid when
- You need detailed confidential farm-level records.

## Inputs
- Registration topic, species scope, and period.

## Outputs
- Structured registration process/output references and fields.

## Primary endpoints
- Registering keeper of animals: https://pta.agri.ee/en/animals/registering-keeper-animals

## Workflow
1. Identify applicable registration route and requirements.
2. Extract available public fields and process artifacts.
3. Normalize entity/type taxonomy.
4. Return structured output and access caveats.

## Human setup (when needed)
- If specific outputs require authenticated services, guide user through that flow and continue from provided documents/results.

## Quality checks
- Keep authoritative identifiers where provided.
- Distinguish guidance content from register outputs.
