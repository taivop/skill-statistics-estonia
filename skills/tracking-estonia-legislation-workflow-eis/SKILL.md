---
name: tracking-estonia-legislation-workflow-eis
description: Track Estonian draft legislation workflow in EIS, including coordination status, document versions, and stakeholder input history.
---

# Estonia Legislation Workflow (EIS)

## Use when
- You need operational status of draft legal acts in inter-ministerial coordination.
- You need chronology of proposals, versions, and comments.

## Avoid when
- You need only final enacted law text (use Riigi Teataja legal-acts skill).

## Inputs
- Draft title, keyword, ministry, or registry identifier.

## Outputs
- Timeline of workflow steps and current status.
- Linked documents and responsible institution context.

## Primary endpoint
- EIS portal: https://eelnoud.valitsus.ee/main/main

## Workflow
1. Search draft by title/keyword/ministry.
2. Open draft card and capture identifiers and latest status.
3. Extract milestone timeline (submission, coordination, revisions, approval path).
4. Return concise status summary with direct source links.

## Human setup (when needed)
- If search results are only available via interactive UI, guide the user step-by-step to open the correct draft card and share the URL; continue from that URL.

## Quality checks
- Separate current draft status from historical status.
- Keep timestamps and institution names exactly as published.
