"""
Simple Budget Tracker
Author: Shivansh Tripathi

This program allows users to:
1. Add expenses with strict input validation
2. View all expenses
3. View expense totals by category

Key concepts used:
- Functions
- Input validation loops
- Lists & dictionaries
- File persistence (JSON)
- Clean separation of logic
"""

import json
from datetime import datetime

DATA_FILE = "expenses.json"


# ---------- Utility Functions ----------

def load_expenses():
    """Load expenses from file if it exists"""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    """Save expenses to file"""
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def get_valid_date():
    """
    Force user to enter a valid date in YYYY-MM-DD format.
    Keeps prompting until valid input is provided.
    """
    while True:
        date_input = input("Date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD (e.g. 2025-12-06).")


def get_valid_amount():
    """
    Force user to enter a valid numeric amount.
    Rejects non-numbers and negative values.
    """
    while True:
        amount_input = input("Amount (in dollars): ")
        try:
            amount = float(amount_input)
            if amount <= 0:
                raise ValueError
            return round(amount, 2)
        except ValueError:
            print("❌ Please enter a valid positive number (e.g. 12.50).")


# ---------- Core Features ----------

def add_expense(expenses):
    """Add a new expense with full validation"""
    print("\n--- Add Expense ---")

    date = get_valid_date()
    category = input("Category (food, transport, school, etc.): ").strip().lower()
    amount = get_valid_amount()

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("✅ Expense added successfully!")


def view_expenses(expenses):
    """Display all recorded expenses"""
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ${exp['amount']:.2f}")


def view_summary_by_category(expenses):
    """Display total spending grouped by category"""
    print("\n--- Summary by Category ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}

    for exp in expenses:
        category = exp["category"]
        summary[category] = summary.get(category, 0) + exp["amount"]

    for category, total in summary.items():
        print(f"{category.title()}: ${total:.2f}")


# ---------- Main Menu Loop ----------

def main():
    expenses = load_expenses()

    while True:
        print("\n=== Simple Budget Tracker ===")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. View summary by category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary_by_category(expenses)
        elif choice == "4":
            print("Progress saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")


if __name__ == "__main__":
    main()
