"""
Simple Budget Tracker
Author: Shivansh Tripathi
Description:
A command-line Python application that allows users to track daily expenses,
validate inputs, store data, and view spending summaries by category.
"""

from datetime import datetime

# -------------------------------
# In-memory storage for expenses
# -------------------------------
expenses = []

# -------------------------------
# Helper Functions
# -------------------------------

def get_valid_date():
    """
    Prompt user until a valid date (YYYY-MM-DD) is entered.
    """
    while True:
        date_input = input("Date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD (e.g. 2025-12-06).")

def get_valid_amount():
    """
    Prompt user until a valid positive number is entered.
    """
    while True:
        amount_input = input("Amount (in dollars): ").strip()
        try:
            amount = float(amount_input)
            if amount <= 0:
                raise ValueError
            return round(amount, 2)
        except ValueError:
            print("❌ Please enter a valid number (e.g. 12.50).")

# -------------------------------
# Core Features
# -------------------------------

def add_expense():
    """
    Add a new expense with full validation.
    """
    print("\n--- Add Expense ---")
    date = get_valid_date()
    category = input("Category (food, transport, school, etc.): ").strip().lower()
    amount = get_valid_amount()

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })

    print("✅ Expense added successfully!")

def view_all_expenses():
    """
    Display all recorded expenses.
    """
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    for exp in expenses:
        print(f"{exp['date']} | {exp['category']} | ${exp['amount']:.2f}")

def view_summary_by_category():
    """
    Display total spending grouped by category.
    """
    print("\n--- Summary by Category ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    summary = {}
    for exp in expenses:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]

    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")

# -------------------------------
# Main Menu Loop
# -------------------------------

def main():
    print("Welcome to the Simple Budget Tracker!")

    while True:
        print("\n=== Simple Budget Tracker ===")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. View summary by category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all_expenses()
        elif choice == "3":
            view_summary_by_category()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")

# -------------------------------
# Program Entry Point
# -------------------------------

if __name__ == "__main__":
    main()
