"""Helper functions for the Intermediate calculator.

This module keeps the plumbing (input validation, calculation, and history
persistence) separate from the menu loop in ``main.py``.
"""

import json
import os
from datetime import datetime

# The history file lives in a ``data/`` folder next to this module.
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")

OPERATORS = {"+", "-", "*", "/"}


def read_number(prompt):
    """Prompt until the user enters a valid number, then return it as a float."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("  Invalid number. Try again (example: 3.14).")


def read_operator(prompt):
    """Prompt until the user enters a supported operator."""
    while True:
        operator = input(prompt).strip()
        if operator in OPERATORS:
            return operator
        print(f"  Unsupported. Choose one of: {' '.join(sorted(OPERATORS))}")


def compute(a, op, b):
    """Apply ``op`` to ``a`` and ``b``.

    Raises:
        ZeroDivisionError: when dividing by zero.
        ValueError: when the operator is not recognised.
    """
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        return a / b
    raise ValueError(f"Unknown operator: {op!r}")


def load_history():
    """Return the saved history as a list, or [] if no file exists yet."""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        # If the file is corrupt or unreadable, start fresh rather than crash.
        return []


def save_entry(expression, result):
    """Append one calculation to the history file, creating it if needed."""
    os.makedirs(DATA_DIR, exist_ok=True)
    history = load_history()
    history.append(
        {
            "expression": expression,
            "result": result,
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }
    )
    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=2)
