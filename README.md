# Expense Manager CLI

A command-line expense management application built with Python.

Expense Manager CLI allows users to record expenses, view expense history, calculate total spending, summarize spending by category, and delete expenses. Expense data is persisted locally using JSON.

This project was built as a practical application of Python fundamentals, Pythonic programming, testing, logging, type hints, modular application design, and dependency management.

## Version

Current release:

**v1.0.0**

## Features

- Add new expenses
- View all recorded expenses
- Calculate total spending
- View spending grouped by category
- Delete expenses by ID
- Persist expense data using JSON
- Validate user input
- Handle missing and invalid data files
- Application logging
- Type hints
- Docstrings
- Modular package structure
- Automated tests using pytest

## Requirements

- Python 3.14 or later
- pytest for running the test suite

The application itself uses only the Python standard library and has no third-party runtime dependencies.

## Project Structure

```text
Expense Manager CLI V1/
│
├── main.py
├── README.md
├── pyproject.toml
├── .gitignore
│
├── data/
│   └── expenses.json
│
├── expense_manager/
│   ├── __init__.py
│   ├── expenses.py
│   ├── logging_config.py
│   ├── models.py
│   ├── reports.py
│   └── storage.py
│
├── tests/
│   ├── conftest.py
│   ├── test_expenses.py
│   ├── test_reports.py
│   └── test_storage.py
│
└── logs/
    └── expense_manager.log
```

Generated files such as logs, caches, the virtual environment, and personal expense data should not be committed to source control.

## Setup

Clone the repository or download the project, then navigate to the project directory.

Create a virtual environment:

```bash
python -m venv .venv
```

### Activate on Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### Activate on Windows Command Prompt

```cmd
.venv\Scripts\activate.bat
```

### Activate on macOS/Linux

```bash
source .venv/bin/activate
```

## Install Development Dependencies

The application itself has no third-party runtime dependencies.

Install pytest to run the automated tests:

```bash
python -m pip install pytest
```

## Run the Application

From the project root:

```bash
python main.py
```

The main menu provides the following options:

```text
==============================
       EXPENSE MANAGER
==============================
1. Add expense
2. View expenses
3. View total
4. View by category
5. Delete expense
6. Exit
```

## Expense Data

Each expense contains:

- ID
- Description
- Amount
- Category

Conceptually, an expense is represented as:

```python
{
    "id": 1,
    "description": "Lunch",
    "amount": 450.0,
    "category": "Food",
}
```

Expense records are persisted locally using JSON.

Personal expense data should not be committed to Git.

## Running Tests

Run the complete test suite from the project root:

```bash
python -m pytest
```

For verbose output:

```bash
python -m pytest -v
```

Run only expense business-logic tests:

```bash
python -m pytest tests/test_expenses.py -v
```

Run reporting tests:

```bash
python -m pytest tests/test_reports.py -v
```

Run storage tests:

```bash
python -m pytest tests/test_storage.py -v
```

Stop after the first failure:

```bash
python -m pytest -x
```

## Testing Approach

The automated test suite covers:

- Expense ID generation
- Expense total calculations
- Category totals
- Expense deletion
- Valid and invalid amount input
- CLI output
- JSON persistence
- Missing data files
- Invalid JSON
- Temporary filesystem isolation

The tests demonstrate several pytest features, including:

- Fixtures
- Parametrization
- `capsys`
- `tmp_path`
- `monkeypatch`
- `unittest.mock.patch`

Temporary files are used during storage tests so automated tests do not modify real expense data.

## Logging

The application uses Python's standard `logging` module.

Logging is configured centrally in:

```text
expense_manager/logging_config.py
```

The application uses different log levels for operational information and debugging.

Console logging displays informational messages and above.

The log file records debug messages and above.

Generated log files are not intended to be committed to source control.

## Architecture

The application separates responsibilities across modules.

### `main.py`

Responsible for:

- Application entry point
- CLI menu
- User interaction
- Application flow

### `expenses.py`

Responsible for:

- Expense business logic
- ID generation
- Adding expenses
- Deleting expenses
- Total calculations
- Category calculations

### `reports.py`

Responsible for:

- Displaying expense records
- Displaying category summaries

### `storage.py`

Responsible for:

- Loading expenses
- Saving expenses
- JSON persistence

### `models.py`

Contains the typed representation of an expense.

### `logging_config.py`

Contains centralized application logging configuration.

## Python Concepts Used

This project applies concepts including:

- Variables and built-in data types
- Lists and dictionaries
- Conditionals and loops
- Functions
- Exceptions
- File handling
- JSON
- `pathlib`
- Modules and packages
- Imports
- Virtual environments
- Type hints
- `TypedDict`
- Docstrings
- PEP 8 conventions
- Logging
- Pytest
- Fixtures
- Parametrization
- Mocking
- Temporary test resources

## Development Principles

The project aims to follow several Python development practices:

- Keep business logic separate from persistence and presentation
- Use explicit imports
- Avoid circular dependencies
- Use type hints at module boundaries
- Document public functionality
- Handle expected exceptions explicitly
- Keep tests independent
- Avoid modifying production data during tests
- Configure logging centrally
- Keep runtime dependencies minimal

## Git Ignore

The repository should exclude generated or machine-specific files such as:

```gitignore
.venv/
__pycache__/
*.pyc
.pytest_cache/
*.log
data/expenses.json
```

## Release History

### v1.0.0

Initial stable release.

Includes:

- Expense creation
- Expense listing
- Expense deletion
- Total spending calculation
- Category spending summaries
- JSON persistence
- Input validation
- Exception handling
- Type hints and docstrings
- Application logging
- Automated pytest test suite
- Modular Python package structure

## Future Improvements

Potential features for future versions include:

- Expense dates
- Expense editing
- Budget limits
- Search and filtering
- CSV import/export
- Monthly reports
- Additional categories
- Database persistence
- Improved CLI presentation

These features are intentionally outside the v1.0.0 scope.

## License

No license has been selected for this project yet.