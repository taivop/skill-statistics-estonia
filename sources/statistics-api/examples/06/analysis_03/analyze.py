#!/usr/bin/env python3
"""
Analysis 3: Retail Sector Performance Trends (Four-Year Decline)
Analyzes retail sales volume index and decomposition by commodity group
"""

import json
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from itertools import product

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

# Helper function to convert JSON-stat2 to DataFrame
def jsonstat_to_dataframe(data):
    """Convert JSON-stat2 format to pandas DataFrame."""
    if "id" in data and "size" in data:
        dims = data["id"]
        sizes = data["size"]
    else:
        dims = data["dimension"]["id"]
        sizes = data["dimension"]["size"]

    # Expand values if sparse
    def expand_values(values, total_size):
        if isinstance(values, dict):
            expanded = [None] * total_size
            for key, value in values.items():
                expanded[int(key)] = value
            return expanded
        return values

    values = expand_values(data["value"], math.prod(sizes))

    dim_codes = {}
    dim_labels = {}

    for dim in dims:
        cat = data["dimension"][dim]["category"]
        idx = cat["index"]
        if isinstance(idx, dict):
            codes = [None] * len(idx)
            for code, pos in idx.items():
                codes[pos] = code
        else:
            codes = list(idx)
        labels = cat.get("label", {})
        label_list = [labels.get(code, code) for code in codes]
        dim_codes[dim] = codes
        dim_labels[dim] = label_list

    multipliers = []
    running = 1
    for size in reversed(sizes):
        multipliers.insert(0, running)
        running *= size

    records = []
    for idxs in product(*[range(size) for size in sizes]):
        flat_index = sum(idx * mult for idx, mult in zip(idxs, multipliers))
        value = values[flat_index]
        if value is None:
            continue
        record = {dim: dim_labels[dim][idx] for dim, idx in zip(dims, idxs)}
        record["value"] = value
        records.append(record)

    return pd.DataFrame(records)


# Load KM00338 - Retail Sales Volume Index
print("Loading KM00338 - Retail Sales Volume Index...")
with open('km00338_retail_sales_index.json', 'r') as f:
    retail_index_data = json.load(f)

retail_df = jsonstat_to_dataframe(retail_index_data)

# Parse period to year and quarter
retail_df['Period'] = retail_df['Vaatlusperiood']
retail_df['Year'] = retail_df['Period'].str[:4].astype(int)
retail_df['Quarter'] = retail_df['Period'].str.split(' ').str[1].str.replace('Q', '').astype(int)

# Create date column
retail_df['Date'] = pd.to_datetime(
    retail_df['Year'].astype(str) + '-' +
    (retail_df['Quarter'] * 3).astype(str) + '-01'
)

retail_df = retail_df.rename(columns={'value': 'Index'})
retail_df = retail_df[['Date', 'Period', 'Year', 'Quarter', 'Index']].sort_values('Date')

print(f"Retail sales index data: {len(retail_df)} quarters from {retail_df['Period'].min()} to {retail_df['Period'].max()}")

# Calculate year-over-year changes
retail_df['YoY_Change'] = retail_df['Index'].pct_change(4) * 100  # 4 quarters = 1 year

# Calculate cumulative change from 2021 baseline (index = 100)
retail_df['Change_from_2021'] = retail_df['Index'] - 100

# Load KM0061 - Retail sales by commodity group
print("\nLoading KM0061 - Retail sales by commodity group...")
with open('km0061_retail_by_commodity.json', 'r') as f:
    commodity_data = json.load(f)

commodity_df = jsonstat_to_dataframe(commodity_data)

# Clean up column names
commodity_df = commodity_df.rename(columns={
    'Vaatlusperiood': 'Period',
    'Kaubagrupp': 'Commodity_Group',
    'Tegevusala': 'Economic_Activity',
    'value': 'Sales_1000_EUR'
})

# Parse year from period
commodity_df['Year'] = commodity_df['Period'].astype(int)

# Filter to total retail trade activity
commodity_df_retail = commodity_df[
    commodity_df['Economic_Activity'] == 'Retail trade, except of motor vehicles and motorcycles'
].copy()

