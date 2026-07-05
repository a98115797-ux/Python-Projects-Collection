"""Intermediate Calculator.

A menu-driven console calculator with input validation and a persistent
calculation history saved to ``data/history.json``.

The program logic lives here; reusable helpers (validation, computation,
and persistence) live in ``utils.py``. Splitting responsibilities like this
is a first step toward maintainable code.

Run it with:
    python main.py
"""

from utils import (
    compute,
    load_history,
    read_number,
    read_operator,
    save_entry,
)

MENU = """
==============================
         CALCULATOR
==============================
  1) New calculation
  2) View history
  3) Clear the screen
  4) Quit
------------------------------"""


def do_calculation():
    """Run one calculation, print it, and save it to the history file."""
    a = read_number("First number:  ")
    op = read_operator("Operator (+ - * /): ")
    b = read_number("Second number: ")

    try:
        result = compute(a, op, b)
    except ZeroDivisionError as error:
        print(f"  {error}")
        return

    expression = f"{a} {op} {b}"
    print(f"  = {result}")
    save_entry(expression, result)


def show_history():
    """Print every saved calculation, oldest first."""
    history = load_history()
    if not history:
        print("  No calculations yet.")
        return
    print("  --- History ---")
    for index, entry in enumerate(history, start=1):
        print(
            f"  {index:>3}. {entry['expression']} = {entry['result']}"
            f"   ({entry['timestamp']})"
        )


def main():
    """Show the menu in a loop until the user chooses to quit."""
    while True:
        print(MENU)
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            do_calculation()
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("\n" * 3)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("  Please choose a number from 1 to 4.")


if __name__ == "__main__":
    main()
