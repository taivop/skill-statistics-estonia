---
name: internal-security-annual-reviews
description: Retrieve Internal Security Service annual review publications with anti-bot-aware workflow and fallback handling when automated access is blocked.
---

# Internal Security Annual Reviews (KAPO)

## Use when
- You need annual institutional review publications from the Internal Security Service.
- You need high-level historical internal-security governance context.

## Avoid when
- You need guaranteed machine-readable extraction without manual/browser steps.

## Inputs
- Target year(s).
- Language preference.

## Outputs
- Annual review list and extracted sections/indicators from downloaded reports.

## Access reality statement
- Access type: `no public machine-readable data` (practical workflow is `UI copy-only`/manual browser download).
- Verified on 2026-02-24.
- Direct automated HTTP access to annual review page can return `403`.

## Primary endpoints
- Annual reviews landing page: https://www.kapo.ee/aastaraamat/

## Retrieval workflow (reproducible)
1. Attempt direct access and log response status.
2. If blocked (e.g., `403`), switch to browser/manual retrieval flow (human-guided click/download).
3. Collect annual report file URLs or downloaded files provided by user.
4. Extract report metadata (year, title, publication language) and requested content fields.
5. Return records with explicit `access_method` and blockage notes.

## Request/query contract
- No documented public API.
- Access may be protected by anti-bot controls and require browser challenge completion.
- Treat extraction as document-based once files are obtained.

## Output schema expectations
- `source_url`
- `report_year`
- `report_title`
- `report_file_url` (if available)
- `access_method` (`direct`, `browser-manual`, `user-provided-file`)
- `extracted_section`
- `notes`

## Limits and caveats
- Automation reliability is low due access controls.
- Publication format and structure can vary by year.
- Do not assume completeness if some years are inaccessible in current run.

## Verification hooks
- Direct request to `https://www.kapo.ee/aastaraamat/` observed `HTTP 403` on 2026-02-24.
- Extraction run must explicitly report whether records came from direct fetch or manual/browser fallback.