print(f"Commodity data: {len(commodity_df_retail)} records")
print(f"Commodity groups: {commodity_df_retail['Commodity_Group'].nunique()}")
print(f"Years: {commodity_df_retail['Year'].min()} to {commodity_df_retail['Year'].max()}")

# Calculate total sales by year and commodity group
commodity_pivot = commodity_df_retail.pivot_table(
    index='Year',
    columns='Commodity_Group',
    values='Sales_1000_EUR',
    aggfunc='sum'
).fillna(0)

# Calculate year-over-year change for commodity groups
commodity_yoy = commodity_pivot.pct_change() * 100

# Print summary statistics
print("\n=== RETAIL SALES INDEX SUMMARY ===")
print(f"Latest value (2025 Q3): {retail_df.iloc[-1]['Index']:.2f}")
peak_2019_q4 = retail_df[retail_df['Period'] == '2019 Q4']['Index'].values
if len(peak_2019_q4) > 0:
    print(f"Pre-pandemic peak (2019 Q4): {peak_2019_q4[0]:.2f}")
else:
    print("Pre-pandemic peak (2019 Q4): Data not available")
print(f"2021 baseline: 100.00")
print(f"Change from 2021 baseline: {retail_df.iloc[-1]['Index'] - 100:.2f} points")

# Identify four-year decline period
recent_data = retail_df[retail_df['Year'] >= 2020].copy()
print("\n=== YEAR-OVER-YEAR CHANGES (2020-2025) ===")
yearly_avg = recent_data.groupby('Year').agg({
    'Index': 'mean',
    'YoY_Change': 'mean'
}).round(2)
print(yearly_avg)

# Check for consecutive years of decline
print("\n=== FOUR-YEAR DECLINE ANALYSIS ===")
for year in range(2021, 2026):
    year_data = recent_data[recent_data['Year'] == year]
    if len(year_data) > 0:
        avg_yoy = year_data['YoY_Change'].mean()
        avg_index = year_data['Index'].mean()
        print(f"{year}: Avg Index = {avg_index:.2f}, Avg YoY = {avg_yoy:+.2f}%")

# ==========================================
# VISUALIZATION 1: Retail Sales Index Over Time (2001-2025)
# ==========================================

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 12))

# Panel 1: Full time series
ax1.plot(retail_df['Date'], retail_df['Index'], linewidth=2.5, color='#2E86AB', marker='o', markersize=3)
ax1.axhline(y=100, color='black', linestyle='--', alpha=0.5, linewidth=1.5, label='2021 Baseline (100)')

