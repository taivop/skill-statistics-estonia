## Examples

| Example | Question | Report |
| --- | --- | --- |
| 01 | Make a chart of cumulative salary distribution of men vs women, latest data available | [examples/01](./01/ANALYSIS.md) |
| 02 | Make a single chart with unemployment and cost of living over time, as long time horizon as possible | [examples/02](./02/ANALYSIS.md) |
| 03 | Create a chart comparing GDP per capita across Estonian counties for the most recent year | [examples/03](./03/ANALYSIS.md) |
| 04 | Visualize Estonia's population pyramid by age groups and sex for the latest available year | [examples/04](./04/ANALYSIS.md) |
| 05 | Create a time series chart showing birth rates and average maternal education level over the past 20 years | [examples/05](./05/ANALYSIS.md) |
| 06 | Comprehensive economic study: consumer confidence, tax policy, retail trends, food inflation, vehicle market (5 sub-analyses) | [examples/06](./06/ANALYSIS.md) |

Examples 01 and 02 were run with Claude Code 2.1.3 and 03, 04 and 05 with Codex 0.77.0. Example 06 was run with Claude Sonnet 4.5 on January 17, 2026.

## Prompts

### Examples 01-05

The prompt used to run examples 01-05 was:

```
You are analyzing Statistics Estonia data. For this analysis:

1. Use the statistics-estonia skill (get_metadata.py script and API access). The skill is described in SKILL.md in /Users/taivo/repos/skill-statistics-estonia.
2. Create comprehensive analysis in ANALYSIS.md including:
   - Executive summary
   - Data sources and methodology
   - Key findings with markdown tables
   - Data visualizations (save as PNG files)
   - Conclusions and insights

1. Save all outputs under examples/<folder_number>:
   - ANALYSIS.md (main report)
   - *.png (charts/plots using matplotlib or similar)
   - *.csv (any data exports)
   - *.json (any API responses worth saving)

4. Embed visualizations in ANALYSIS.md using relative paths: ![Chart](./chart.png)

5. Use markdown tables for structured data presentation.

folder_number: {folder_number}
Your task: {task}
```

### Example 06

The prompt used to run example 06 was:

```
Consider the topics discussed in this article:
https://www.err.ee/1609913176/juri-kao-valitsus-tahab-eesti-majandust-ilusamaks-raakida

Identify the proposed study questions. Propose 5 options for methodology how to do it, what strong empirical economists would do, do cursory research of previous literature on similar topics.

Then identify potential data sources, incl Statistics Estonia (skill in this repo) and others, be creative, including datasets you could create through scraping.

Then run all the analyses from scratch, each in a separate folder for neat separation. For each, produce a markdown report including figures and tables where relevant. Be straight to the point without extra fluff, but include relevant context.
```
