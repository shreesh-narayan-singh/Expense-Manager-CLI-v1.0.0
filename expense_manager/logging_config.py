"""Logging configuration for the Expense Manager application."""

import logging
from logging.config import dictConfig
from pathlib import Path


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "expense_manager.log"


def configure_logging() -> None:
    """Configure console and file logging for the application.

    Console output includes INFO-level messages and above.
    The log file includes DEBUG-level messages and above.
    """
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": (
                    "%(asctime)s | "
                    "%(levelname)s | "
                    "%(name)s | "
                    "%(message)s"
                ),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "standard",
            },
            "file": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "filename": str(LOG_FILE),
                "encoding": "utf-8",
            },
        },
        "root": {
            "level": "DEBUG",
            "handlers": [
                "console",
                "file",
            ],
        },
    }

    dictConfig(config)