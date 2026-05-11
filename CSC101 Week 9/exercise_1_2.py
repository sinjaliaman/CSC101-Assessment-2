''' Practice Exercise 1.2: Top Performing Products '''

import pandas as pd

# Load CSV
df = pd.read_csv("sales_data.csv")

# Clean Quantity column
df["Quantity"] = df["Quantity"].astype(str).str.replace("$", "", regex=False).str.strip().astype(int)

# Clean Unit_Price and Total_Sale
df["Unit_Price"] = df["Unit_Price"].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)
df["Total_Sale"] = df["Total_Sale"].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)

# Recalculate revenue (optional)
df["Calculated_Revenue"] = df["Quantity"] * df["Unit_Price"]

# Group by product
product_summary = df.groupby("Product").agg(
    Total_Units_Sold=("Quantity", "sum"),
    Total_Revenue=("Total_Sale", "sum"),
    Average_Unit_Price=("Unit_Price", "mean")
).reset_index()

# Show product summary
print("\nProduct summary (units, revenue, average price):")
print(product_summary)

# Top 5 by revenue
top5_by_revenue = product_summary.sort_values(by="Total_Revenue", ascending=False).head(5)
print("\nTop 5 products by total revenue:")
print(top5_by_revenue)

# Top 5 by units sold
top5_by_units = product_summary.sort_values(by="Total_Units_Sold", ascending=False).head(5)
print("\nTop 5 products by total units sold:")
print(top5_by_units)

# Highest profit margin proxy
highest_margin_product = product_summary.sort_values(by="Average_Unit_Price", ascending=False).head(1)
print("\nProduct with highest profit margin proxy (highest average unit price):")
print(highest_margin_product)

# Final conclusions
print("\n--- Conclusions ---")
print("Top 5 products by total revenue:")
for _, row in top5_by_revenue.iterrows():
    print(f"- {row['Product']}: Revenue = ${row['Total_Revenue']:.2f}, Units Sold = {row['Total_Units_Sold']}")

print("\nTop 5 products by total units sold:")
for _, row in top5_by_units.iterrows():
    print(f"- {row['Product']}: Units Sold = {row['Total_Units_Sold']}, Revenue = ${row['Total_Revenue']:.2f}")

best = highest_margin_product.iloc[0]
print(f"\nProduct with highest profit margin proxy (by average unit price):")
print(f"- {best['Product']} with average unit price of ${best['Average_Unit_Price']:.2f}")
