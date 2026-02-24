---
name: defence-public-opinion-surveys
description: Retrieve Ministry of Defence public-opinion-on-defence survey reports from official historical PDF publication pages.
---

# Defence Public-Opinion Surveys

## Use when
- You need long-run public-opinion survey records on defence attitudes.
- You need comparable historical survey publications from one official source.

## Avoid when
- You need broader social polling outside defence domain.

## Inputs
- Year range.
- Topic keywords (readiness, willingness to defend, threat perception, NATO support).

## Outputs
- Survey publication index with dates, file URLs, and extracted headline indicators.

## Access reality statement
- Access type: `download files`.
- Verified on 2026-02-24.
- Survey reports are published as PDF links on the Ministry of Defence page.

## Primary endpoints
- Main surveys page: https://www.kaitseministeerium.ee/et/eesmargid-tegevused/avalik-arvamus-riigikaitsest
- Example survey file pattern: `/sites/default/files/avalik_arvamus_riigikaitsest_*.pdf`

## Retrieval workflow (reproducible)
1. Open surveys page and collect PDF links under `/sites/default/files/...`.
2. Parse year/month from filename and map to publication chronology.
3. Download selected reports and extract core indicators requested by user.
4. Preserve question wording/source page when comparing across years.
5. Return dataset with both publication metadata and extracted indicators.

## Request/query contract
- No auth required.
- Source is link-based (no documented API).
- Files are directly downloadable PDFs.

## Output schema expectations
- `source_page_url`
- `survey_file_url`
- `survey_period`
- `publication_date` (if available)
- `indicator_name`
- `indicator_value`
- `question_text`
- `notes`

## Limits and caveats
- Methodology and wording can change across survey waves.
- Historic files may use older naming/format conventions.
- Indicator extraction requires careful PDF parsing and consistency checks.

## Verification hooks
- Page includes many PDF links such as `avalik_arvamus_ja_riigikaitse_mai_2024.pdf` and `avalik_arvamus_riigikaitsest_2025_kantar_emor_.pdf`.
- File archive spans early 2000s onward in visible links.
