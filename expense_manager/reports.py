"""Terminal reporting functions for expense data."""

from .expenses import totals_by_category
from .models import Expense


def view_expenses(expenses: list[Expense]) -> None:
    """Display all expenses in a formatted table.

    Display a message and return immediately when no expenses
    are available.
    """
    if not expenses:
        print("No expenses found.")
        return

    print()
    print(
        f"{'ID':<5}"
        f"{'Description':<20}"
        f"{'Category':<15}"
        f"{'Amount':>12}"
    )
    print("-" * 52)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['description']:<20}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:>11.2f}"
        )


def view_by_category(expenses: list[Expense]) -> None:
    """Display total spending grouped by expense category.

    Display a message and return immediately when no expense
    data is available.
    """
    totals: dict[str, float] = totals_by_category(expenses)

    if not totals:
        print("No expenses found.")
        return

    print("\nSpending by category:")

    for category, total in totals.items():
        print(f"{category}: ₹{total:.2f}")

