---
name: bank-of-statistics
description: Retrieve macro-financial and monetary statistics from the Bank of Estonia statistics portal for banking, external sector, and monetary analysis.
---

# Bank of Estonia Statistics

## Use when
- You need central-bank indicators (monetary, financial, external sector).
- You need statistics complementary to Statistics Estonia.

## Avoid when
- The indicator is already fully available from Statistics Estonia and no financial split is needed.

## Access reality
- Public access type: JavaScript UI backed by `/spring/*` JSON endpoints.
- Critical caveat: direct endpoint calls can return `406` without browser-like request headers.

## Inputs
- Indicator topic and period.
- Preferred granularity and format.

## Outputs
- Downloaded indicator series and source citation.

## Primary endpoints
- Portal UI: https://statistika.eestipank.ee/
- Example JSON endpoints (public):
  - https://statistika.eestipank.ee/spring/getValuutad
  - https://statistika.eestipank.ee/spring/getValuutaKursid
  - https://statistika.eestipank.ee/spring/getValuutaKurssAjaloos
  - https://statistika.eestipank.ee/spring/getAvaldamiskalenderHeaders
  - https://statistika.eestipank.ee/spring/getHeadingsFilterData
  - https://statistika.eestipank.ee/spring/getAvaldamiskalenderList

## Retrieval workflow
1. Start from portal page to identify needed indicator family.
2. For `/spring/*` endpoint calls, send headers:
   - `Accept: application/json, text/plain, */*`
   - `X-Requested-With: XMLHttpRequest`
   - `Referer: https://statistika.eestipank.ee/`
3. Call relevant endpoint with required parameters.
4. Parse JSON response and normalize dates/units.
5. Keep endpoint URL and parameter set with output.

## Request contract
- `getValuutaKursid`:
  - required: `aeg`, `aeg1`, `aeg2`, `tyyp`, `lang`
  - date format expected by endpoint: `dd.mm.yyyy`
- `getValuutaKurssAjaloos`:
  - required: `valuuta1`, `valuuta2`, `aegAlg`, `aegLopp`, `lang`, `step`
  - known `step` values: `DAY`, `WEEK`, `MONTH`, `QUARTER`, `SEMIANNUAL`, `YEAR`
- `getAvaldamiskalenderList`:
  - required: `lng`
  - optional filter: `rubriikId`

## Output schema expectations
- Keep at least:
  - indicator code/name
  - period/date
  - value
  - unit/currency
  - dimension filters used (if any)
  - source endpoint URL and params

## Limits and caveats
- Endpoints are unofficially documented through frontend behavior.
- Some endpoint combinations return empty arrays if params are incomplete or mismatched.
- UI routes are hash-based; data endpoints are under `/spring/`.

## Verification hooks
- Verify JSON response content type is `application/json`.
- Verify endpoint returns non-empty arrays for known-valid sample query.
- Verify calls without headers can fail with `406` and calls with headers succeed.

## Quality checks
- Confirm frequency (daily/weekly/monthly/quarterly/annual).
- Confirm whether values are stock or flow before interpretation.
