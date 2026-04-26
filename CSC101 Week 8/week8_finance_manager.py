# Week 8: Smart Personal Finance Manager

def load_transactions(filename):
    """Read lines from a transaction file safely."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return []

def process_transactions(lines):
    """
    Convert lines like 'Coffee,-4.50' into dictionaries:
    {'name': 'Coffee', 'amount': -4.50}
    """
    transactions = []

    for line in lines:
        # Skip invalid lines
        if "," not in line:
            print(f"Skipping invalid line: {line}")
            continue

        name, amount_str = line.split(",", 1)

        try:
            amount = float(amount_str)
        except ValueError:
            print(f"Invalid amount in line: {line}")
            continue

        transactions.append({
            "name": name.strip(),
            "amount": amount
        })

    return transactions


def show_summary(transactions):
    """Calculate and display totals for income, expenses, and net balance."""
    total_income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    total_expenses = sum(t["amount"] for t in transactions if t["amount"] < 0)
    net_balance = total_income + total_expenses

    print("\n Summary")
    print("=" * 30)
    print(f"Total Income:   ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance:    ${net_balance:.2f}")


def main():
    print("Personal Finance Manager")
    print("=" * 30)

    filename = "transactions.txt"
    raw_lines = load_transactions(filename)

    if not raw_lines:
        print("No data to process!")
        return

    transactions = process_transactions(raw_lines)
    show_summary(transactions)


main()