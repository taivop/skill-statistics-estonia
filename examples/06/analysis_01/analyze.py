#!/usr/bin/env python3
"""
Analysis 1: Consumer Confidence vs Economic Indicators
Examines relationship between consumer confidence and macro indicators
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from datetime import datetime

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load data
with open('consumer_confidence.json', 'r') as f:
    cc_data = json.load(f)

with open('gdp_growth.json', 'r') as f:
    gdp_data = json.load(f)

with open('unemployment.json', 'r') as f:
    unemp_data = json.load(f)

with open('retail_sales.json', 'r') as f:
    retail_data = json.load(f)

with open('cpi.json', 'r') as f:
    cpi_data = json.load(f)

# Process consumer confidence data (monthly 2010-2020)
cc_values = []
cc_dates = []
for i, val in enumerate(cc_data['value']):
    year_idx = cc_data['dimension']['Vaatlusperiood']['category']['index'][str(i)] if 'dimension' in cc_data else None
    month_idx = cc_data['dimension']['Kuu']['category']['index'][str(i)] if 'dimension' in cc_data else None

    # Simpler approach: parse from data structure
    if val is not None:
        cc_values.append(val)

# Alternative: extract from structured format
cc_df_data = []
idx = 0
for year in range(2010, 2021):
    for month in range(1, 13):
        if idx < len(cc_data['value']) and cc_data['value'][idx] is not None:
            cc_df_data.append({
                'date': f'{year}-{month:02d}',
                'value': cc_data['value'][idx]
            })
        idx += 1

cc_df = pd.DataFrame(cc_df_data)
cc_df['date'] = pd.to_datetime(cc_df['date'])
cc_df.set_index('date', inplace=True)

# Convert to quarterly for comparison with other indicators
cc_quarterly = cc_df.resample('Q').mean()

# Process GDP growth data (quarterly)
gdp_df_data = []
for val, year_key, quarter_key in zip(
    gdp_data['value'],
    [k for k in gdp_data['dimension']['Aasta']['category']['index'].keys()],
    [k for k in gdp_data['dimension']['Kvartal']['category']['index'].keys()]
):
    if val is not None:
        year_val = gdp_data['dimension']['Aasta']['category']['label'][year_key]
        quarter_val = gdp_data['dimension']['Kvartal']['category']['label'][quarter_key]

        # Map quarter to month
        q_map = {'1st quarter': '03', '2nd quarter': '06', '3rd quarter': '09', '4th quarter': '12'}
        if quarter_val in q_map:
            date_str = f"{year_val}-{q_map[quarter_val]}"
            gdp_df_data.append({'date': date_str, 'value': val})

gdp_df = pd.DataFrame(gdp_df_data)
gdp_df['date'] = pd.to_datetime(gdp_df['date'])
gdp_df.set_index('date', inplace=True)
gdp_df = gdp_df[~gdp_df.index.duplicated(keep='first')]

# Process unemployment data (quarterly, thousands)
unemp_df_data = []
for val, period_key in zip(
    unemp_data['value'],
    [k for k in unemp_data['dimension']['Vaatlusperiood']['category']['index'].keys()]
):
    if val is not None:
        period_val = unemp_data['dimension']['Vaatlusperiood']['category']['label'][period_key]
        # Parse "2010 Q1" format
        parts = period_val.split()
        if len(parts) == 2:
            year = parts[0]
            quarter = parts[1]
            q_map = {'Q1': '03', 'Q2': '06', 'Q3': '09', 'Q4': '12'}
            if quarter in q_map:
                date_str = f"{year}-{q_map[quarter]}"
                unemp_df_data.append({'date': date_str, 'value': val})

unemp_df = pd.DataFrame(unemp_df_data)
unemp_df['date'] = pd.to_datetime(unemp_df['date'])
unemp_df.set_index('date', inplace=True)
unemp_df = unemp_df[~unemp_df.index.duplicated(keep='first')]

# Process retail sales data
retail_df_data = []
for val, period_key in zip(
    retail_data['value'],
    [k for k in retail_data['dimension']['Vaatlusperiood']['category']['index'].keys()]
):
    if val is not None:
        period_val = retail_data['dimension']['Vaatlusperiood']['category']['label'][period_key]
        parts = period_val.split()
        if len(parts) == 2:
            year = parts[0]
            quarter = parts[1]
            q_map = {'Q1': '03', 'Q2': '06', 'Q3': '09', 'Q4': '12'}
            if quarter in q_map:
                date_str = f"{year}-{q_map[quarter]}"
                retail_df_data.append({'date': date_str, 'value': val})

retail_df = pd.DataFrame(retail_df_data)
retail_df['date'] = pd.to_datetime(retail_df['date'])
retail_df.set_index('date', inplace=True)
retail_df = retail_df[~retail_df.index.duplicated(keep='first')]

# Process CPI data (annual %) - convert to quarterly
cpi_df_data = []
for val, period_key in zip(
    cpi_data['value'],
    [k for k in cpi_data['dimension']['Vaatlusperiood']['category']['index'].keys()]
):
    if val is not None:
        period_val = cpi_data['dimension']['Vaatlusperiood']['category']['label'][period_key]
        # Could be various formats, try to parse
        try:
            if 'Q' in period_val:
                parts = period_val.split()
                if len(parts) == 2:
                    year = parts[0]
                    quarter = parts[1]
                    q_map = {'Q1': '03', 'Q2': '06', 'Q3': '09', 'Q4': '12'}
                    if quarter in q_map:
                        date_str = f"{year}-{q_map[quarter]}"
                        cpi_df_data.append({'date': date_str, 'value': val})
            else:
                # Annual data - assign to Q4
                date_str = f"{period_val}-12"
                cpi_df_data.append({'date': date_str, 'value': val})
        except:
            pass

cpi_df = pd.DataFrame(cpi_df_data)
if len(cpi_df) > 0:
    cpi_df['date'] = pd.to_datetime(cpi_df['date'])
    cpi_df.set_index('date', inplace=True)
    cpi_df = cpi_df[~cpi_df.index.duplicated(keep='first')]

# Merge all data
merged = pd.DataFrame({
    'Consumer Confidence': cc_quarterly['value'],
})

# Filter to 2010-2020 period where we have confidence data
gdp_filtered = gdp_df[(gdp_df.index >= '2010-01-01') & (gdp_df.index <= '2020-12-31')]
unemp_filtered = unemp_df[(unemp_df.index >= '2010-01-01') & (unemp_df.index <= '2020-12-31')]
retail_filtered = retail_df[(retail_df.index >= '2010-01-01') & (retail_df.index <= '2020-12-31')]

merged['GDP Growth (%)'] = gdp_filtered['value']
merged['Unemployment (000s)'] = unemp_filtered['value']
merged['Retail Sales Index'] = retail_filtered['value']

# Drop rows with missing values
merged_clean = merged.dropna()

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Consumer Confidence over time
ax1 = axes[0, 0]
ax1.plot(merged.index, merged['Consumer Confidence'], marker='o', linewidth=2, markersize=4)
ax1.axhline(y=0, color='r', linestyle='--', alpha=0.5, label='Neutral (0)')
ax1.set_title('Consumer Confidence Index (2010-2020)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year')
ax1.set_ylabel('Confidence Index')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 2. Confidence vs GDP Growth
ax2 = axes[0, 1]
ax2.scatter(merged_clean['GDP Growth (%)'], merged_clean['Consumer Confidence'], alpha=0.6, s=50)
z = np.polyfit(merged_clean['GDP Growth (%)'], merged_clean['Consumer Confidence'], 1)
p = np.poly1d(z)
ax2.plot(merged_clean['GDP Growth (%)'], p(merged_clean['GDP Growth (%)']), "r--", alpha=0.8, linewidth=2)
corr = merged_clean['Consumer Confidence'].corr(merged_clean['GDP Growth (%)'])
ax2.set_title(f'Confidence vs GDP Growth\\n(Correlation: {corr:.3f})', fontsize=14, fontweight='bold')
ax2.set_xlabel('GDP Growth (%)')
ax2.set_ylabel('Consumer Confidence')
ax2.grid(True, alpha=0.3)

# 3. Confidence vs Unemployment
ax3 = axes[1, 0]
ax3.scatter(merged_clean['Unemployment (000s)'], merged_clean['Consumer Confidence'], alpha=0.6, s=50, color='orange')
z = np.polyfit(merged_clean['Unemployment (000s)'], merged_clean['Consumer Confidence'], 1)
p = np.poly1d(z)
ax3.plot(merged_clean['Unemployment (000s)'], p(merged_clean['Unemployment (000s)']), "r--", alpha=0.8, linewidth=2)
corr = merged_clean['Consumer Confidence'].corr(merged_clean['Unemployment (000s)'])
ax3.set_title(f'Confidence vs Unemployment\\n(Correlation: {corr:.3f})', fontsize=14, fontweight='bold')
ax3.set_xlabel('Unemployed Persons (000s)')
ax3.set_ylabel('Consumer Confidence')
ax3.grid(True, alpha=0.3)

# 4. Confidence vs Retail Sales
ax4 = axes[1, 1]
ax4.scatter(merged_clean['Retail Sales Index'], merged_clean['Consumer Confidence'], alpha=0.6, s=50, color='green')
z = np.polyfit(merged_clean['Retail Sales Index'], merged_clean['Consumer Confidence'], 1)
p = np.poly1d(z)
ax4.plot(merged_clean['Retail Sales Index'], p(merged_clean['Retail Sales Index']), "r--", alpha=0.8, linewidth=2)
corr = merged_clean['Consumer Confidence'].corr(merged_clean['Retail Sales Index'])
ax4.set_title(f'Confidence vs Retail Sales\\n(Correlation: {corr:.3f})', fontsize=14, fontweight='bold')
ax4.set_xlabel('Retail Sales Volume Index')
ax4.set_ylabel('Consumer Confidence')
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('confidence_indicators.png', dpi=300, bbox_inches='tight')
print("Saved confidence_indicators.png")

# Create time series comparison plot
fig, ax1 = plt.subplots(figsize=(16, 8))

color = 'tab:blue'
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Consumer Confidence', color=color, fontsize=12)
ax1.plot(merged.index, merged['Consumer Confidence'], color=color, marker='o', linewidth=2, markersize=4, label='Consumer Confidence')
ax1.tick_params(axis='y', labelcolor=color)
ax1.axhline(y=0, color='gray', linestyle='--', alpha=0.5)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('GDP Growth (%)', color=color, fontsize=12)
ax2.plot(merged.index, merged['GDP Growth (%)'], color=color, marker='s', linewidth=2, markersize=4, label='GDP Growth')
ax2.tick_params(axis='y', labelcolor=color)

# Add vertical line for financial crisis and COVID
ax1.axvline(x=pd.Timestamp('2008-09-15'), color='black', linestyle=':', alpha=0.5, linewidth=2)
ax1.text(pd.Timestamp('2008-09-15'), merged['Consumer Confidence'].max(), 'Financial Crisis', rotation=90, verticalalignment='bottom')

ax1.axvline(x=pd.Timestamp('2020-03-01'), color='purple', linestyle=':', alpha=0.5, linewidth=2)
ax1.text(pd.Timestamp('2020-03-01'), merged['Consumer Confidence'].max(), 'COVID-19', rotation=90, verticalalignment='bottom')

plt.title('Consumer Confidence and GDP Growth (2010-2020)', fontsize=14, fontweight='bold', pad=20)
fig.tight_layout()
plt.savefig('time_series_comparison.png', dpi=300, bbox_inches='tight')
print("Saved time_series_comparison.png")

# Calculate correlation matrix
corr_matrix = merged_clean.corr()
print("\\nCorrelation Matrix:")
print(corr_matrix)

# Save correlation matrix
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm', center=0,
            square=True, linewidths=1, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix: Consumer Confidence and Economic Indicators',
          fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
print("Saved correlation_matrix.png")

# Export data to CSV
merged.to_csv('analysis_data.csv')
print("Saved analysis_data.csv")

# Print summary statistics
print("\\nSummary Statistics:")
print(merged.describe())

print("\\nAnalysis complete!")
