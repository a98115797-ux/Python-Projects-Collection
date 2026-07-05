"""Configuration constants and logging setup for the Advanced calculator."""

from __future__ import annotations

import logging
from pathlib import Path

APP_NAME: str = "PyCalc Advanced"
VERSION: str = "1.0.0"

# Number of significant digits shown in results.
DISPLAY_PRECISION: int = 10

# Where persistent data would be stored (reserved for future features).
BASE_DIR: Path = Path(__file__).resolve().parent
DATA_DIR: Path = BASE_DIR / "data"
HISTORY_FILE: Path = DATA_DIR / "history.json"

# Logging configuration.
LOG_LEVEL: int = logging.INFO
LOG_FORMAT: str = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def configure_logging() -> None:
    """Configure root logging once, using the module-level format and level."""
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
