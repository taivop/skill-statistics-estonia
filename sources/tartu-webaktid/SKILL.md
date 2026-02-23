---
name: tartu-webaktid
description: Use Tartu WebAktid register for city legal acts and official municipal decision records.
---

# Tartu WebAktid

## Use when
- You need Tartu city legal acts and municipal legal decisions.

## Avoid when
- You need broader Tartu document workflow metadata outside legal acts.

## Inputs
- Act keywords, type, period.

## Outputs
- Tartu legal-act records with links/metadata.

## Primary endpoint
- WebAktid: https://info.raad.tartu.ee/webaktid.nsf

## Workflow
1. Search WebAktid by keywords/type/date.
2. Extract act metadata and document links.
3. Standardize identifiers and dates.
4. Return legal-acts table for analysis.

## Human setup (when needed)
- If UI requires manual query forms, guide user through exact form inputs and continue from result links.

## Quality checks
- Preserve original Tartu act identifiers.
- Keep validity/effective dates when published.
