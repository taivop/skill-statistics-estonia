#!/usr/bin/env python3
"""
Analysis 2: Tax Policy Impacts on Economic Activity
Examines relationship between tax policy changes and retail sales
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
from scipy import stats

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

# Load data
print("Loading data...")

with open('tax_revenues_monthly.json', 'r') as f:
    tax_monthly = json.load(f)

with open('tax_revenues_quarterly.json', 'r') as f:
    tax_quarterly = json.load(f)

with open('retail_sales.json', 'r') as f:
    retail_sales = json.load(f)

with open('cpi_monthly.json', 'r') as f:
    cpi_data = json.load(f)


# Process monthly tax revenue data
print("Processing tax revenue data...")
tax_df_list = []

# Parse JSON-stat2 format
if 'dimension' in tax_monthly:
    # Get dimension info
    tax_type_dim = tax_monthly['dimension']['Maksu liik']
    period_dim = tax_monthly['dimension']['Vaatlusperiood']

    # Extract values
    values = tax_monthly['value']

    # Build dataframe - data is organized per size array [1, 6, 311]
    # Period varies fastest, then tax type, then indicator
    idx = 0
    for tax_key in sorted(tax_type_dim['category']['index'].keys(),
                          key=lambda x: tax_type_dim['category']['index'][x]):
        tax_label = tax_type_dim['category']['label'][tax_key]

        for period_key in sorted(period_dim['category']['index'].keys(),
                                key=lambda x: period_dim['category']['index'][x]):
            period_label = period_dim['category']['label'][period_key]

            if idx < len(values):
                value = values[idx]
                # Parse date from period (e.g., "2020 January" -> "2020-01")
                try:
                    parts = period_label.split()
                    if len(parts) == 2:
                        year = parts[0]
                        month_name = parts[1]
                        month_map = {
                            'January': '01', 'February': '02', 'March': '03', 'April': '04',
                            'May': '05', 'June': '06', 'July': '07', 'August': '08',
                            'September': '09', 'October': '10', 'November': '11', 'December': '12'
                        }
                        month = month_map.get(month_name, '01')
                        date_str = f"{year}-{month}"

                        tax_df_list.append({
                            'date': date_str,
                            'tax_type': tax_label,
                            'value': value if value is not None else np.nan
                        })
                except Exception as e:
                    print(f"Warning: Could not parse date '{period_label}': {e}")
            idx += 1

tax_df = pd.DataFrame(tax_df_list)
tax_df['date'] = pd.to_datetime(tax_df['date'])

# Pivot to wide format
tax_wide = tax_df.pivot(index='date', columns='tax_type', values='value')


# Process quarterly retail sales data
print("Processing retail sales data...")
retail_df_list = []

if 'dimension' in retail_sales:
    period_dim = retail_sales['dimension']['Vaatlusperiood']
    values = retail_sales['value']

    idx = 0
    for period_key in period_dim['category']['index'].keys():
        period_label = period_dim['category']['label'][period_key]

        if idx < len(values) and values[idx] is not None:
            # Parse quarter (e.g., "2020Q1" -> "2020-03")
            if 'Q' in period_label:
                year = period_label[:4]
                quarter = period_label[-1]
                q_map = {'1': '03', '2': '06', '3': '09', '4': '12'}
                date_str = f"{year}-{q_map[quarter]}"
            else:
                date_str = period_label

            retail_df_list.append({
                'date': date_str,
                'value': values[idx]
            })
        idx += 1

retail_df = pd.DataFrame(retail_df_list)
retail_df['date'] = pd.to_datetime(retail_df['date'])
retail_df.set_index('date', inplace=True)
retail_df.columns = ['Retail Sales Index']


# Process CPI data
print("Processing CPI data...")
cpi_df_list = []

if 'dimension' in cpi_data:
    year_dim = cpi_data['dimension']['Aasta']
    month_dim = cpi_data['dimension']['Kuu']
    values = cpi_data['value']

    idx = 0
    for year_key in year_dim['category']['index'].keys():
        year_label = year_dim['category']['label'][year_key]

        for month_key in month_dim['category']['index'].keys():
            month_label = month_dim['category']['label'][month_key]
            month_num = str(int(month_key)).zfill(2)

            if idx < len(values) and values[idx] is not None:
                date_str = f"{year_label}-{month_num}"
                cpi_df_list.append({
                    'date': date_str,
                    'value': values[idx]
                })
            idx += 1

cpi_df = pd.DataFrame(cpi_df_list)
cpi_df['date'] = pd.to_datetime(cpi_df['date'])
cpi_df.set_index('date', inplace=True)
cpi_df.columns = ['CPI YoY Change (%)']


# Convert monthly tax data to quarterly for comparison with retail sales
tax_wide_quarterly = tax_wide.resample('QE').sum()

# Convert quarterly index to match retail sales format (first day of last month in quarter)
# QE creates dates like 2020-03-31, we want 2020-03-01
# Create new index by replacing day with 01
tax_wide_quarterly.index = pd.to_datetime(tax_wide_quarterly.index.strftime('%Y-%m-01'))

# Merge datasets for analysis
merged = pd.DataFrame(index=retail_df.index)
merged['Retail Sales Index'] = retail_df['Retail Sales Index']

# Add tax data (quarterly sums)
for col in tax_wide_quarterly.columns:
    merged[col] = tax_wide_quarterly[col]

# Add CPI (quarterly average)
cpi_quarterly = cpi_df.resample('QE').mean()
cpi_quarterly.index = pd.to_datetime(cpi_quarterly.index.strftime('%Y-%m-01'))
merged['CPI YoY Change (%)'] = cpi_quarterly['CPI YoY Change (%)']

# Filter to recent period (2015-2025) for focused analysis
merged_recent = merged[merged.index >= '2015-01-01'].copy()

# Calculate year-over-year changes for key metrics
merged_recent['Retail Sales YoY (%)'] = merged_recent['Retail Sales Index'].pct_change(4) * 100
merged_recent['Total Tax YoY (%)'] = merged_recent['Taxes'].pct_change(4) * 100
merged_recent['VAT YoY (%)'] = merged_recent['..value added tax'].pct_change(4) * 100


# ===== VISUALIZATION 1: Tax Revenue Trends =====
print("Creating visualization 1: Tax revenue trends...")
fig, axes = plt.subplots(2, 1, figsize=(16, 10))

# Plot 1: Total tax revenue and VAT over time
ax1 = axes[0]
ax1_twin = ax1.twinx()

# Total taxes on left axis
line1 = ax1.plot(merged_recent.index, merged_recent['Taxes'] / 1000,
                 color='#2E86AB', linewidth=2.5, marker='o', markersize=4,
                 label='Total Tax Revenue')

# VAT on right axis
line2 = ax1_twin.plot(merged_recent.index, merged_recent['..value added tax'] / 1000,
                      color='#A23B72', linewidth=2.5, marker='s', markersize=4,
                      label='VAT Revenue')

# Motor vehicle tax on right axis (if available)
if '..motor vehicle tax' in merged_recent.columns:
    line3 = ax1_twin.plot(merged_recent.index, merged_recent['..motor vehicle tax'],
                          color='#F18F01', linewidth=2.5, marker='^', markersize=4,
                          label='Motor Vehicle Tax')

# Formatting
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Total Tax Revenue (Million EUR)', fontsize=12, fontweight='bold', color='#2E86AB')
ax1_twin.set_ylabel('VAT Revenue (Million EUR)', fontsize=12, fontweight='bold', color='#A23B72')
ax1.tick_params(axis='y', labelcolor='#2E86AB')
ax1_twin.tick_params(axis='y', labelcolor='#A23B72')
ax1.set_title('Estonian State Budget Tax Revenues (2015-2025)', fontsize=14, fontweight='bold', pad=15)

# Add policy event markers
ax1.axvline(x=pd.Timestamp('2022-07-01'), color='red', linestyle='--', alpha=0.6, linewidth=2)
ax1.text(pd.Timestamp('2022-07-01'), ax1.get_ylim()[1] * 0.95,
         'VAT 20% → 22%\\n(Jul 2022)', rotation=0, ha='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax1.axvline(x=pd.Timestamp('2024-01-01'), color='red', linestyle='--', alpha=0.6, linewidth=2)
ax1.text(pd.Timestamp('2024-01-01'), ax1.get_ylim()[1] * 0.85,
         'Motor Vehicle\\nTax Intro\\n(Jan 2024)', rotation=0, ha='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax1.grid(True, alpha=0.3)
ax1_twin.grid(False)

# Combine legends
lines = line1 + line2
if '..motor vehicle tax' in merged_recent.columns:
    lines = lines + line3
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=10)


# Plot 2: Year-over-year growth rates
ax2 = axes[1]
ax2.plot(merged_recent.index, merged_recent['Total Tax YoY (%)'],
         color='#2E86AB', linewidth=2.5, marker='o', markersize=4,
         label='Total Tax Revenue YoY %')
ax2.plot(merged_recent.index, merged_recent['VAT YoY (%)'],
         color='#A23B72', linewidth=2.5, marker='s', markersize=4,
         label='VAT Revenue YoY %')

ax2.axhline(y=0, color='gray', linestyle='-', alpha=0.5, linewidth=1)
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Year-over-Year Change (%)', fontsize=12, fontweight='bold')
ax2.set_title('Tax Revenue Growth Rates (2015-2025)', fontsize=14, fontweight='bold', pad=15)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, alpha=0.3)

# Add policy event markers
ax2.axvline(x=pd.Timestamp('2022-07-01'), color='red', linestyle='--', alpha=0.6, linewidth=2)
ax2.axvline(x=pd.Timestamp('2024-01-01'), color='red', linestyle='--', alpha=0.6, linewidth=2)

plt.tight_layout()
plt.savefig('tax_revenue_trends.png', dpi=300, bbox_inches='tight')
print("Saved tax_revenue_trends.png")


# ===== VISUALIZATION 2: Retail Sales Response to Tax Changes =====
print("Creating visualization 2: Retail sales response...")
fig, axes = plt.subplots(2, 1, figsize=(16, 10))

# Plot 1: Retail sales index and CPI
ax1 = axes[0]
ax1_twin = ax1.twinx()

line1 = ax1.plot(merged_recent.index, merged_recent['Retail Sales Index'],
                 color='#06A77D', linewidth=2.5, marker='o', markersize=4,
                 label='Retail Sales Volume Index')

line2 = ax1_twin.plot(merged_recent.index, merged_recent['CPI YoY Change (%)'],
                      color='#D62246', linewidth=2.5, marker='s', markersize=4,
                      label='CPI YoY Change %')

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Retail Sales Index (2021=100)', fontsize=12, fontweight='bold', color='#06A77D')
ax1_twin.set_ylabel('CPI YoY Change (%)', fontsize=12, fontweight='bold', color='#D62246')
ax1.tick_params(axis='y', labelcolor='#06A77D')
ax1_twin.tick_params(axis='y', labelcolor='#D62246')
ax1.set_title('Retail Sales Performance and Inflation (2015-2025)', fontsize=14, fontweight='bold', pad=15)

# Add policy event markers
ax1.axvline(x=pd.Timestamp('2022-07-01'), color='red', linestyle='--', alpha=0.6, linewidth=2)
ax1.text(pd.Timestamp('2022-07-01'), ax1.get_ylim()[1] * 0.95,
         'VAT +2pp', rotation=0, ha='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax1.axvline(x=pd.Timestamp('2024-01-01'), color='red', linestyle='--', alpha=0.6, linewidth=2)
ax1.text(pd.Timestamp('2024-01-01'), ax1.get_ylim()[1] * 0.85,
         'Vehicle Tax', rotation=0, ha='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

ax1.grid(True, alpha=0.3)
ax1_twin.grid(False)

lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=10)


# Plot 2: Retail sales YoY change
ax2 = axes[1]
colors = ['#06A77D' if x >= 0 else '#D62246' for x in merged_recent['Retail Sales YoY (%)'].fillna(0)]
ax2.bar(merged_recent.index, merged_recent['Retail Sales YoY (%)'],
        color=colors, alpha=0.7, width=80)
ax2.axhline(y=0, color='gray', linestyle='-', alpha=0.5, linewidth=1)
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_ylabel('Year-over-Year Change (%)', fontsize=12, fontweight='bold')
ax2.set_title('Retail Sales Volume Growth (2015-2025)', fontsize=14, fontweight='bold', pad=15)
ax2.grid(True, alpha=0.3, axis='y')

# Add policy event markers
ax2.axvline(x=pd.Timestamp('2022-07-01'), color='red', linestyle='--', alpha=0.6, linewidth=2)
ax2.axvline(x=pd.Timestamp('2024-01-01'), color='red', linestyle='--', alpha=0.6, linewidth=2)

# Annotate key periods
ax2.text(pd.Timestamp('2023-01-01'), ax2.get_ylim()[0] * 0.9,
         '4-year decline period', rotation=0, ha='center', fontsize=10,
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

plt.tight_layout()
plt.savefig('retail_sales_response.png', dpi=300, bbox_inches='tight')
print("Saved retail_sales_response.png")


# ===== VISUALIZATION 3: Tax Revenue vs Retail Sales Correlation =====
print("Creating visualization 3: Tax-retail correlation...")

# Filter to complete data only
if 'Taxes' in merged_recent.columns and '..value added tax' in merged_recent.columns:
    analysis_df = merged_recent[['Retail Sales Index', 'Taxes', '..value added tax']].dropna()

    if len(analysis_df) > 2:
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        # Scatter plot: Retail sales vs Total tax
        ax1 = axes[0]
        ax1.scatter(analysis_df['Retail Sales Index'], analysis_df['Taxes'] / 1000,
                    alpha=0.6, s=80, c=range(len(analysis_df)), cmap='viridis')

        # Add trend line
        z = np.polyfit(analysis_df['Retail Sales Index'], analysis_df['Taxes'] / 1000, 1)
        p = np.poly1d(z)
        ax1.plot(analysis_df['Retail Sales Index'],
                 p(analysis_df['Retail Sales Index']),
                 "r--", alpha=0.8, linewidth=2)

        corr = analysis_df['Retail Sales Index'].corr(analysis_df['Taxes'])
        ax1.set_xlabel('Retail Sales Index', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Total Tax Revenue (Million EUR)', fontsize=12, fontweight='bold')
        ax1.set_title(f'Retail Sales vs Total Tax Revenue\\n(Correlation: {corr:.3f})',
                      fontsize=13, fontweight='bold')
        ax1.grid(True, alpha=0.3)

        # Scatter plot: Retail sales vs VAT
        ax2 = axes[1]
        ax2.scatter(analysis_df['Retail Sales Index'], analysis_df['..value added tax'] / 1000,
                    alpha=0.6, s=80, c=range(len(analysis_df)), cmap='plasma')

        z = np.polyfit(analysis_df['Retail Sales Index'], analysis_df['..value added tax'] / 1000, 1)
        p = np.poly1d(z)
        ax2.plot(analysis_df['Retail Sales Index'],
                 p(analysis_df['Retail Sales Index']),
                 "r--", alpha=0.8, linewidth=2)

        corr = analysis_df['Retail Sales Index'].corr(analysis_df['..value added tax'])
        ax2.set_xlabel('Retail Sales Index', fontsize=12, fontweight='bold')
        ax2.set_ylabel('VAT Revenue (Million EUR)', fontsize=12, fontweight='bold')
        ax2.set_title(f'Retail Sales vs VAT Revenue\\n(Correlation: {corr:.3f})',
                      fontsize=13, fontweight='bold')
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('tax_retail_correlation.png', dpi=300, bbox_inches='tight')
        print("Saved tax_retail_correlation.png")
    else:
        print("Warning: Insufficient data for correlation plot")
else:
    print("Warning: Tax data columns not found")


# ===== CALCULATE KEY STATISTICS =====
print("\n" + "="*80)
print("KEY FINDINGS")
print("="*80)

# Pre-VAT increase period (2020Q1-2022Q2)
pre_vat = merged_recent[(merged_recent.index >= '2020-01-01') &
                        (merged_recent.index < '2022-07-01')]
# Post-VAT increase period (2022Q3-2024Q4)
post_vat = merged_recent[(merged_recent.index >= '2022-07-01') &
                         (merged_recent.index < '2025-01-01')]

print("\n1. TAX REVENUE ANALYSIS:")
print(f"   Average quarterly total tax revenue (pre-VAT increase): €{pre_vat['Taxes'].mean()/1000:.1f}M")
print(f"   Average quarterly total tax revenue (post-VAT increase): €{post_vat['Taxes'].mean()/1000:.1f}M")
print(f"   Change: {((post_vat['Taxes'].mean() / pre_vat['Taxes'].mean()) - 1) * 100:.1f}%")

print(f"\n   Average quarterly VAT revenue (pre-increase): €{pre_vat['..value added tax'].mean()/1000:.1f}M")
print(f"   Average quarterly VAT revenue (post-increase): €{post_vat['..value added tax'].mean()/1000:.1f}M")
print(f"   Change: {((post_vat['..value added tax'].mean() / pre_vat['..value added tax'].mean()) - 1) * 100:.1f}%")

print("\n2. RETAIL SALES ANALYSIS:")
print(f"   Average retail sales index (pre-VAT increase): {pre_vat['Retail Sales Index'].mean():.1f}")
print(f"   Average retail sales index (post-VAT increase): {post_vat['Retail Sales Index'].mean():.1f}")
print(f"   Change: {((post_vat['Retail Sales Index'].mean() / pre_vat['Retail Sales Index'].mean()) - 1) * 100:.1f}%")

# Peak to trough analysis
peak_retail = merged_recent['Retail Sales Index'].max()
peak_date = merged_recent['Retail Sales Index'].idxmax()
trough_retail = merged_recent[merged_recent.index >= '2021-01-01']['Retail Sales Index'].min()
trough_date = merged_recent[merged_recent.index >= '2021-01-01']['Retail Sales Index'].idxmin()

print(f"\n   Peak retail sales: {peak_retail:.1f} ({peak_date.strftime('%Y Q%q')})")
print(f"   Trough retail sales (post-2021): {trough_retail:.1f} ({trough_date.strftime('%Y Q%q')})")
print(f"   Decline from peak: {((trough_retail / peak_retail) - 1) * 100:.1f}%")

# Latest data
latest = merged_recent.iloc[-1]
latest_date = merged_recent.index[-1]
print(f"\n3. LATEST DATA ({latest_date.strftime('%Y Q%q')}):")
print(f"   Retail Sales Index: {latest['Retail Sales Index']:.1f}")
print(f"   Retail Sales YoY: {latest['Retail Sales YoY (%)']:.1f}%")
print(f"   CPI YoY: {latest['CPI YoY Change (%)']:.1f}%")
print(f"   Total Tax Revenue: €{latest['Taxes']/1000:.1f}M")
print(f"   VAT Revenue: €{latest['..value added tax']/1000:.1f}M")

# 4-year decline validation
decline_start = merged_recent[merged_recent.index >= '2022-01-01']
consecutive_declines = (decline_start['Retail Sales YoY (%)'] < 0).sum()
print(f"\n4. FOUR-YEAR DECLINE VALIDATION:")
print(f"   Quarters with YoY decline since 2022: {consecutive_declines} out of {len(decline_start)}")
print(f"   Proportion: {consecutive_declines/len(decline_start)*100:.1f}%")

# Export summary data
summary_data = merged_recent[['Retail Sales Index', 'Taxes', '..value added tax',
                              'CPI YoY Change (%)', 'Retail Sales YoY (%)',
                              'Total Tax YoY (%)', 'VAT YoY (%)']].copy()
summary_data.to_csv('analysis_data.csv')
print("\n" + "="*80)
print("Saved analysis_data.csv")
print("\nAnalysis complete!")
