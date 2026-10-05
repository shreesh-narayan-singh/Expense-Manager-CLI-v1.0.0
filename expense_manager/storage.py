"""JSON persistence for expense records."""

import json
from pathlib import Path

from .models import Expense


DATA_FILE = Path("data") / "expenses.json"


def load_expenses() -> list[Expense]:
    """Load expenses from the JSON data file.

    Return an empty list if the file does not exist
    or contains invalid JSON.
    """
    try:
        with DATA_FILE.open(
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_expenses(
    expenses: list[Expense],
) -> None:
    """Write all expenses to the JSON data file."""
    with DATA_FILE.open(
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            expenses,
            file,
            indent=4,
        )