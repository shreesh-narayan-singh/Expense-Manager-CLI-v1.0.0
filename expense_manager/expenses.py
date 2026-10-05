"""Business logic for expense operations."""

from .models import Expense


def next_expense_id(expenses: list[Expense]) -> int:
    """Return the next available expense ID.

    Return 1 when the expense list is empty. Otherwise,
    return one greater than the highest existing expense ID.
    """
    if not expenses:
        return 1

    return max(expense["id"] for expense in expenses) + 1


def read_amount() -> float:
    """Prompt for and return a valid positive expense amount.

    Continue prompting until the user enters a valid number
    greater than zero.
    """
    while True:
        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def add_expense(expenses: list[Expense]) -> bool:
    """Create an expense from user input and add it to the list.

    Return True after the expense has been added successfully.
    """
    description = input("Description: ").strip()
    amount = read_amount()
    category = input("Category: ").strip()

    expense: Expense = {
        "id": next_expense_id(expenses),
        "description": description,
        "amount": amount,
        "category": category,
    }

    expenses.append(expense)
    print("Expense added successfully.")

    return True


def delete_expense(
    expenses: list[Expense],
    expense_id: int,
) -> bool:
    """Delete the expense with the given ID.

    Return True if an expense was deleted, otherwise return
    False if no matching expense exists.
    """
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            return True

    return False


def calculate_total(expenses: list[Expense]) -> float:
    """Return the total amount across all expenses."""
    return sum(expense["amount"] for expense in expenses)


def totals_by_category(
    expenses: list[Expense],
) -> dict[str, float]:
    """Return total spending grouped by expense category."""
    totals: dict[str, float] = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        totals[category] = totals.get(category, 0.0) + amount

    return totals
