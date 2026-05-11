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
