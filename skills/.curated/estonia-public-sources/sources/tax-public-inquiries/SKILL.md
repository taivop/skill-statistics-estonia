---
name: tax-public-inquiries
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

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.emta.ee/en/private-client/e-services-tax-literacy/registers-inquiries/public-data-inquiries (HTTP 200, text/html;, file links detected: 1)
- https://apps.emta.ee/saqu/public/reference?lang=en (HTTP 200, text/html;, file links detected: 0)
- https://apps.emta.ee/saqu/public/taxdebt?lang=en (HTTP 200, text/html;, file links detected: 0)

## Request contract
- Use the listed primary endpoints as authoritative entry points.
- If API/query parameters are only visible in-browser, preserve exact request URL, params, and headers in output metadata.
- If endpoint is UI-only, document click path and extraction method used.

## Output schema expectations
- Keep at least: source URL, retrieval timestamp, publication/update date (if available), title/record label, and extracted governance-relevant fields.
- Preserve original field names when present in downloadable/API output.

## Limits and caveats
- Confirm whether data is open-download, UI-only, or authenticated before claiming full access.
- Separate narrative/guidance text from measurable records.

## Verification hooks
- Validate endpoint reachability and content type before extraction.
- Validate that each extracted claim is linked to a concrete source URL.
