---
name: riigikogu-agendas
description: Track Riigikogu meeting schedules and agenda items from parliamentary calendar views.
---

# Riigikogu Agendas

## Use when
- You need upcoming or historical meeting agenda operations.
- You need committee/plenary schedule tracking.

## Avoid when
- You need only final decisions without agenda context.

## Inputs
- Date window and body type (plenary/committee).

## Outputs
- Agenda calendar extract and event summary.

## Primary endpoint
- Calendar: https://www.riigikogu.ee/tegevus/kalender/

## Workflow
1. Filter calendar by date/body.
2. Capture event metadata and linked agenda pages.
3. Normalize date/time and venue fields.
4. Return chronological agenda dataset.

## Human setup (when needed)
- If calendar requires interactive filtering, walk user through exact filter selection and have them share resulting view URL.

## Quality checks
- Use Estonian local dates/times as published.
- Avoid inferring agenda outcomes from schedule entries.
