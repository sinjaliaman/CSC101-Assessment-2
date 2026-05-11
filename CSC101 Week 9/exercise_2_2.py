import csv
from statistics import mean, stdev

# -----------------------------
# 1. Load transactions
# -----------------------------
categories = {}

with open("transactions.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = float(row["Amount"].replace("$", ""))
        category = row["Category"]

        # Ignore refunds (negative amounts)
        if amount < 0:
            continue

        if category not in categories:
            categories[category] = []
        categories[category].append(amount)

# -----------------------------
# 2. Calculate average monthly spending
# -----------------------------
avg_spending = {cat: mean(amounts) for cat, amounts in categories.items()}

# -----------------------------
# 3. Identify high‑variation categories
# -----------------------------
variation = {}
for cat, amounts in categories.items():
    if len(amounts) > 1:
        variation[cat] = stdev(amounts)
    else:
        variation[cat] = 0  # No variation with one transaction

high_variation = {cat: var for cat, var in variation.items() if var > mean(variation.values())}

# -----------------------------
# 4. Suggest realistic budgets
#    (average + 10% buffer)
# -----------------------------
suggested_budget = {cat: round(avg * 1.10, 2) for cat, avg in avg_spending.items()}

# -----------------------------
# 5. Identify categories to reduce
#    (above overall average spending)
# -----------------------------
overall_avg = mean(avg_spending.values())
reduce_categories = [cat for cat, avg in avg_spending.items() if avg > overall_avg]

# -----------------------------
# 6. Print results
# -----------------------------
print("Average Monthly Spending by Category:")
for cat, avg in avg_spending.items():
    print(f" - {cat}: ${avg:.2f}")

print("\nHigh Variation Categories (Inconsistent Spending):")
for cat in high_variation:
    print(f" - {cat}")

print("\nSuggested Monthly Budget (Avg + 10% buffer):")
for cat, budget in suggested_budget.items():
    print(f" - {cat}: ${budget:.2f}")

print("\nCategories Where Spending Might Be Reduced:")
for cat in reduce_categories:
    print(f" - {cat}")
