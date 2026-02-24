---
name: state-assets-register
description: Retrieve Estonian state real-estate register open-data access points and related public state-assets records from fin.ee and RKVR frontend routes.
---

# State Assets Register (RKVR and fin.ee)

## Use when
- You need public state real-estate register open-data access paths.
- You need official state-assets governance records linked from Ministry of Finance pages.

## Avoid when
- You need cadastral geometry-only datasets (use geospatial/cadastre sources).

## Inputs
- Asset scope (state real estate / register open data).
- Time period if filtering by publication date.

## Outputs
- Source-linked list of asset register datasets/pages and downloadable records.

## Access reality statement
- Access type: `download files` + `UI export`/`UI copy-only`.
- Verified on 2026-02-24.
- fin.ee page publishes a direct RKVR open-data link; RKVR frontend uses SPA routes.

## Primary endpoints
- fin.ee state-assets area: https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-assets
- fin.ee state real-estate context: https://www.fin.ee/en/public-procurement-state-aid-and-assets/state-assets/state-real-estate
- RKVR open-data page (Estonian): https://www.fin.ee/riigihaldus-ja-avalik-teenistus-kinnisvara/riigi-kinnisvararegister/avaandmed
- RKVR frontend root: https://riigivara.fin.ee/rkvr-frontend/
- RKVR open-data route (SPA): https://riigivara.fin.ee/rkvr-frontend/#/aruanded/avaandmed

## Retrieval workflow (reproducible)
1. Open fin.ee RKVR open-data page and capture the explicitly listed RKVR open-data link.
2. Open RKVR frontend root to confirm service availability.
3. Use hash-route `#/aruanded/avaandmed` for open-data reports.
4. Capture dataset/report names and export/download actions visible in RKVR UI.
5. Return records with exact source URL, extraction method (`direct-file`, `ui-copy`, `ui-export`), and retrieval timestamp.

## Request/query contract
- No documented public REST contract is exposed on the fin.ee landing page.
- RKVR frontend declares bases in `rkvr-frontend-properties.js`:
  - `backEndBase = /rkvr`
  - `frontEndBase = /rkvr-frontend`
- Treat RKVR extraction as UI-driven unless stable machine endpoints are confirmed during retrieval.

## Output schema expectations
- `source_page_url`
- `dataset_or_report_name`
- `record_date` (if shown)
- `download_url` or `ui_path`
- `asset_scope`
- `format`
- `retrieval_method`

## Limits and caveats
- Non-hash path `.../rkvr-frontend/aruanded/avaandmed` can return 404; use hash route.
- UI labels are primarily Estonian.
- Full machine-readable inventory coverage may depend on frontend behavior and session state.

## Verification hooks
- RKVR open-data landing page contains text with link `https://riigivara.fin.ee/rkvr-frontend/aruanded/avaandmed`.
- `https://riigivara.fin.ee/rkvr-frontend/` returns 200 and includes `rkvr-frontend-properties.js`.
- `rkvr-frontend-properties.js` exposes `backEndBase` and `frontEndBase` variables.
