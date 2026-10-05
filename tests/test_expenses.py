"""Tests for expense business logic."""

from unittest.mock import patch

import pytest

from expense_manager.expenses import (
    add_expense,
    calculate_total,
    delete_expense,
    next_expense_id,
    read_amount,
    totals_by_category,
)


@pytest.mark.parametrize(
    "expenses, expected",
    [
        (
            [],
            1,
        ),
        (
            [
                {
                    "id": 1,
                    "description": "Test",
                    "amount": 100.0,
                    "category": "Test",
                },
            ],
            2,
        ),
        (
            [
                {
                    "id": 2,
                    "description": "A",
                    "amount": 100.0,
                    "category": "Test",
                },
                {
                    "id": 8,
                    "description": "B",
                    "amount": 200.0,
                    "category": "Test",
                },
                {
                    "id": 4,
                    "description": "C",
                    "amount": 300.0,
                    "category": "Test",
                },
            ],
            9,
        ),
    ],
)
def test_next_expense_id(
    expenses,
    expected,
) -> None:
    """Return one greater than the highest existing ID."""
    assert next_expense_id(expenses) == expected


def test_calculate_total(sample_expenses) -> None:
    """Calculate the total amount across all expenses."""
    result = calculate_total(sample_expenses)

    assert result == pytest.approx(900.0)


def test_calculate_total_empty_list() -> None:
    """Return zero when there are no expenses."""
    assert calculate_total([]) == 0


def test_totals_by_category(sample_expenses) -> None:
    """Group expense totals by category."""
    result = totals_by_category(sample_expenses)

    assert result == {
        "Food": 600.0,
        "Travel": 300.0,
    }


def test_totals_by_category_empty_list() -> None:
    """Return an empty dictionary when there are no expenses."""
    assert totals_by_category([]) == {}


def test_delete_expense_success(
    sample_expenses,
) -> None:
    """Delete a matching expense and return True."""
    result = delete_expense(
        sample_expenses,
        2,
    )

    assert result is True
    assert len(sample_expenses) == 2

    remaining_ids = [
        expense["id"]
        for expense in sample_expenses
    ]

    assert remaining_ids == [1, 3]


def test_delete_expense_not_found(
    sample_expenses,
) -> None:
    """Return False without modifying data for an unknown ID."""
    original_length = len(sample_expenses)

    result = delete_expense(
        sample_expenses,
        99,
    )

    assert result is False
    assert len(sample_expenses) == original_length


def test_read_amount_valid(
    monkeypatch,
) -> None:
    """Return a valid positive amount entered by the user."""
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "450.50",
    )

    result = read_amount()

    assert result == pytest.approx(450.50)


def test_read_amount_retries_after_invalid_input(
    monkeypatch,
) -> None:
    """Keep prompting until a valid positive amount is entered."""
    answers = iter(
        [
            "hello",
            "-20",
            "0",
            "500",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers),
    )

    result = read_amount()

    assert result == pytest.approx(500.0)


def test_read_amount_prints_error_for_invalid_number(
    monkeypatch,
    capsys,
) -> None:
    """Display an error after non-numeric input."""
    answers = iter(
        [
            "abc",
            "100",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers),
    )

    result = read_amount()

    captured = capsys.readouterr()

    assert result == pytest.approx(100.0)
    assert (
        "Please enter a valid number."
        in captured.out
    )


def test_read_amount_rejects_non_positive_value(
    monkeypatch,
    capsys,
) -> None:
    """Reject zero or negative expense amounts."""
    answers = iter(
        [
            "-50",
            "250",
        ]
    )

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(answers),
    )

    result = read_amount()

    captured = capsys.readouterr()

    assert result == pytest.approx(250.0)
    assert (
        "Amount must be greater than zero."
        in captured.out
    )


def test_add_expense() -> None:
    """Create and append an expense from mocked user input."""
    expenses = []

    with patch(
        "builtins.input",
        side_effect=[
            "Lunch",
            "450",
            "Food",
        ],
    ):
        result = add_expense(expenses)

    assert result is True
    assert len(expenses) == 1

    assert expenses[0] == {
        "id": 1,
        "description": "Lunch",
        "amount": 450.0,
        "category": "Food",
    }


def test_add_expense_uses_next_available_id(
    sample_expenses,
) -> None:
    """Assign the next ID when adding another expense."""
    with patch(
        "builtins.input",
        side_effect=[
            "Dinner",
            "700",
            "Food",
        ],
    ):
        add_expense(sample_expenses)

    assert sample_expenses[-1]["id"] == 4
    assert sample_expenses[-1]["description"] == "Dinner"