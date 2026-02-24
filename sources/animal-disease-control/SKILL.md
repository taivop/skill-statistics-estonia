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

## Access reality
- Public access type: guidance pages and linked public information resources.
- This source is primarily policy/operational guidance; direct machine-readable disease-event datasets are limited.

## Inputs
- Disease topic, period, and region/species scope.

## Outputs
- Structured disease-control references and indicator fields where publicly published.

## Primary endpoints
- Main page: https://pta.agri.ee/en/animals/infectious-animal-diseases
- Related registration/process page: https://pta.agri.ee/en/animals/registering-keeper-animals
- Linked agriculture portal (public/services mix): https://portaal.agri.ee/epm-portal-ng/esileht.html

## Retrieval workflow
1. Open infectious disease page and collect disease-control notices, definitions, and linked references.
2. Follow only public links that contain concrete records, bulletins, or official lists.
3. Extract explicit measures, responsible authority, scope, and effective dates from source text.
4. If records are only in linked files/pages, preserve source URLs and continue extraction from those materials.

## Request contract
- No single documented open API for infectious animal disease records in this source skill.
- Treat this as document/page extraction unless a linked public dataset is explicitly available.

## Output schema expectations
- Keep at least:
  - disease name
  - measure/control action
  - affected species/area scope
  - effective/start date and end date (if present)
  - source authority and source URL

## Limits and caveats
- Many linked systems mix public info and authenticated workflows.
- Guidance text can change without machine-readable changelog.
- Do not infer incident counts unless explicitly published.

## Verification hooks
- Verify each extracted item has a source URL and publication/update date where available.
- Verify extraction separates preventive guidance from incident/event statements.

## Quality checks
- Keep disease definitions and measure scope explicit.
- Distinguish preventive guidance from incident reporting.
