---
name: court-proceedings-data
description: Query public Estonian court-proceedings and related judicial information from Riigi Teataja court information pages.
---

# Estonia Court Proceedings Data

## Use when
- You need publicly listed court proceedings information.
- You need searchable judicial procedure records for legal-operational analysis.

## Avoid when
- You need sealed/non-public case files.

## Inputs
- Court/proceeding filters, date ranges, case keywords.

## Outputs
- Proceedings extract with case metadata and links.

## Primary endpoints
- Proceedings listing: https://www.riigiteataja.ee/kohtulahendid/koik_menetlused.html
- Court session search: https://www.riigiteataja.ee/kohtuteave/kohtuistungid_otsing.html

## Workflow
1. Use proceedings/session search pages for scope.
2. Extract case references, dates, and court identifiers.
3. Normalize case metadata for downstream analysis.
4. Return case/proceedings table with source links.

## Human setup (when needed)
- If anti-bot/UI controls block direct extraction, guide user through manual query and ask them to share resulting URLs.

## Quality checks
- Do not infer legal outcomes unless explicitly listed.
- Keep sensitive fields strictly within what is publicly exposed.
