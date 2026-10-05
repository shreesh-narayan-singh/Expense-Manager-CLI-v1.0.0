"""Command-line entry point for the Expense Manager application."""

from expense_manager.logging_config import configure_logging

from expense_manager.expenses import (
    add_expense,
    calculate_total,
    delete_expense,
)
from expense_manager.reports import (
    view_by_category,
    view_expenses,
)
from expense_manager.storage import (
    load_expenses,
    save_expenses,
)

import logging

logger = logging.getLogger(__name__)

def show_menu() -> None:
    """Display the main Expense Manager menu."""
    print()
    print("=" * 30)
    print("       EXPENSE MANAGER")
    print("=" * 30)
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. View by category")
    print("5. Delete expense")
    print("6. Exit")


def main() -> None:
    """Run the Expense Manager command-line application."""
    expenses = load_expenses()

    while True:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            if add_expense(expenses):
                save_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total = calculate_total(expenses)
            print(f"Total spending: ₹{total:.2f}")

        elif choice == "4":
            view_by_category(expenses)

        elif choice == "5":
            if not expenses:
                print("No expenses to delete.")
                continue

            view_expenses(expenses)

            try:
                expense_id = int(
                    input("\nEnter expense ID to delete: ")
                )

            except ValueError:
                print("Please enter a valid ID.")
                continue

            if delete_expense(expenses, expense_id):
                save_expenses(expenses)
                print("Expense deleted.")

            else:
                print("Expense not found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    configure_logging()
    logger.info(
        "Application started",
        extra={"event": "application_started"},
    )

    try:
        main()
    finally:
        logger.info(
            "Application stopped",
            extra={"event": "application_stopped"},
        )

