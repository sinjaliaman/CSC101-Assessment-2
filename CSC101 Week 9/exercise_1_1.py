''' Exercise Set 1: Sales Data Analysis '''


''' Practice Exercise 1.1: Sales Performance by Region'''
import pandas as pd

# Load the sales data
sales_df = pd.read_csv('sales_data.csv')

# Clean currency columns (remove $ and convert to float)
sales_df['Total_Sale'] = sales_df['Total_Sale'].replace('[\$,]', '', regex=True).astype(float)

# Group by region and calculate metrics
summary = sales_df.groupby('Region').agg(
    Total_Sales=('Total_Sale', 'sum'),
    Average_Sale=('Total_Sale', 'mean'),
    Transaction_Count=('Total_Sale', 'count')
).reset_index()

# Format numbers for presentation
summary['Total_Sales'] = summary['Total_Sales'].map('${:,.2f}'.format)
summary['Average_Sale'] = summary['Average_Sale'].map('${:,.2f}'.format)

# Display manager‑friendly output
print("\n=== Regional Sales Performance Summary ===")
for _, row in summary.iterrows():
    print(f"""
Region: {row['Region']}
- Total Sales: {row['Total_Sales']}
- Average Sale Amount: {row['Average_Sale']}
- Number of Transactions: {row['Transaction_Count']}
""")
print("==========================================")

#====================================================================================================================#
''' Practice 1.2: Top performing Products '''
# Clean numeric fields
sales_df['Quantity'] = sales_df['Quantity'].replace('[\$,]', '', regex=True).astype(float)
sales_df['Unit_Price'] = sales_df['Unit_Price'].replace('[\$,]', '', regex=True).astype(float)
sales_df['Total_Sale'] = sales_df['Total_Sale'].replace('[\$,]', '', regex=True).astype(float)

# --- PRODUCT‑LEVEL SUMMARY ---
product_summary = sales_df.groupby('Product').agg(
    Total_Revenue=('Total_Sale', 'sum'),
    Units_Sold=('Quantity', 'sum'),
    Avg_Unit_Price=('Unit_Price', 'mean')   # proxy for profit margin
).reset_index()

# Sort by revenue and margin
top_revenue = product_summary.sort_values(by='Total_Revenue', ascending=False)
top_margin = product_summary.sort_values(by='Avg_Unit_Price', ascending=False)

# Format for presentation
product_summary['Total_Revenue'] = product_summary['Total_Revenue'].map('${:,.2f}'.format)
product_summary['Avg_Unit_Price'] = product_summary['Avg_Unit_Price'].map('${:,.2f}'.format)

print("\n=== Product Performance Summary ===")
print(product_summary.to_string(index=False))

print("\n=== Highest Revenue Products (Top 5) ===")
print(top_revenue.head(5)[['Product', 'Total_Revenue', 'Units_Sold']].to_string(index=False))

print("\n=== Highest Profit-Margin Products (Top 5 by Unit Price) ===")
print(top_margin.head(5)[['Product', 'Avg_Unit_Price', 'Units_Sold']].to_string(index=False))
