# BigMart Outlet Performance and Expansion Decision System
# Business Context
# BigMart plans to optimize its outlet network by identifying underperforming stores and evaluating potential expansion strategies based on historical performance data.
# Problem Statement
# Create an OutletPerformanceAnalyzer that supports data-driven outlet expansion and shutdown decisions.
# Business Requirements
# Calculate:
# Outlet age using establishment year
# Average sales per product per outlet
# Sales density adjusted by outlet size
# Compare performance across:
# Outlet sizes
# Outlet types
# Outlet age groups
# Identify:
# Consistently underperforming outlets
# High-potential outlet categories
# Simulate an expansion scenario:
# Assume new outlets of top-performing types
# Estimate projected revenue contribution
# Technical Constraints
# Use NumPy for:
# Normalization of sales metrics
# Rolling or window-based averages
# Use Pandas for:
# Multi-level grouping
# Custom aggregation functions
# Outliers must be handled using statistical logic.
# Visualization Requirements
# Matplotlib:
# Bar plot of outlet size versus average sales
# Plotly:
# Interactive heatmap of outlet type versus outlet size
# Color intensity represents average sales
# OOP Constraints
# Use composition between analyzer and data processing classes
# Use class methods for configuration management
# Implement custom exceptions for invalid outlet data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
file = pd.read_csv("bigmart.csv")
df = pd.DataFrame(file)
# print(file)
df['Outlet_Establishment_Year'] = pd.to_numeric(df['Outlet_Establishment_Year'], errors='coerce')
current_year = date.today().year
df['years_established'] = current_year - df['Outlet_Establishment_Year']
print(df['years_established'])#outlet age using establishment year
avg_sales =df.groupby([df["Item_Type"],df["Outlet_Identifier"]])["Item_Outlet_Sales"].mean().reset_index()
print(avg_sales)# average sales per product per outlet
sales_density = df["Item_Outlet_Sales"] / (df["Item_Outlet_Sales"] ** 2)
print(sales_density)# sales density adjusted by outlet size
#2.performnace
def get_age_group(age):
    if age < 20: return 'New'
    elif age <= 30: return 'Mid-Age'
    else: return 'Old'
df['Age_Group'] = df['years_established'].apply(get_age_group)
size_compare = df.groupby('Outlet_Size')['Item_Outlet_Sales'].mean()
type_compare = df.groupby('Outlet_Type')['Item_Outlet_Sales'].mean()
age_compare = df.groupby('Age_Group')['Item_Outlet_Sales'].mean()
print("Size Performance:\n", size_compare)
print("\nType Performance:\n", type_compare)
print("\nAge Group Performance:\n", age_compare)

#consistently underperforming outlets
underperformers = df.groupby('Outlet_Identifier')['Item_Outlet_Sales'].mean().nsmallest(3)
print(underperformers)

#high potential outlet categories
high_potential = df.groupby('Outlet_Type')['Item_Outlet_Sales'].mean().nlargest(1)
print(high_potential)
type_performance = df.groupby('Outlet_Type')['Item_Outlet_Sales'].mean()
top_type = type_performance.idxmax() 
print("top_type",top_type)
avg_sales_per_store = type_performance.max()
num_new_stores = 10  
projected_revenue = avg_sales_per_store * num_new_stores
print(f"Top Performing Type: {top_type}")
print(f"Average Sales per {top_type}:{avg_sales_per_store:.2f}")
print(f"Simulation")
print(f"Projected Revenue for {num_new_stores} new stores:{projected_revenue:.2f}")
#matplotlib
import matplotlib.pyplot as plt
size_perf = df.copy()
size_perf['Outlet_Size'] = size_perf['Outlet_Size'].fillna('Unknown')
avg_sales_by_size = size_perf.groupby('Outlet_Size')['Item_Outlet_Sales'].mean().sort_values()
plt.figure(figsize=(8, 5))
avg_sales_by_size.plot(kind='bar')
plt.title('How Store Size Impacts Sales')
plt.xlabel('Store Size')
plt.ylabel('Average Sales ')
plt.show()








