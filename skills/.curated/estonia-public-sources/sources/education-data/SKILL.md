---
name: education-data
description: Retrieve public education registry and indicator records from EHIS and HaridusSilm, including published XLS/XLSX extracts and public registry views.
---

# Education Data (EHIS + HaridusSilm)

## Use when
- You need public education registry extracts (institutions/curricula/status).
- You need education indicator context from HaridusSilm.

## Avoid when
- You need student-level personal data (not publicly available).

## Inputs
- Education scope (`institutions`, `curricula`, `validation-status`, indicator topic).
- Period and geography.

## Outputs
- Source-linked registry/indicator extract with field definitions and caveats.

## Access reality statement
- Access type: `download files` + `UI export`.
- Verified on 2026-02-24.
- EHIS homepage exposes direct XLS/XLSX downloads and links to public registry views.

## Primary endpoints
- EHIS portal: https://www.ehis.ee/
- EHIS public view entry: https://enda.ehis.ee/avalik/
- EHIS institutions view: https://ehis.edu.ee/schools/educational-institutions
- Published institutions contacts XLS: https://gituja.eenet.ee/ehis/ehis1/failihoidla/-/raw/main/koolide_kontaktid.xls?ref_type=heads&inline=false
- Published curricula extract XLSX: https://gituja.eenet.ee/ehis/ehis1/failihoidla/-/raw/main/oppekavad.xlsx?ref_type=heads&inline=false
- HaridusSilm portal: https://www.haridussilm.ee/ee/avaleht

## Retrieval workflow (reproducible)
1. Start at `ehis.ee` and identify the relevant public extract link (contacts/curricula/validation).
2. Download XLS/XLSX file(s) directly from `gituja.eenet.ee` links.
3. If needed fields are not in files, use `enda.ehis.ee/avalik` or `ehis.edu.ee` views and capture filtered UI output.
4. For indicator context, export from HaridusSilm dashboards with explicit filters (level, region, year).
5. Return normalized fields and keep original column names alongside mapped names.

## Request/query contract
- No auth required for listed endpoints.
- EHIS file links are direct binary downloads (`application/octet-stream`).
- UI registry views are browser-rendered; extraction may require rendered HTML parsing rather than static source.

## Output schema expectations
- `source_system` (`EHIS` or `HaridusSilm`)
- `source_url`
- `record_type`
- `institution_id`/`school_name` (where available)
- `curriculum_code`/`curriculum_name` (where available)
- `status_or_indicator_name`
- `value`
- `period`
- `publication_or_update_date`

## Limits and caveats
- EHIS registry views are Estonian-first.
- Registry snapshots may not align to calendar year boundaries.
- Some interactive views may require browser execution to access full table content.

## Verification hooks
- EHIS homepage lists direct download links including `koolide_kontaktid.xls` and `oppekavad.xlsx`.
- Both published file URLs return HTTP 200 with binary content.
- `enda.ehis.ee/avalik/` is reachable and serves public registry access.
