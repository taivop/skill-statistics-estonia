---
name: ministry-document-registries
description: Query Estonia's official ministry and agency document registries (ADR network) for operational records, incoming/outgoing documents, and workflow traceability.
---

# Ministry Document Registries

## Use when
- You need official document-level operational records from ministries/agencies.
- You need a trace of administrative workflow (registration, correspondence, routing).

## Avoid when
- You need enacted legal texts only.

## Inputs
- Institution, date range, document keywords, registry identifiers.

## Outputs
- Registry search results with document metadata and source links.

## Primary endpoints
- ADR network root: https://adr.rik.ee/
- RIK agency document register: https://www.rik.ee/en/agency/document-register

## Workflow
1. Identify target institution's registry from ADR network.
2. Query by keyword/date/document number.
3. Include RIK agency document register where institution context requires it.
4. Extract core metadata (registry number, dates, sender/recipient, subject).
5. Return normalized records and links.

## Human setup (when needed)
- ADR pages are often UI-first. Walk the user through selecting the institution and entering filters, then ask for the resulting search URL or exported file and continue.

## Quality checks
- Keep original registry identifiers unchanged.
- Separate incoming vs outgoing records where provided.
