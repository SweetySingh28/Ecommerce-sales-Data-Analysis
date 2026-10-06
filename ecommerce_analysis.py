# E-Commerce Sales Data Analysis
# Author: Sweety Singh
# Institute: RV Institute of Technology
# Course: Data Analytics

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ecommerce_sales.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print(df.head())
print("\nShape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nSummary:\n", df.describe(numeric_only=True))

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
avg_order_value = total_sales / total_orders

print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ₹{avg_order_value:,.2f}")

# Category analysis
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
category_profit = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print("\nSales by Category:\n", category_sales)
print("\nProfit by Category:\n", category_profit)

# Region analysis
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Region:\n", region_sales)

# Monthly trend
monthly_sales = df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"].sum()
print("\nMonthly Sales:\n", monthly_sales)

# Product performance
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nTop Products:\n", product_sales.head(10))

# Visualizations
plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.savefig("sales_by_category.png", dpi=150)
plt.show()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Sales (₹)")
plt.tight_layout()
plt.savefig("sales_by_region.png", dpi=150)
plt.show()

plt.figure(figsize=(10,5))
monthly_sales.astype(float).plot(marker="o")
plt.title("Monthly Sales Trend")
plt.ylabel("Sales (₹)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=150)
plt.show()

print("\nTop 5 Insights:")
print("1. Compare categories to identify the strongest revenue contributors.")
print("2. Compare regional sales to identify high-performing markets.")
print("3. Use the monthly trend to identify seasonal peaks and weak periods.")
print("4. Product-level sales helps prioritize inventory and marketing.")
print("5. Profit should be considered alongside sales before making business decisions.")
