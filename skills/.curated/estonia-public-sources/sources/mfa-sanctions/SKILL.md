---
name: mfa-sanctions
description: Retrieve MFA sanctions implementation records from official sanctions pages and the linked sanctions search backend endpoint.
---

# MFA Sanctions Implementation

## Use when
- You need Estonia MFA sanctions implementation guidance and subject-list records.
- You need to test or monitor the sanctions backend endpoint used by portal pages.

## Avoid when
- You need only EU legal base texts without Estonia-specific implementation context.

## Inputs
- Sanctions topic (Belarus, human rights, Russia/Belarus, etc.).
- Whether to include API endpoint diagnostics.

## Outputs
- Page-derived sanctions records and API endpoint behavior metadata.

## Access reality statement
- Access type: `UI copy-only` + `API` (query-driven endpoint with currently sparse default response).
- Verified on 2026-02-24.
- Portal config exposes sanctions backend URL; direct unauthenticated requests currently return `null`.

## Primary endpoints
- MFA sanctions page: https://www.vm.ee/en/activity/international-sanctions/sanctions-government-republic-estonia
- Backend endpoint exposed in page config: https://search.service.eu-live.vportal.ee/v1/sanctions/vm
- Example sanctions subpages are linked from main page (subject lists by regime).

## Retrieval workflow (reproducible)
1. Open sanctions page and capture regime-specific list links and legal references.
2. Parse page config (`drupal-settings-json`) for `vpVmSanctions.sanctionsUrl`.
3. Query backend endpoint and store response status/body for reproducibility.
4. When backend returns empty/null, fall back to regime list pages and downloadable/legal references.
5. Return combined dataset with explicit `source_type` (`page_list`, `backend_probe`, `legal_reference`).

## Request/query contract
- Backend endpoint: `GET https://search.service.eu-live.vportal.ee/v1/sanctions/vm`.
- No public API spec discovered for required query params; default GET observed to return `null`.
- If browser network calls show additional params/headers, preserve them in run metadata.

## Output schema expectations
- `source_type`
- `source_url`
- `regime`
- `record_title`
- `record_url`
- `backend_request`
- `backend_response_summary`
- `legal_reference_url`

## Limits and caveats
- Backend may require undocumented query context; default responses can be empty.
- Sanctions content is policy-sensitive and changes over time; always capture retrieval date.
- Pages can mix explanatory text and actionable list records.

## Verification hooks
- Sanctions page `drupal-settings-json` includes `vpVmSanctions.sanctionsUrl` pointing to `.../v1/sanctions/vm`.
- Direct request to backend endpoint returns JSON `null` (observed on 2026-02-24).
- Main sanctions page includes direct links to regime-specific subject lists.
