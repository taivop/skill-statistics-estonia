---
name: querying-tartu-open-data
description: Locate and use Tartu city open datasets via Tartu open data page and national portal organization listings.
---

# Tartu Open Data

## Use when
- You need Tartu municipal datasets.
- You need organization-scoped discovery for Tartu city data.

## Avoid when
- You need Tallinn-specific direct API querying.

## Inputs
- Topic and desired dataset granularity.

## Outputs
- Tartu dataset shortlist with direct data links.

## Primary endpoints
- City open data page: https://www.tartu.ee/en/open-data
- Organization discovery on national portal: https://andmed.eesti.ee/en/search?organization=tartu-linnavalitsus

## Workflow
1. Start from Tartu open data page and collect linked catalog references.
2. Discover Tartu-owned datasets on the national portal.
3. Select datasets with machine-readable access and recent updates.
4. Return prioritized list with concrete extraction steps.

## Human setup (when needed)
- If a dataset is only downloadable via browser flow, provide precise click path and request the downloaded file for continuation.

## Quality checks
- Confirm dataset owner is Tartu city (or clearly linked municipal entity).
- Keep source URL and refresh date in final metadata.
