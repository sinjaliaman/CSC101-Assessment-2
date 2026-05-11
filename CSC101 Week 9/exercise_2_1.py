''' Practice Exercise 2.1: Spending Trend Analysis '''

import pandas as pd

# -----------------------------
# 1. LOAD & CLEAN THE DATA
# -----------------------------
df = pd.read_csv("transactions.csv")

# Remove $ sign and convert Amount to float
df["Amount"] = df["Amount"].str.replace("$", "").astype(float)

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Create a positive-spending column (ignore refunds)
df["Spending"] = df["Amount"].apply(lambda x: x if x > 0 else 0)

# -----------------------------
# 2. SPENDING BY DAY OF WEEK
# -----------------------------
df["DayOfWeek"] = df["Date"].dt.day_name()

spending_by_day = df.groupby("DayOfWeek")["Spending"].sum()
print("Spending by day of week:")
print(spending_by_day)

# -----------------------------
# 3. IS SPENDING INCREASING?
# -----------------------------
daily_totals = df.groupby("Date")["Spending"].sum()

print("\nDaily spending totals:")
print(daily_totals)

# Simple trend check: compare first 5 days vs last 5 days
first_period = daily_totals.head(5).mean()
last_period = daily_totals.tail(5).mean()

print("\nAverage spending (first 5 days):", first_period)
print("Average spending (last 5 days):", last_period)

if last_period > first_period:
    print("\nSpending has increased over time.")
else:
    print("\nSpending has NOT increased over time.")

# -----------------------------
# 4. UNUSUAL SPENDING PATTERNS
# -----------------------------
mean_spend = daily_totals.mean()
std_spend = daily_totals.std()

# Flag days where spending > mean + 1.5*std
threshold = mean_spend + 1.5 * std_spend
unusual_days = daily_totals[daily_totals > threshold]

print("\nUnusual spending days:")
print(unusual_days)
