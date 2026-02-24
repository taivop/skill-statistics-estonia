---
name: kultuurkapital-grants-data
description: Extract Estonian Cultural Endowment grant allocation records from round pages and embedded grant tables.
---

# Kultuurkapital Grants Data

## Use when
- You need award-level cultural grant allocations by round/year.
- You need recipient, purpose, and amount fields from official grant publications.

## Avoid when
- You need applicant personal data not publicly listed.

## Inputs
- Year/round.
- Optional target foundation or thematic area.

## Outputs
- Grant allocation table with recipient, purpose, amount, and round metadata.

## Access reality statement
- Access type: `UI copy-only`.
- Verified on 2026-02-24.
- Grant rounds are published as HTML pages with embedded tables.

## Primary endpoints
- Rounds index: https://www.kulka.ee/avalik-teave/eraldused-voorude-kaupa
- Example round page: https://www.kulka.ee/avalik-teave/eraldused-voorude-kaupa/2025-a-4-taotlusvoor

## Retrieval workflow (reproducible)
1. Open rounds index and collect round URLs.
2. Open target round page and identify grant tables.
3. Parse rows into recipient, purpose, and amount fields.
4. Normalize amount values (remove spaces/non-breaking spaces, preserve original string separately).
5. Return records with round slug and source page URL.

## Request/query contract
- No auth required.
- Data is HTML table content (no documented public API).
- Round pages follow stable slug pattern under `/avalik-teave/eraldused-voorude-kaupa/<slug>`.

## Output schema expectations
- `round_slug`
- `source_page_url`
- `recipient_name`
- `allocation_purpose`
- `amount_original`
- `amount_numeric`
- `foundation_or_section` (if inferable)

## Limits and caveats
- Table structures can vary between round pages.
- Amount formatting uses localized separators/spaces.
- Some pages contain multiple sections/foundations in one document.

## Verification hooks
- Index page contains many round links (for example `2025-a-4-taotlusvoor`).
- Example round page includes table columns `Eralduse saaja`, `Kasutamise eesmärk`/`Eralduse eesmärk`, and `Summa`/`Eraldatud summa`.
