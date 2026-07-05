"""Advanced Calculator entry point.

Three ways to run:

    python main.py            # interactive command-line REPL
    python main.py --gui      # launch the Tkinter graphical calculator
    python main.py "2 + 2*3"  # evaluate a single expression and exit
"""

from __future__ import annotations

import argparse
import logging
import sys

from config import APP_NAME, VERSION, configure_logging
from models import Calculator, CalculatorError

logger = logging.getLogger(__name__)


def run_repl(calculator: Calculator) -> None:
    """Run an interactive read-eval-print loop."""
    print(f"{APP_NAME} {VERSION}  (type 'quit' to exit, 'history' to review)")
    while True:
        try:
            raw = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return
        if raw.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            return
        if raw.lower() == "history":
            for entry in calculator.history:
                print(f"  {entry.expression} = {entry.result}")
            continue
        if not raw:
            continue
        try:
            print(f"= {calculator.evaluate(raw)}")
        except CalculatorError as error:
            print(f"Error: {error}")


def evaluate_once(calculator: Calculator, expression: str) -> int:
    """Evaluate a single expression, print it, and return an exit code."""
    try:
        print(calculator.evaluate(expression))
        return 0
    except CalculatorError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and dispatch to the requested mode."""
    configure_logging()
    parser = argparse.ArgumentParser(description=f"{APP_NAME} {VERSION}")
    parser.add_argument("expression", nargs="?", help="expression to evaluate")
    parser.add_argument("--gui", action="store_true", help="launch the GUI")
    args = parser.parse_args(argv)

    calculator = Calculator()

    if args.gui:
        from gui import launch  # imported lazily so the REPL needs no Tk

        launch(calculator)
        return 0

    if args.expression:
        return evaluate_once(calculator, args.expression)

    run_repl(calculator)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
