---
name: digital-government-studies
description: Query RIA studies, analyses, and overviews for digital-government operational evidence and policy context.
---

# Digital Government Studies (RIA)

## Use when
- You need official studies/analyses on state digital systems and governance.
- You need contextual evidence for operational-government assessments.

## Avoid when
- You need transactional system data instead of analytical publications.

## Inputs
- Topic keywords and date range.

## Outputs
- Publication index with metadata and links.

## Primary endpoint
- Studies/analyses page: https://www.ria.ee/en/authority-news-and-contact/news-media-contact/studies-analyses-overviews

## Workflow
1. Collect study/overview entries by topic/date.
2. Extract titles, dates, and downloadable links.
3. Tag each entry by domain (cyber, services, infrastructure, etc.).
4. Return structured publication table.

## Human setup (when needed)
- If files are embedded behind UI components, guide user through download steps and continue from local files.

## Quality checks
- Keep publication date and source institution.
- Avoid mixing RIA studies with unrelated news posts.
