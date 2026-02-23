---
name: querying-state-assets-register
description: Query official state-assets publication pages for public real-estate and state-assets governance context in Estonia.
---

# State Assets Register Context

## Use when
- You need official references on state assets and state real estate.
- You need governance context for state asset management.

## Avoid when
- You need cadastral parcel geometry only.

## Inputs
- Asset class, institution scope, and period.

## Outputs
- Structured state-assets reference dataset and notes.

## Primary endpoints
- State assets: https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-assets
- State real estate context: https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-assets/state-real-estate

## Workflow
1. Identify relevant asset-governance publication/section.
2. Extract asset categories and institution mappings.
3. Normalize taxonomy and period references.
4. Return structured output with provenance.

## Human setup (when needed)
- If detailed asset inventories are available only through linked PDFs or portals, walk user through retrieval and continue from those files.

## Quality checks
- Track publication date for each extracted item.
- Keep source-level distinctions between policy and asset inventories.

## Limitations
- Publicly exposed machine-readable full asset inventory may be limited; this skill focuses on official accessible sources and linked materials.
