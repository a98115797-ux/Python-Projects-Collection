"""Core calculation engine for the Advanced calculator.

This module implements a *safe* arithmetic expression evaluator. It never
uses ``eval()``; instead it tokenizes the input, converts it to Reverse
Polish Notation (RPN) with the shunting-yard algorithm, then evaluates the
RPN. This makes it safe to run on untrusted input.

Supported syntax:
    - numbers (integer and floating point, e.g. 3, 3.14, .5)
    - binary operators: + - * / % **
    - unary minus (e.g. -3, 2 * -4)
    - parentheses for grouping
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)


class CalculatorError(Exception):
    """Raised when an expression cannot be parsed or evaluated."""


# --- Tokenizer ---------------------------------------------------------


@dataclass(frozen=True)
class Token:
    """A single lexical token: a number, operator, or parenthesis."""

    kind: str  # "NUMBER", "OP", "LPAREN", "RPAREN"
    value: str


def tokenize(expression: str) -> list[Token]:
    """Convert a raw expression string into a list of tokens.

    Raises:
        CalculatorError: if an unexpected character is encountered.
    """
    tokens: list[Token] = []
    i = 0
    n = len(expression)

    while i < n:
        char = expression[i]

        if char.isspace():
            i += 1
            continue

        if char.isdigit() or char == ".":
            start = i
            seen_dot = char == "."
            i += 1
            while i < n and (expression[i].isdigit() or expression[i] == "."):
                if expression[i] == ".":
                    if seen_dot:
                        raise CalculatorError(
                            f"Malformed number near position {start}."
                        )
                    seen_dot = True
                i += 1
            tokens.append(Token("NUMBER", expression[start:i]))
            continue

        if char == "*" and i + 1 < n and expression[i + 1] == "*":
            tokens.append(Token("OP", "**"))
            i += 2
            continue

        if char in "+-*/%":
            tokens.append(Token("OP", char))
            i += 1
            continue

        if char == "(":
            tokens.append(Token("LPAREN", char))
            i += 1
            continue

        if char == ")":
            tokens.append(Token("RPAREN", char))
            i += 1
            continue

        raise CalculatorError(f"Unexpected character {char!r} at position {i}.")

    return tokens


# --- Parsing (shunting-yard) -------------------------------------------

# operator -> (precedence, is_right_associative)
_PRECEDENCE: dict[str, tuple[int, bool]] = {
    "u-": (4, True),  # unary minus
    "**": (3, True),
    "*": (2, False),
    "/": (2, False),
    "%": (2, False),
    "+": (1, False),
    "-": (1, False),
}


def to_rpn(tokens: list[Token]) -> list[Token]:
    """Convert an infix token list to Reverse Polish Notation.

    Handles operator precedence, associativity, parentheses, and unary minus.
    """
    output: list[Token] = []
    stack: list[Token] = []
    previous: Token | None = None

    for token in tokens:
        if token.kind == "NUMBER":
            output.append(token)
        elif token.kind == "OP":
            op = token.value
            # A '-' at the start, or right after an operator or '(', is unary.
            if op == "-" and (
                previous is None
                or previous.kind == "OP"
                or previous.kind == "LPAREN"
            ):
                op = "u-"
            prec, right_assoc = _PRECEDENCE[op]
            while stack and stack[-1].kind == "OP":
                top_prec, _ = _PRECEDENCE[stack[-1].value]
                if top_prec > prec or (top_prec == prec and not right_assoc):
                    output.append(stack.pop())
                else:
                    break
            stack.append(Token("OP", op))
        elif token.kind == "LPAREN":
            stack.append(token)
        elif token.kind == "RPAREN":
            while stack and stack[-1].kind != "LPAREN":
                output.append(stack.pop())
            if not stack:
                raise CalculatorError("Unbalanced parentheses: missing '('.")
            stack.pop()  # discard the matching '('
        previous = token

    while stack:
        top = stack.pop()
        if top.kind in {"LPAREN", "RPAREN"}:
            raise CalculatorError("Unbalanced parentheses: missing ')'.")
        output.append(top)

    return output


# --- Evaluation --------------------------------------------------------


def _apply(op: str, right: float, left: float | None = None) -> float:
    """Apply a single operator. ``left`` is None for unary operators."""
    if op == "u-":
        return -right
    if left is None:
        raise CalculatorError(f"Operator {op!r} is missing an operand.")
    if op == "+":
        return left + right
    if op == "-":
        return left - right
    if op == "*":
        return left * right
    if op == "/":
        if right == 0:
            raise CalculatorError("Division by zero.")
        return left / right
    if op == "%":
        if right == 0:
            raise CalculatorError("Modulo by zero.")
        return left % right
    if op == "**":
        return left ** right
    raise CalculatorError(f"Unknown operator: {op!r}")


def eval_rpn(rpn: list[Token]) -> float:
    """Evaluate a Reverse Polish Notation token list and return the result."""
    stack: list[float] = []
    for token in rpn:
        if token.kind == "NUMBER":
            stack.append(float(token.value))
            continue
        op = token.value
        if op == "u-":
            if not stack:
                raise CalculatorError("Unary minus has no operand.")
            stack.append(_apply(op, stack.pop()))
        else:
            if len(stack) < 2:
                raise CalculatorError(f"Operator {op!r} needs two operands.")
            right = stack.pop()
            left = stack.pop()
            stack.append(_apply(op, right, left))
    if len(stack) != 1:
        raise CalculatorError("Invalid expression.")
    return stack[0]


# --- Public API --------------------------------------------------------


@dataclass
class HistoryEntry:
    """One evaluated expression and its result."""

    expression: str
    result: float
    timestamp: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )


class Calculator:
    """A safe arithmetic calculator with an in-memory history."""

    def __init__(self) -> None:
        self._history: list[HistoryEntry] = []

    @property
    def history(self) -> list[HistoryEntry]:
        """Return a copy of the calculation history."""
        return list(self._history)

    def evaluate(self, expression: str) -> float:
        """Safely evaluate an arithmetic expression string.

        Raises:
            CalculatorError: if the expression is empty or invalid.
        """
        if not expression or not expression.strip():
            raise CalculatorError("Expression is empty.")
        logger.debug("Evaluating expression: %s", expression)
        tokens = tokenize(expression)
        rpn = to_rpn(tokens)
        result = eval_rpn(rpn)
        self._history.append(HistoryEntry(expression.strip(), result))
        return result

    def clear_history(self) -> None:
        """Remove all entries from the history."""
        self._history.clear()
