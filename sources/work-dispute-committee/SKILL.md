---
name: work-dispute-committee
description: Use Labour Inspectorate work dispute committee pages for labor-dispute procedure, filing workflow, and decision context.
---

# Work Dispute Committee

## Use when
- You need official labor dispute committee procedures and decision workflow context.
- You need structured extraction of public committee materials.

## Avoid when
- You need private dispute files not publicly released.

## Inputs
- Dispute category, period, and procedural stage.

## Outputs
- Structured process references and available decision outputs.

## Primary endpoints
- Work dispute committee: https://www.tooinspektsioon.ee/en/work-dispute-committee

## Workflow
1. Identify relevant committee procedure and document paths.
2. Extract deadlines, stages, and available outputs.
3. Normalize procedure vocabulary.
4. Return structured guidance/output references.

## Human setup (when needed)
- If decision materials require manual retrieval, guide the user through steps and continue from provided documents.

## Quality checks
- Distinguish binding decision text from guidance.
- Preserve official timelines and stage labels.
