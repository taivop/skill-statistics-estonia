---
name: animal-disease-control
description: Use Agriculture and Food Board infectious animal disease sources for control measures, surveillance context, and operational response references.
---

# Animal Disease Control

## Use when
- You need official infectious animal disease control context.
- You need structured extraction of surveillance/control references.

## Avoid when
- You need human communicable disease statistics.

## Inputs
- Disease topic, period, and region/species scope.

## Outputs
- Structured disease-control references and indicator fields.

## Primary endpoints
- Infectious animal diseases: https://pta.agri.ee/en/animals/infectious-animal-diseases

## Workflow
1. Retrieve relevant disease-control publications/pages.
2. Extract measures, timelines, and indicator fields.
3. Normalize disease and response categories.
4. Return structured outputs with source links.

## Human setup (when needed)
- If source details are in linked documents, guide user through retrieval and continue from files.

## Quality checks
- Keep disease definitions and measure scope explicit.
- Distinguish preventive guidance from incident reporting.