# Mark key events
ax1.axvline(x=pd.Timestamp('2008-09-15'), color='red', linestyle=':', alpha=0.6, linewidth=2)
ax1.text(pd.Timestamp('2008-09-15'), ax1.get_ylim()[1]*0.95, 'Financial\nCrisis',
         rotation=0, ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

ax1.axvline(x=pd.Timestamp('2020-03-01'), color='purple', linestyle=':', alpha=0.6, linewidth=2)
ax1.text(pd.Timestamp('2020-03-01'), ax1.get_ylim()[1]*0.95, 'COVID-19',
         rotation=0, ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

ax1.axvline(x=pd.Timestamp('2022-02-24'), color='darkred', linestyle=':', alpha=0.6, linewidth=2)
ax1.text(pd.Timestamp('2022-02-24'), ax1.get_ylim()[1]*0.95, 'Ukraine\nWar',
         rotation=0, ha='center', fontsize=9, bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

ax1.set_title('Estonia Retail Sales Volume Index (2001-2025, Base Year 2021=100)',
              fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Index (2021 = 100)', fontsize=12)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3)

# Panel 2: Year-over-year change
colors = ['green' if x >= 0 else 'red' for x in retail_df['YoY_Change']]
ax2.bar(retail_df['Date'], retail_df['YoY_Change'], color=colors, alpha=0.7, width=80)
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.8, linewidth=1)

# Mark key events
ax2.axvline(x=pd.Timestamp('2020-03-01'), color='purple', linestyle=':', alpha=0.6, linewidth=2)
ax2.axvline(x=pd.Timestamp('2022-02-24'), color='darkred', linestyle=':', alpha=0.6, linewidth=2)

ax2.set_title('Year-over-Year Change in Retail Sales Volume (%)', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('YoY Change (%)', fontsize=12)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('retail_sales_index_timeseries.png', dpi=300, bbox_inches='tight')
print("\nSaved: retail_sales_index_timeseries.png")

# ==========================================
# VISUALIZATION 2: Recent Period Analysis (2019-2025)
# ==========================================

recent_period = retail_df[retail_df['Year'] >= 2019].copy()

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Panel 1: Index level
ax1 = axes[0, 0]
ax1.plot(recent_period['Date'], recent_period['Index'], linewidth=3, color='#2E86AB', marker='o', markersize=6)
ax1.axhline(y=100, color='black', linestyle='--', alpha=0.5, linewidth=1.5, label='2021 Baseline')

# Highlight pre-pandemic peak
peak_2019_data = retail_df[retail_df['Period'] == '2019 Q4']['Index'].values
if len(peak_2019_data) > 0:
    peak_2019 = peak_2019_data[0]
    ax1.axhline(y=peak_2019, color='green', linestyle='--', alpha=0.5, linewidth=1.5, label=f'2019 Q4 Peak ({peak_2019:.1f})')

ax1.set_title('Retail Sales Index (2019-2025)', fontsize=13, fontweight='bold')
ax1.set_xlabel('Quarter', fontsize=11)
ax1.set_ylabel('Index (2021 = 100)', fontsize=11)
ax1.legend(fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: Year-over-year change
ax2 = axes[0, 1]
colors = ['green' if x >= 0 else 'red' for x in recent_period['YoY_Change']]
ax2.bar(range(len(recent_period)), recent_period['YoY_Change'], color=colors, alpha=0.7)
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.8, linewidth=1)
ax2.set_title('YoY Change by Quarter (2019-2025)', fontsize=13, fontweight='bold')
ax2.set_xlabel('Quarter', fontsize=11)
ax2.set_ylabel('YoY Change (%)', fontsize=11)
ax2.set_xticks(range(0, len(recent_period), 4))
ax2.set_xticklabels([recent_period.iloc[i]['Period'] for i in range(0, len(recent_period), 4)], rotation=45)
ax2.grid(True, alpha=0.3, axis='y')

# Panel 3: Cumulative change from 2021
ax3 = axes[1, 0]
colors = ['green' if x >= 0 else 'red' for x in recent_period['Change_from_2021']]
ax3.bar(range(len(recent_period)), recent_period['Change_from_2021'], color=colors, alpha=0.7)
ax3.axhline(y=0, color='black', linestyle='-', alpha=0.8, linewidth=1)
ax3.set_title('Deviation from 2021 Baseline (Index Points)', fontsize=13, fontweight='bold')
ax3.set_xlabel('Quarter', fontsize=11)
ax3.set_ylabel('Change from Baseline', fontsize=11)
ax3.set_xticks(range(0, len(recent_period), 4))
ax3.set_xticklabels([recent_period.iloc[i]['Period'] for i in range(0, len(recent_period), 4)], rotation=45)
ax3.grid(True, alpha=0.3, axis='y')

# Panel 4: Rolling 4-quarter average
ax4 = axes[1, 1]
recent_period['Rolling_Avg'] = recent_period['Index'].rolling(window=4, center=False).mean()
ax4.plot(recent_period['Date'], recent_period['Index'], linewidth=2, alpha=0.5, label='Quarterly', color='lightblue')
ax4.plot(recent_period['Date'], recent_period['Rolling_Avg'], linewidth=3, label='4-Quarter MA', color='#2E86AB')
ax4.axhline(y=100, color='black', linestyle='--', alpha=0.5, linewidth=1.5)
ax4.set_title('Index with 4-Quarter Moving Average', fontsize=13, fontweight='bold')
ax4.set_xlabel('Quarter', fontsize=11)
ax4.set_ylabel('Index', fontsize=11)
ax4.legend(fontsize=9)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('retail_sales_recent_analysis.png', dpi=300, bbox_inches='tight')
print("Saved: retail_sales_recent_analysis.png")

# ==========================================
# VISUALIZATION 3: Seasonal Patterns
# ==========================================

fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Panel 1: Seasonal pattern by quarter
ax1 = axes[0]
quarterly_pattern = retail_df.groupby('Quarter')['Index'].mean()
ax1.bar(['Q1', 'Q2', 'Q3', 'Q4'], quarterly_pattern.values, color='#2E86AB', alpha=0.7)
ax1.set_title('Average Retail Sales Index by Quarter (2001-2025)', fontsize=13, fontweight='bold')
ax1.set_xlabel('Quarter', fontsize=11)
ax1.set_ylabel('Average Index', fontsize=11)
ax1.grid(True, alpha=0.3, axis='y')

# Panel 2: Quarter-over-quarter change distribution
ax2 = axes[1]
retail_df['QoQ_Change'] = retail_df['Index'].pct_change() * 100
qoq_by_quarter = retail_df.groupby('Quarter')['QoQ_Change'].mean()
colors = ['green' if x >= 0 else 'red' for x in qoq_by_quarter]
ax2.bar(['Q1', 'Q2', 'Q3', 'Q4'], qoq_by_quarter.values, color=colors, alpha=0.7)
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.8, linewidth=1)
ax2.set_title('Average Quarter-over-Quarter Change by Quarter', fontsize=13, fontweight='bold')
ax2.set_xlabel('Quarter', fontsize=11)
ax2.set_ylabel('Avg QoQ Change (%)', fontsize=11)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('retail_sales_seasonal_patterns.png', dpi=300, bbox_inches='tight')
print("Saved: retail_sales_seasonal_patterns.png")

# ==========================================
# VISUALIZATION 4: Commodity Group Breakdown
# ==========================================

if len(commodity_pivot) > 0:
    # Select recent years
    recent_commodity = commodity_pivot[commodity_pivot.index >= 2020]

    # Select main commodity groups (exclude totals)
    main_groups = ['Food', 'Alcoholic beverages and tobacco products',
                   'Manufactured goods', 'Clothing, woven materials, footwear',
                   'Motor vehicles, their parts and accessories', 'Automotive fuel']

    available_groups = [g for g in main_groups if g in recent_commodity.columns]

    if len(available_groups) > 0:
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        # Panel 1: Sales by commodity group
        recent_commodity[available_groups].plot(kind='bar', ax=ax1, width=0.8)
        ax1.set_title('Retail Sales by Commodity Group (2020-2024)', fontsize=13, fontweight='bold')
        ax1.set_xlabel('Year', fontsize=11)
        ax1.set_ylabel('Sales (Million EUR)', fontsize=11)
        ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
        ax1.grid(True, alpha=0.3, axis='y')
        ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0)

        # Panel 2: Market share evolution
        recent_commodity_pct = recent_commodity[available_groups].div(
            recent_commodity[available_groups].sum(axis=1), axis=0
        ) * 100

        recent_commodity_pct.plot(kind='area', stacked=True, ax=ax2, alpha=0.7)
        ax2.set_title('Market Share by Commodity Group (%)', fontsize=13, fontweight='bold')
        ax2.set_xlabel('Year', fontsize=11)
        ax2.set_ylabel('Market Share (%)', fontsize=11)
        ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
        ax2.grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        plt.savefig('retail_sales_commodity_breakdown.png', dpi=300, bbox_inches='tight')
        print("Saved: retail_sales_commodity_breakdown.png")

# ==========================================
# Export data for further analysis
# ==========================================

retail_df.to_csv('retail_sales_analysis_data.csv', index=False)
print("\nSaved: retail_sales_analysis_data.csv")

if len(commodity_pivot) > 0:
    commodity_pivot.to_csv('commodity_sales_by_year.csv')
    commodity_yoy.to_csv('commodity_yoy_change.csv')
    print("Saved: commodity_sales_by_year.csv")
    print("Saved: commodity_yoy_change.csv")

print("\n=== Analysis Complete ===")
print(f"Total visualizations created: 4")
print(f"Data exports: 3-5 CSV files")
