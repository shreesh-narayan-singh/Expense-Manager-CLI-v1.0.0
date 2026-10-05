"""Tests for expense reporting functions."""

from expense_manager.reports import (
    view_by_category,
    view_expenses,
)


def test_view_expenses_empty(
    capsys,
) -> None:
    """Display a message when there are no expenses."""
    view_expenses([])

    captured = capsys.readouterr()

    assert "No expenses found." in captured.out


def test_view_expenses_displays_expenses(
    sample_expenses,
    capsys,
) -> None:
    """Display expense records in the terminal report."""
    view_expenses(sample_expenses)

    captured = capsys.readouterr()

    assert "ID" in captured.out
    assert "Description" in captured.out
    assert "Category" in captured.out
    assert "Amount" in captured.out

    assert "Lunch" in captured.out
    assert "Taxi" in captured.out
    assert "Coffee" in captured.out

    assert "Food" in captured.out
    assert "Travel" in captured.out


def test_view_expenses_displays_ids(
    sample_expenses,
    capsys,
) -> None:
    """Display expense IDs in the report."""
    view_expenses(sample_expenses)

    captured = capsys.readouterr()

    assert "1" in captured.out
    assert "2" in captured.out
    assert "3" in captured.out


def test_view_expenses_displays_formatted_amounts(
    sample_expenses,
    capsys,
) -> None:
    """Display expense amounts with two decimal places."""
    view_expenses(sample_expenses)

    captured = capsys.readouterr()

    assert "450.00" in captured.out
    assert "300.00" in captured.out
    assert "150.00" in captured.out


def test_view_by_category_empty(
    capsys,
) -> None:
    """Display a message when no category totals exist."""
    view_by_category([])

    captured = capsys.readouterr()

    assert "No expenses found." in captured.out


def test_view_by_category(
    sample_expenses,
    capsys,
) -> None:
    """Display total spending grouped by category."""
    view_by_category(sample_expenses)

    captured = capsys.readouterr()

    assert "Spending by category:" in captured.out
    assert "Food" in captured.out
    assert "Travel" in captured.out

    assert "600.00" in captured.out
    assert "300.00" in captured.out