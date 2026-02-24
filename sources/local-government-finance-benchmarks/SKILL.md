---
name: local-government-finance-benchmarks
description: Query Ministry of Finance local-government and state-accountancy sources for municipal finance benchmarking and cross-municipality comparison context.
---

# Local Government Finance Benchmarks

## Use when
- You need local-government finance benchmark context.
- You need official municipality-level finance comparison inputs.

## Avoid when
- You only need national aggregate fiscal indicators.

## Inputs
- Municipality scope, period, and benchmark metrics.

## Outputs
- Municipality-level benchmark dataset with metric definitions.

## Primary endpoints
- State accountancy reports: https://www.fin.ee/en/public-finances-and-taxes/state-accountancy/consolidated-annual-reports-state
- State/local governance context: https://www.fin.ee/en/state-local-governments-spatial-planning/riigihaldus

## Workflow
1. Identify official finance report/publication for the target period.
2. Extract municipality-relevant indicators and definitions.
3. Standardize municipality names/codes and units.
4. Return benchmark-ready table and metric caveats.

## Human setup (when needed)
- If benchmark values are in PDF/annex tables, guide user through file retrieval and continue from provided files.

## Quality checks
- Keep accounting-basis notes with every metric.
- Separate budget, cash, and balance-sheet concepts.

## Access reality
- Public access type: UI page with direct downloadable files.
- Verification run: 2026-02-24.
- https://www.fin.ee/en/public-finances-and-taxes/state-accountancy/consolidated-annual-reports-state (HTTP 200, text/html;, file links detected: 1)
- https://www.fin.ee/en/state-local-governments-spatial-planning/riigihaldus (HTTP 200, text/html;, file links detected: 1)

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
