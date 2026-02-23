---
name: government-session-agendas
description: Track Estonian government session agenda publications and related operational updates from valitsus.ee.
---

# Government Session Agendas

## Use when
- You need cabinet session agenda publications and related updates.
- You need chronology of session communications.

## Avoid when
- You need formal legal text of adopted acts.

## Inputs
- Date range and topic keywords.

## Outputs
- Session agenda publication list with dates and links.

## Primary endpoints
- Search seed (agenda keyword): https://valitsus.ee/otsing?filters%5Btype%5D=Uudis&filters%5Bkeyword%5D=Istungi%20p%C3%A4evakord&sort=created&page=1
- Main portal: https://valitsus.ee/en

## Workflow
1. Start from agenda-keyword search.
2. Collect matching publications with dates and titles.
3. Open item pages for links to related materials.
4. Return timeline of agenda publications.

## Human setup (when needed)
- If language/UI ambiguity blocks extraction, ask user to open the target publication in browser and share URL; then continue.

## Quality checks
- Separate agenda announcements from post-meeting communications.
- Preserve publication timestamps exactly.
