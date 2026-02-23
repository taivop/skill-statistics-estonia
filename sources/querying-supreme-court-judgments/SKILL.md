---
name: querying-supreme-court-judgments
description: Query Estonian Supreme Court judgment publications for case-law context that shapes governance and administrative practice.
---

# Supreme Court Judgments

## Use when
- You need Supreme Court case-law references.
- You need jurisprudence context for administrative/governance questions.

## Avoid when
- You need lower-court bulk proceedings without Supreme Court focus.

## Inputs
- Case topic, chamber/type, date range, keywords.

## Outputs
- Judgment list with metadata and links.

## Primary endpoint
- Judgments page (ET): https://www.riigikohus.ee/et/lahendid

## Workflow
1. Search/filter judgments by topic/date.
2. Extract case references and dates.
3. Capture decision summaries or linked full text.
4. Return legal-context dataset.

## Human setup (when needed)
- If filtering is UI-only or Estonian-only, provide exact user steps to locate target judgments and continue from shared links.

## Quality checks
- Preserve case number and date format.
- Do not infer holdings beyond published text.
