---
name: riigiteataja-draft-acts
description: Query Riigi Teataja draft-act search for legal drafting stream monitoring and draft-text retrieval.
---

# Riigi Teataja Draft Acts

## Use when
- You need public draft-act discovery and monitoring.
- You need links between drafts and final legal instruments.

## Avoid when
- You only need enacted/current legal text.

## Inputs
- Draft topic, issuer, date range.

## Outputs
- Draft-act search results with metadata and links.

## Primary endpoint
- Draft search: https://www.riigiteataja.ee/eelnoud/otsing.html

## Workflow
1. Run draft search with focused terms.
2. Capture draft identifiers, dates, and issuing body.
3. Follow links to draft documents and related acts.
4. Return tracking table suitable for updates.

## Human setup (when needed)
- If filters are UI-only, walk user through exact settings and ask for result URL or exported file.

## Quality checks
- Keep draft and enacted references separate.
- Preserve official identifiers and document dates.
