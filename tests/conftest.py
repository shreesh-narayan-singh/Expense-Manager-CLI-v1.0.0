"""Shared pytest fixtures for the Expense Manager test suite."""

import pytest

from expense_manager.models import Expense


@pytest.fixture
def sample_expenses() -> list[Expense]:
    """Return a fresh list of sample expenses for each test."""
    return [
        {
            "id": 1,
            "description": "Lunch",
            "amount": 450.0,
            "category": "Food",
        },
        {
            "id": 2,
            "description": "Taxi",
            "amount": 300.0,
            "category": "Travel",
        },
        {
            "id": 3,
            "description": "Coffee",
            "amount": 150.0,
            "category": "Food",
        },
    ]