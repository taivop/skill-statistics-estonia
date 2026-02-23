---
name: querying-local-government-finance-benchmarks
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
