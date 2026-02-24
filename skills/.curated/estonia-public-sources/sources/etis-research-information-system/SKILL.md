---
name: etis-research-information-system
description: Retrieve public R&D records from ETIS by using browser-session-backed search endpoints and public portal views for projects, publications, persons, and institutions.
---

# ETIS Research Information System

## Use when
- You need public Estonian research governance records (projects, publications, institutions, researchers).
- You need repeatable ETIS search workflows with documented endpoint behavior.

## Avoid when
- You require restricted internal ETIS data.

## Inputs
- Entity type (`projects`, `publications`, `persons`, `institutions`, etc.).
- Search/filter terms.

## Outputs
- Structured ETIS search results with captured filter metadata and source URLs.

## Access reality statement
- Access type: `UI export`/`UI copy-only` with browser-session endpoint calls.
- Verified on 2026-02-24.
- Portal bundle exposes many `/Portal/...` endpoints; direct stateless POSTs can return SPA HTML, so browser session context is required.

## Primary endpoints
- ETIS portal: https://www.etis.ee/
- Example portal endpoints discovered in frontend bundle:
  - `/Portal/Projects/Search`
  - `/Portal/Publications/Search`
  - `/Portal/Persons/Search`
  - `/Portal/Institutions/Search`
  - `/Portal/*/GetFilters`

## Retrieval workflow (reproducible)
1. Open ETIS in browser and select target entity search view.
2. Apply filters through UI and observe network calls to `/Portal/.../Search` and `/Portal/.../GetFilters`.
3. Capture request payloads, response format, and current session headers/cookies used by browser.
4. Re-run equivalent requests within same browser session context when needed.
5. Return parsed records and include endpoint/payload metadata for reproducibility.

## Request/query contract
- Endpoint family: `/Portal/<Entity>/{Search|GetFilters}`.
- Requests are JSON-like/XHR from SPA context; session and anti-forgery context may be required.
- Unauthenticated direct POST without browser context may return portal HTML instead of data payload.

## Output schema expectations
- `entity_type`
- `source_url`
- `search_payload`
- `record_id`
- `title_or_name`
- `institution`
- `start_date`/`end_date` (if present)
- `funding_or_status` (if present)

## Limits and caveats
- API contract is not publicly documented in a stable spec.
- Endpoint behavior depends on SPA state/session.
- Field schemas vary significantly by entity type.

## Verification hooks
- ETIS frontend JS includes endpoint strings such as `/Portal/Projects/Search`, `/Portal/Publications/Search`, `/Portal/Persons/Search`.
- Direct POST to `/Portal/Projects/GetFilters` without browser session returns `text/html`, confirming UI-session dependency.
