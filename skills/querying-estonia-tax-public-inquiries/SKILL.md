---
name: querying-estonia-tax-public-inquiries
description: Query EMTA public inquiry services and related registry endpoints for tax-debt, registry, and public-lookup compliance context.
---

# Tax Public Inquiries (EMTA)

## Use when
- You need public inquiry outputs from EMTA registry/query tools.
- You need tax-debt or public registry lookup context.

## Avoid when
- You need full confidential tax filings.

## Inputs
- Person/company identifier or search parameters supported by inquiry tool.

## Outputs
- Structured results from public inquiry endpoints.

## Primary endpoints
- Public data inquiries info: https://www.emta.ee/en/private-client/e-services-tax-literacy/registers-inquiries/public-data-inquiries
- Public reference query: https://apps.emta.ee/saqu/public/reference?lang=en
- Public tax debt query: https://apps.emta.ee/saqu/public/taxdebt?lang=en

## Workflow
1. Select correct EMTA public inquiry endpoint.
2. Query with allowed identifier/search fields.
3. Parse and normalize returned public fields.
4. Return lookup result with query timestamp.

## Human setup (when needed)
- If captcha/session controls block automation, guide user through the inquiry form and continue from copied result output.

## Quality checks
- Respect endpoint-specific public-data limits.
- Keep inquiry timestamp and endpoint used.
