"""Beginner Calculator.

Asks the user for two numbers and one operator (+, -, *, /),
then prints the result. Uses only Python's built-in features:
no external libraries required.

Run it with:
    python main.py
"""


def get_number(prompt):
    """Ask the user for a number, repeating until they type a valid one.

    We use a ``while True`` loop so that if the user types something that is
    not a number (like "hello"), we simply ask again instead of crashing.
    """
    while True:
        # ``input()`` always returns text (a string), so we try to turn it
        # into a floating-point number with ``float()``.
        raw_value = input(prompt)
        try:
            return float(raw_value)
        except ValueError:
            # ``float("hello")`` raises a ValueError. We catch it, explain the
            # problem in a friendly way, and then let the loop ask again.
            print("  That doesn't look like a number. Please try again.")


def get_operator():
    """Ask the user for one of the four supported operators."""
    valid_operators = ("+", "-", "*", "/")
    while True:
        operator = input("Choose an operator (+, -, *, /): ").strip()
        if operator in valid_operators:
            return operator
        print("  Please type one of: + - * /")


def calculate(first_number, operator, second_number):
    """Return the result of applying ``operator`` to the two numbers.

    Division by zero is undefined, so we guard against it and return a
    friendly message instead of letting Python raise an error.
    """
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            return "Error: you cannot divide by zero."
        return first_number / second_number
    # We should never reach this line because the operator is validated
    # earlier, but being explicit is good practice.
    return "Error: unknown operator."


def main():
    """Run the calculator once, from start to finish."""
    print("=" * 40)
    print("        Welcome to the Calculator")
    print("=" * 40)

    first_number = get_number("Enter the first number:  ")
    operator = get_operator()
    second_number = get_number("Enter the second number: ")

    result = calculate(first_number, operator, second_number)

    print("-" * 40)
    print(f"Result: {first_number} {operator} {second_number} = {result}")
    print("-" * 40)


# This means: only run main() if this file is started directly,
# not if it is imported by another file.
if __name__ == "__main__":
    main()
