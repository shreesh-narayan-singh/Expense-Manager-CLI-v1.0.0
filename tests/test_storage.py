"""Tests for JSON expense persistence."""

import json

from expense_manager import storage


def test_save_and_load_expenses(
    tmp_path,
    monkeypatch,
    sample_expenses,
) -> None:
    """Save expenses and load the same data back."""
    test_file = tmp_path / "expenses.json"

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        test_file,
    )

    storage.save_expenses(sample_expenses)

    loaded_expenses = storage.load_expenses()

    assert loaded_expenses == sample_expenses
    assert test_file.exists()


def test_save_expenses_creates_json_file(
    tmp_path,
    monkeypatch,
    sample_expenses,
) -> None:
    """Create the configured JSON file when saving."""
    test_file = tmp_path / "expenses.json"

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        test_file,
    )

    storage.save_expenses(sample_expenses)

    assert test_file.exists()
    assert test_file.is_file()


def test_saved_file_contains_valid_json(
    tmp_path,
    monkeypatch,
    sample_expenses,
) -> None:
    """Write valid JSON matching the supplied expenses."""
    test_file = tmp_path / "expenses.json"

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        test_file,
    )

    storage.save_expenses(sample_expenses)

    with test_file.open(
        "r",
        encoding="utf-8",
    ) as file:
        saved_data = json.load(file)

    assert saved_data == sample_expenses


def test_load_expenses_missing_file(
    tmp_path,
    monkeypatch,
) -> None:
    """Return an empty list when the data file is missing."""
    missing_file = (
        tmp_path / "does_not_exist.json"
    )

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        missing_file,
    )

    result = storage.load_expenses()

    assert result == []


def test_load_expenses_invalid_json(
    tmp_path,
    monkeypatch,
) -> None:
    """Return an empty list when the JSON file is invalid."""
    test_file = tmp_path / "expenses.json"

    test_file.write_text(
        "{ this is not valid json",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        test_file,
    )

    result = storage.load_expenses()

    assert result == []


def test_load_expenses_empty_json_list(
    tmp_path,
    monkeypatch,
) -> None:
    """Return an empty list when the JSON file contains []."""
    test_file = tmp_path / "expenses.json"

    test_file.write_text(
        "[]",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        test_file,
    )

    result = storage.load_expenses()

    assert result == []


def test_save_expenses_overwrites_existing_data(
    tmp_path,
    monkeypatch,
    sample_expenses,
) -> None:
    """Replace existing JSON data when expenses are saved."""
    test_file = tmp_path / "expenses.json"

    test_file.write_text(
        '[{"old": "data"}]',
        encoding="utf-8",
    )

    monkeypatch.setattr(
        storage,
        "DATA_FILE",
        test_file,
    )

    storage.save_expenses(sample_expenses)

    loaded = storage.load_expenses()

    assert loaded == sample_expenses