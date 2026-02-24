---
name: aviation-occurrence-reporting
description: Use aviation occurrence reporting sources for safety-event reporting workflows and oversight context.
---

# Aviation Occurrence Reporting

## Use when
- You need official aviation occurrence reporting procedures and safety context.
- You need structured extraction of published reporting/safety materials.

## Avoid when
- You need aircraft registry status only.

## Access reality
- Public access type: reporting framework pages and links to reporting systems.
- Core occurrence systems are reporting portals; open incident-level datasets are not directly published here.

## Inputs
- Event type, period, and reporting scope.

## Outputs
- Structured occurrence-reporting references and extracted data (when published).

## Primary endpoints
- Transpordiamet occurrence page: https://www.transpordiamet.ee/en/aviation-and-aviation-safety/aviation-safety/occurrence-reporting
- ECCAIRS central hub: https://aviationreporting.eu/
- LOIS portal (login): https://lois.ecaa.ee/LoginClient.aspx

## Retrieval workflow
1. Open Transpordiamet occurrence page and extract official reporting obligations and taxonomy references.
2. Record links to reporting systems (ECCAIRS/LOIS) as system endpoints, not open-data endpoints.
3. If user asks for statistics, redirect to published report outputs (see `aviation-safety-reports`) or provided official files.
4. Return explicit limitations when incident-level data is not publicly downloadable.

## Request contract
- No public JSON/CSV incident API is documented in this source.
- ECCAIRS/LOIS links are service/reporting systems and may require registration/login.

## Output schema expectations
- Keep at least:
  - reporting authority
  - reportable event category reference
  - submission channel/system
  - publication/report link (if any)
  - access limitation status

## Limits and caveats
- Distinguish reporting instructions from published occurrence statistics.
- Do not claim open incident datasets unless a direct official publication is available.

## Verification hooks
- Verify source includes active links to occurrence-reporting systems.
- Verify every extracted event metric is tied to a published report/file source.

## Quality checks
- Distinguish reporting guidance from actual occurrence statistics.
- Keep event taxonomy tied to source definitions.
