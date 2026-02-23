---
name: aviation-occurrence-reporting
description: Use aviation occurrence reporting sources for safety-event reporting workflows and oversight context.
---

# Aviation Occurrence Reporting

## Use when
- You need official aviation occurrence reporting procedures and safety context.
- You need structured extraction of published reporting/safety materials.

## Avoid when
- You need aircraft registry status only.

## Inputs
- Event type, period, and reporting scope.

## Outputs
- Structured occurrence-reporting references and extracted data (when published).

## Primary endpoints
- Occurrence reporting: https://www.transpordiamet.ee/en/aviation-and-aviation-safety/aviation-safety/occurrence-reporting

## Workflow
1. Identify reporting framework and public outputs.
2. Extract published occurrence indicators/materials.
3. Normalize event categories and periods.
4. Return structured output with limitations.

## Human setup (when needed)
- If detailed datasets are not directly published, guide user through accessible report retrieval and continue from files.

## Quality checks
- Distinguish reporting guidance from actual occurrence statistics.
- Keep event taxonomy tied to source definitions.
