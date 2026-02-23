#!/usr/bin/env python3
"""
Process unemployment and CPI data from Statistics Estonia and create visualization.
"""
import json
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Read unemployment data (1993-2019)
with open('unemployment_1993_2019.json', 'r') as f:
    unemp_old = json.load(f)

# Read unemployment data (2018-2024)
with open('unemployment_2018_2024.json', 'r') as f:
    unemp_new = json.load(f)

# Read CPI data
with open('cpi_data.json', 'r') as f:
    cpi_data = json.load(f)

# Extract unemployment data (1993-2019)
unemployment_old = {}
if 'dimension' in unemp_old and 'Aasta' in unemp_old['dimension']:
    years_old = unemp_old['dimension']['Aasta']['category']['label']
    values_old = unemp_old['value']
    for i, (year_code, year_label) in enumerate(years_old.items()):
        if i < len(values_old):
            unemployment_old[int(year_label)] = values_old[i]

# Extract unemployment data (2018-2024)
unemployment_new = {}
if 'dimension' in unemp_new and 'Vaatlusperiood' in unemp_new['dimension']:
    years_new = unemp_new['dimension']['Vaatlusperiood']['category']['label']
    values_new = unemp_new['value']
    for i, (year_code, year_label) in enumerate(years_new.items()):
        if i < len(values_new):
            unemployment_new[int(year_label)] = values_new[i]

# Merge unemployment data (prefer newer data for overlapping years)
unemployment = {**unemployment_old, **unemployment_new}

# Extract and process CPI data (calculate annual averages)
if 'dimension' in cpi_data:
    years_cpi = cpi_data['dimension']['Aasta']['category']['label']
    months_cpi = cpi_data['dimension']['Kuu']['category']['label']
    values_cpi = cpi_data['value']

    # Group by year and calculate averages
    cpi_by_year = defaultdict(list)
    idx = 0
    for year_code, year_label in years_cpi.items():
        for month_code, month_label in months_cpi.items():
            if idx < len(values_cpi) and values_cpi[idx] is not None:
                cpi_by_year[int(year_label)].append(values_cpi[idx])
            idx += 1

    # Calculate annual averages
    cpi_annual = {year: np.mean(values) for year, values in cpi_by_year.items()}

    # Convert to index where 1998 = 100 (already in the data)
    # The data is already indexed to 1997=100, so we'll keep it as is

# Find common years for both datasets
common_years = sorted(set(unemployment.keys()) & set(cpi_annual.keys()))
print(f"Data range: {min(common_years)} to {max(common_years)}")
print(f"Total years: {len(common_years)}")

# Prepare data for plotting
years = common_years
unemployment_values = [unemployment[y] for y in years]
cpi_values = [cpi_annual[y] for y in years]

# Create the visualization
fig, ax1 = plt.subplots(figsize=(14, 7))

# Plot unemployment rate on left y-axis
color1 = '#2E86AB'
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Unemployment Rate (%)', color=color1, fontsize=12, fontweight='bold')
line1 = ax1.plot(years, unemployment_values, color=color1, linewidth=2.5,
                 label='Unemployment Rate', marker='o', markersize=4)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_ylim(0, max(unemployment_values) * 1.1)

# Plot CPI on right y-axis
ax2 = ax1.twinx()
color2 = '#A23B72'
ax2.set_ylabel('Consumer Price Index (1997=100)', color=color2, fontsize=12, fontweight='bold')
line2 = ax2.plot(years, cpi_values, color=color2, linewidth=2.5,
                 label='Consumer Price Index', marker='s', markersize=4)
ax2.tick_params(axis='y', labelcolor=color2)

# Title and legend
plt.title('Estonia: Unemployment Rate and Cost of Living (1998-2024)',
          fontsize=14, fontweight='bold', pad=20)

# Combine legends
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=10, framealpha=0.9)

# Add some key event annotations
# 2008-2009 Financial Crisis
if 2009 in years:
    idx_2009 = years.index(2009)
    ax1.annotate('2008-2009\nFinancial Crisis',
                xy=(2009, unemployment_values[idx_2009]),
                xytext=(2009, unemployment_values[idx_2009] + 3),
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7),
                arrowprops=dict(arrowstyle='->', color='black', lw=1))

# 2020 COVID-19
if 2020 in years:
    idx_2020 = years.index(2020)
    ax1.annotate('COVID-19\nPandemic',
                xy=(2020, unemployment_values[idx_2020]),
                xytext=(2018, unemployment_values[idx_2020] + 2),
                ha='center', fontsize=9,
                bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.7),
                arrowprops=dict(arrowstyle='->', color='black', lw=1))

plt.tight_layout()
plt.savefig('unemployment_and_cpi_chart.png', dpi=300, bbox_inches='tight')
print("Chart saved as unemployment_and_cpi_chart.png")

# Export data to CSV
import csv
with open('unemployment_and_cpi_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Year', 'Unemployment Rate (%)', 'Consumer Price Index (1997=100)'])
    for year in years:
        writer.writerow([year, unemployment[year], cpi_annual[year]])
print("Data exported to unemployment_and_cpi_data.csv")

# Print summary statistics
print("\n=== SUMMARY STATISTICS ===")
print(f"Unemployment Rate:")
print(f"  - Average: {np.mean(unemployment_values):.2f}%")
print(f"  - Minimum: {np.min(unemployment_values):.2f}% (year {years[np.argmin(unemployment_values)]})")
print(f"  - Maximum: {np.max(unemployment_values):.2f}% (year {years[np.argmax(unemployment_values)]})")
print(f"\nConsumer Price Index (1997=100):")
print(f"  - Start (1998): {cpi_annual[1998]:.2f}")
print(f"  - End (2024): {cpi_annual[max(years)]:.2f}")
print(f"  - Total increase: {((cpi_annual[max(years)] / cpi_annual[1998]) - 1) * 100:.1f}%")
print(f"  - Average annual growth: {(((cpi_annual[max(years)] / cpi_annual[1998]) ** (1/(max(years)-1998))) - 1) * 100:.2f}%")
