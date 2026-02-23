---
name: querying-estonia-state-ownership-data
description: Query official state-stakeholding and state-ownership policy pages for governance, ownership structure, and state-enterprise context.
---

# State Ownership Data

## Use when
- You need state stakeholding and ownership-governance context.
- You need official source references for state-enterprise ownership.

## Avoid when
- You need company-level financial statements only.

## Inputs
- Enterprise scope, sector, and analysis period.

## Outputs
- Structured ownership-governance dataset and source notes.

## Primary endpoints
- State assets/stakeholdings: https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-assets/state-stakeholdings

## Workflow
1. Retrieve state-stakeholding references and linked materials.
2. Extract enterprise, ownership-share, and governance fields where published.
3. Normalize organization names and ownership categories.
4. Return ownership map with confidence notes.

## Human setup (when needed)
- If core details are spread across linked documents/annexes, guide the user through opening/downloading them and continue from those files.

## Quality checks
- Distinguish direct vs indirect state ownership.
- Record publication date for each extracted source.

## Limitations
- A single machine-readable central register may not be publicly exposed from this entry page; use linked official materials as primary evidence.
