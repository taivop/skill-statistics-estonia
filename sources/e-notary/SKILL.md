---
name: e-notary
description: Use RIK e-notary service context for notarial workflow guidance and structured extraction of publicly accessible process information.
---

# E-Notary

## Use when
- You need official notarial e-service process context.
- You need structured extraction of public e-notary workflow outputs.

## Avoid when
- You need confidential notarial records.

## Inputs
- Service type, procedural stage, and period.

## Outputs
- Structured e-notary process/output references.

## Primary endpoints
- E-notary service: https://www.rik.ee/en/other-services/e-notary

## Workflow
1. Identify relevant e-notary service route.
2. Extract process requirements and available outputs.
3. Normalize service/stage terminology.
4. Return structured process map and references.

## Human setup (when needed)
- If interaction requires authenticated service usage, guide user through required steps and continue from provided results.

## Quality checks
- Separate process guidance from official output artifacts.
- Preserve legal references and fees where listed.
