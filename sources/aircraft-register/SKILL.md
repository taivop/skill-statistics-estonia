---
name: aircraft-register
description: Use official aircraft register pages for aircraft registration status and aviation registry context.
---

# Aircraft Register

## Use when
- You need official aircraft registration context.
- You need structured extraction of aircraft register fields.

## Avoid when
- You need air-incident reporting analytics (use aviation occurrence skill).

## Access reality
- Public access type: HTML table on a public webpage (no documented JSON API in skill scope).
- EN context page exists, but practical register table is on the ET page.

## Inputs
- Optional aircraft identifier or registration scope.

## Outputs
- Structured aircraft registry records and status metadata.

## Primary endpoints
- EN context page: https://www.transpordiamet.ee/en/vehicle-ship-airplane/aircraft-registration/aircraft-register
- ET register table page (practical source): https://www.transpordiamet.ee/ohusoidukite-register

## Retrieval workflow
1. Open ET register page `https://www.transpordiamet.ee/ohusoidukite-register`.
2. Locate the published register table under aircraft register content.
3. Extract row cells in fixed order per table row.
4. Capture the published update stamp (`Register seisuga: .../updated`).
5. Return normalized rows with source URL and retrieval timestamp.

## Request contract
- No stable public API contract documented here.
- Retrieval is page HTML parsing from published table content.

## Output schema expectations
- Extract these fields per row:
  - registration mark (example format `ES - XYZ`)
  - aircraft type
  - serial / construction number
  - owner
  - operator
- Attach `register_update_date` from page text (`Register seisuga`).

## Limits and caveats
- English route is mainly context; data table is on Estonian page.
- Page also contains procedural forms/docx links; separate these from register-row extraction.
- Formatting and table structure can change with CMS updates.

## Verification hooks
- Confirm at least one `ES - ...` registration value is extracted.
- Confirm row-cell grouping is divisible by 5 fields.
- Confirm update stamp is captured when present.

## Quality checks
- Keep official registration identifiers unchanged.
- Separate current status table values from procedural document links.
