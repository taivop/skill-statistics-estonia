#!/usr/bin/env python3
"""
Analysis 5: Vehicle Market Response to Taxation
Examines the impact of Estonia's vehicle registration tax on market size and structure
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
plt.rcParams['font.size'] = 10

# Load data
print("Loading data...")

with open('vehicle_registrations.json', 'r') as f:
    reg_data = json.load(f)

with open('vehicle_registrations_monthly.json', 'r') as f:
    reg_monthly_data = json.load(f)

with open('motor_vehicle_sales_index.json', 'r') as f:
    sales_data = json.load(f)

with open('vehicle_tax_revenue.json', 'r') as f:
    tax_data = json.load(f)

# Process annual registration data
print("Processing annual registration data...")
years = list(reg_data['dimension']['Aasta']['category']['label'].values())

reg_annual_data = []
# Data structure: [vehicle_type=1, years=33, indicators=2, months=1]
# Values are ordered: year varies slowest, indicator varies fastest
idx = 0
for year in years:
    for ind_code, ind_name in reg_data['dimension']['Näitaja']['category']['label'].items():
        value = reg_data['value'][idx]
        if value is not None:
            reg_annual_data.append({
                'year': int(year),
                'indicator': ind_name,
                'value': value
            })
        idx += 1

reg_annual_df = pd.DataFrame(reg_annual_data)

# Process monthly registration data
print("Processing monthly registration data...")
monthly_data_list = []

# Extract dimensions
years_monthly = list(reg_monthly_data['dimension']['Aasta']['category']['label'].values())
months = list(reg_monthly_data['dimension']['Kuu']['category']['label'].values())
indicators = list(reg_monthly_data['dimension']['Näitaja']['category']['label'].values())

idx = 0
for year in years_monthly:
    for month_code, month_name in reg_monthly_data['dimension']['Kuu']['category']['label'].items():
        for ind_code, ind_name in reg_monthly_data['dimension']['Näitaja']['category']['label'].items():
            value = reg_monthly_data['value'][idx]
            if value is not None and month_name != 'Ascending total':
                # Parse month name to number
                month_map = {
                    'January': 1, 'February': 2, 'March': 3, 'April': 4,
                    'May': 5, 'June': 6, 'July': 7, 'August': 8,
                    'September': 9, 'October': 10, 'November': 11, 'December': 12
                }
                if month_name in month_map:
                    date_str = f"{year}-{month_map[month_name]:02d}"
                    monthly_data_list.append({
                        'date': date_str,
                        'indicator': ind_name,
                        'value': value
                    })
            idx += 1

reg_monthly_df = pd.DataFrame(monthly_data_list)
reg_monthly_df['date'] = pd.to_datetime(reg_monthly_df['date'])

# Process sales index data
print("Processing sales index data...")
sales_data_list = []

month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}

for period_code, period_name in sales_data['dimension']['Vaatlusperiood']['category']['label'].items():
    for ind_code, ind_name in sales_data['dimension']['Näitaja']['category']['label'].items():
        # Construct index for value array
        period_idx = sales_data['dimension']['Vaatlusperiood']['category']['index'][period_code]
        ind_idx = sales_data['dimension']['Näitaja']['category']['index'][ind_code]

        # Calculate linear index: indicator varies fastest
        linear_idx = period_idx * 2 + ind_idx

        value = sales_data['value'][linear_idx]
        if value is not None:
            # Parse period (format: "2001 January")
            parts = period_name.split()
            if len(parts) == 2:
                year = int(parts[0])
                month_name = parts[1]
                if month_name in month_map:
                    month = month_map[month_name]
                    date_str = f"{year}-{month:02d}"
                    sales_data_list.append({
                        'date': date_str,
                        'indicator': ind_name,
                        'value': value
                    })

sales_df = pd.DataFrame(sales_data_list)
sales_df['date'] = pd.to_datetime(sales_df['date'])

# Process tax revenue data
print("Processing tax revenue data...")
tax_data_list = []
years_tax = list(tax_data['dimension']['Aasta']['category']['label'].values())
tax_types = list(tax_data['dimension']['Keskkonnamaks']['category']['label'].values())

idx = 0
for tax_code, tax_name in tax_data['dimension']['Keskkonnamaks']['category']['label'].items():
    for year in years_tax:
        value = tax_data['value'][idx]
        if value is not None:
            tax_data_list.append({
                'year': int(year),
                'tax_type': tax_name,
                'revenue_millions': value
            })
        idx += 1

tax_df = pd.DataFrame(tax_data_list)

# Calculate key metrics
print("\n=== KEY METRICS ===")

# Annual registrations for specific years
reg_total = reg_annual_df[reg_annual_df['indicator'] == 'Registered vehicles']
reg_new = reg_annual_df[reg_annual_df['indicator'] == 'Registered new vehicles']

# Compare 2024 vs 2025
if 2024 in reg_total['year'].values and 2025 in reg_total['year'].values:
    reg_2024 = reg_total[reg_total['year'] == 2024]['value'].iloc[0]
    reg_2025 = reg_total[reg_total['year'] == 2025]['value'].iloc[0]
    decline_pct = ((reg_2025 - reg_2024) / reg_2024) * 100
    print(f"Total registrations 2024: {reg_2024:,.0f}")
    print(f"Total registrations 2025: {reg_2025:,.0f}")
    print(f"Change: {decline_pct:.1f}%")

# Compare 2023 vs 2024 (pre-tax surge)
if 2023 in reg_total['year'].values:
    reg_2023 = reg_total[reg_total['year'] == 2023]['value'].iloc[0]
    surge_2024 = ((reg_2024 - reg_2023) / reg_2023) * 100
    print(f"\nTotal registrations 2023: {reg_2023:,.0f}")
    print(f"Surge in 2024 (pre-tax): {surge_2024:.1f}%")

# Tax revenue analysis
vehicle_tax_total = tax_df[tax_df['tax_type'] == 'Transport taxes']
reg_fee = tax_df[tax_df['tax_type'] == '..car registration fee']

if len(reg_fee) > 0:
    print(f"\nCar registration fee revenue (latest available):")
    latest_year = reg_fee['year'].max()
    latest_revenue = reg_fee[reg_fee['year'] == latest_year]['revenue_millions'].iloc[0]
    print(f"  {latest_year}: €{latest_revenue:.1f}M")

# Sales volume index change
sales_volume = sales_df[sales_df['indicator'] == 'Volume index (deflated turnover), 2021 = 100']
if len(sales_volume) > 0:
    # Compare recent months
    recent = sales_volume[sales_volume['date'] >= '2024-01-01'].copy()
    if len(recent) > 0:
        avg_2024 = recent[recent['date'].dt.year == 2024]['value'].mean()
        avg_2025 = recent[recent['date'].dt.year == 2025]['value'].mean()
        if not pd.isna(avg_2024) and not pd.isna(avg_2025):
            volume_change = ((avg_2025 - avg_2024) / avg_2024) * 100
            print(f"\nSales volume index change:")
            print(f"  2024 avg: {avg_2024:.1f}")
            print(f"  2025 avg: {avg_2025:.1f}")
            print(f"  Change: {volume_change:.1f}%")

# VISUALIZATION 1: Annual Registration Trends
print("\nCreating Visualization 1: Annual Registration Trends...")
fig, ax1 = plt.subplots(figsize=(16, 8))

# Filter to recent years
reg_plot = reg_total[reg_total['year'] >= 2010].sort_values('year')
reg_new_plot = reg_new[reg_new['year'] >= 2010].sort_values('year')

color1 = 'tab:blue'
ax1.set_xlabel('Year', fontsize=14, fontweight='bold')
ax1.set_ylabel('Total Registrations', color=color1, fontsize=14, fontweight='bold')
line1 = ax1.plot(reg_plot['year'], reg_plot['value'],
                 marker='o', linewidth=3, markersize=8, color=color1,
                 label='Total Passenger Car Registrations')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, alpha=0.3)

# Mark the tax introduction
ax1.axvline(x=2025, color='red', linestyle='--', linewidth=3, alpha=0.7)
ax1.text(2025, ax1.get_ylim()[1] * 0.95, 'Vehicle Tax\nIntroduced\nJan 1, 2025',
         ha='center', va='top', fontsize=12, fontweight='bold',
         bbox=dict(boxstyle='round', facecolor='red', alpha=0.2))

# Add annotation for pre-tax surge
if 2024 in reg_plot['year'].values:
    reg_2024_val = reg_plot[reg_plot['year'] == 2024]['value'].iloc[0]
    ax1.annotate('Pre-tax\nBuying Surge',
                xy=(2024, reg_2024_val),
                xytext=(2022.5, reg_2024_val * 1.1),
                arrowprops=dict(arrowstyle='->', lw=2, color='green'),
                fontsize=11, fontweight='bold', color='green')

# Add annotation for post-tax collapse
if 2025 in reg_plot['year'].values:
    reg_2025_val = reg_plot[reg_plot['year'] == 2025]['value'].iloc[0]
    ax1.annotate('Post-tax\nMarket Collapse',
                xy=(2025, reg_2025_val),
                xytext=(2024.5, reg_2025_val * 0.7),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'),
                fontsize=11, fontweight='bold', color='red')

plt.title('Estonia: Passenger Car Registrations 2010-2025\nImpact of Vehicle Registration Tax',
          fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('registration_trends.png', dpi=300, bbox_inches='tight')
print("Saved registration_trends.png")
plt.close()

# VISUALIZATION 2: Monthly Registrations Around Tax Introduction
print("\nCreating Visualization 2: Monthly Registration Pattern...")
fig, ax = plt.subplots(figsize=(16, 8))

reg_monthly_total = reg_monthly_df[reg_monthly_df['indicator'] == 'Registered vehicles']
reg_monthly_plot = reg_monthly_total[reg_monthly_total['date'] >= '2023-01-01'].sort_values('date')

ax.plot(reg_monthly_plot['date'], reg_monthly_plot['value'],
        marker='o', linewidth=2, markersize=6, color='darkblue', label='Monthly Registrations')
ax.axvline(x=pd.Timestamp('2025-01-01'), color='red', linestyle='--', linewidth=3, alpha=0.7)
ax.axvspan(pd.Timestamp('2024-11-01'), pd.Timestamp('2024-12-31'),
           alpha=0.2, color='green', label='Pre-tax Rush Period')
ax.axvspan(pd.Timestamp('2025-01-01'), pd.Timestamp('2025-12-31'),
           alpha=0.2, color='red', label='Post-tax Period')

ax.text(pd.Timestamp('2025-01-01'), ax.get_ylim()[1] * 0.95,
        'Tax Introduced', ha='center', va='top', fontsize=12, fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

ax.set_xlabel('Month', fontsize=14, fontweight='bold')
ax.set_ylabel('Passenger Car Registrations', fontsize=14, fontweight='bold')
ax.set_title('Monthly Vehicle Registrations: Pre-tax Surge and Post-tax Collapse\n(2023-2025)',
             fontsize=16, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=11, loc='upper left')

plt.tight_layout()
plt.savefig('monthly_registrations.png', dpi=300, bbox_inches='tight')
print("Saved monthly_registrations.png")
plt.close()

# VISUALIZATION 3: Revenue vs Volume Trade-off
print("\nCreating Visualization 3: Revenue vs Volume Trade-off...")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7))

# Left panel: Registration volume over time
reg_recent = reg_total[reg_total['year'] >= 2015].sort_values('year')
bars1 = ax1.bar(reg_recent['year'], reg_recent['value'],
                color=['green' if y < 2024 else 'orange' if y == 2024 else 'red'
                       for y in reg_recent['year']], alpha=0.7)

ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Passenger Car Registrations', fontsize=12, fontweight='bold')
ax1.set_title('Market Volume: Before and After Tax', fontsize=14, fontweight='bold')
ax1.axhline(y=reg_recent[reg_recent['year'] <= 2023]['value'].mean(),
            color='blue', linestyle=':', linewidth=2, alpha=0.5,
            label='Pre-2024 Average')
ax1.legend()
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=9, fontweight='bold')

# Right panel: Tax revenue (if available)
transport_tax = tax_df[tax_df['tax_type'] == 'Transport taxes']
if len(transport_tax) > 0:
    tax_recent = transport_tax[transport_tax['year'] >= 2015].sort_values('year')
    bars2 = ax2.bar(tax_recent['year'], tax_recent['revenue_millions'],
                    color='darkgreen', alpha=0.7)

    ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax2.set_ylabel('Tax Revenue (€ millions)', fontsize=12, fontweight='bold')
    ax2.set_title('Transport Tax Revenue Over Time', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3, axis='y')

    # Add value labels
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'€{height:.0f}M',
                ha='center', va='bottom', fontsize=9, fontweight='bold')
else:
    ax2.text(0.5, 0.5, 'Tax revenue data not available\nfor recent years',
             ha='center', va='center', fontsize=14, transform=ax2.transAxes)
    ax2.set_title('Transport Tax Revenue', fontsize=14, fontweight='bold')

plt.suptitle('Estonia Vehicle Market: Volume vs Revenue Trade-off',
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('revenue_volume_tradeoff.png', dpi=300, bbox_inches='tight')
print("Saved revenue_volume_tradeoff.png")
plt.close()

# VISUALIZATION 4: Sales Volume Index Comparison
print("\nCreating Visualization 4: Sales Volume Index...")
fig, ax = plt.subplots(figsize=(16, 8))

sales_volume_plot = sales_df[sales_df['indicator'] == 'Volume index (deflated turnover), 2021 = 100']
sales_volume_plot = sales_volume_plot[sales_volume_plot['date'] >= '2018-01-01'].sort_values('date')

ax.plot(sales_volume_plot['date'], sales_volume_plot['value'],
        linewidth=2, color='purple', label='Motor Vehicle Sales Volume Index (2021=100)')
ax.axhline(y=100, color='gray', linestyle=':', linewidth=2, alpha=0.5, label='Baseline (2021=100)')
ax.axvline(x=pd.Timestamp('2025-01-01'), color='red', linestyle='--', linewidth=3, alpha=0.7,
          label='Tax Introduction')

# Add shaded regions
ax.axvspan(pd.Timestamp('2020-03-01'), pd.Timestamp('2020-06-01'),
           alpha=0.15, color='orange', label='COVID-19 Lockdown')
ax.axvspan(pd.Timestamp('2024-11-01'), pd.Timestamp('2024-12-31'),
           alpha=0.2, color='green')

ax.set_xlabel('Date', fontsize=14, fontweight='bold')
ax.set_ylabel('Volume Index (2021 = 100)', fontsize=14, fontweight='bold')
ax.set_title('Motor Vehicle Sales Volume Index: Market Activity Over Time',
             fontsize=16, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10, loc='best')

plt.tight_layout()
plt.savefig('sales_volume_index.png', dpi=300, bbox_inches='tight')
print("Saved sales_volume_index.png")
plt.close()

# Export processed data
print("\nExporting processed data...")
reg_total.to_csv('annual_registrations.csv', index=False)
reg_monthly_total.to_csv('monthly_registrations.csv', index=False)
sales_volume_plot.to_csv('sales_volume_index.csv', index=False)
tax_df.to_csv('vehicle_tax_revenue.csv', index=False)

print("\n=== ANALYSIS COMPLETE ===")
print("\nFiles created:")
print("  - registration_trends.png")
print("  - monthly_registrations.png")
print("  - revenue_volume_tradeoff.png")
print("  - sales_volume_index.png")
print("  - annual_registrations.csv")
print("  - monthly_registrations.csv")
print("  - sales_volume_index.csv")
print("  - vehicle_tax_revenue.csv")
