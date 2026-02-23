---
name: querying-tallinn-legal-acts-register
description: Query Tallinn legal acts register for municipal regulations, orders, and official city legal documents.
---

# Tallinn Legal Acts Register

## Use when
- You need official Tallinn municipal legal acts.
- You need city-level regulation tracking and reference links.

## Avoid when
- You need broader national legal corpus only.

## Inputs
- Legal act keywords, type, issuing body, date range.

## Outputs
- Tallinn legal acts dataset with citations.

## Primary endpoint
- Register: https://oigusaktid.tallinn.ee/

## Workflow
1. Search acts by topic/type/date.
2. Capture identifiers, dates, and validity metadata.
3. Extract links to full act text.
4. Return structured act list.

## Human setup (when needed)
- If results are only browsable via UI widgets, guide user through exact search and have them share the resulting filtered URL.

## Quality checks
- Preserve act identifier and effective date.
- Separate current and repealed acts.
