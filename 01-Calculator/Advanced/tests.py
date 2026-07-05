"""Unit tests for the Advanced calculator engine.

Run with:
    pytest tests.py
"""

from __future__ import annotations

import pytest

from models import Calculator, CalculatorError, eval_rpn, to_rpn, tokenize


@pytest.fixture
def calc() -> Calculator:
    return Calculator()


@pytest.mark.parametrize(
    "expression, expected",
    [
        ("2 + 2", 4),
        ("2 + 3 * 4", 14),
        ("(2 + 3) * 4", 20),
        ("10 / 4", 2.5),
        ("2 ** 3 ** 2", 512),  # ** is right associative
        ("-5 + 3", -2),
        ("2 * -4", -8),
        ("10 % 3", 1),
        (".5 + .5", 1.0),
        ("2 + 3 * (4 - 1) ** 2", 29),
    ],
)
def test_evaluate(calc: Calculator, expression: str, expected: float) -> None:
    assert calc.evaluate(expression) == pytest.approx(expected)


def test_division_by_zero(calc: Calculator) -> None:
    with pytest.raises(CalculatorError):
        calc.evaluate("1 / 0")


def test_empty_expression(calc: Calculator) -> None:
    with pytest.raises(CalculatorError):
        calc.evaluate("   ")


def test_unbalanced_parentheses(calc: Calculator) -> None:
    with pytest.raises(CalculatorError):
        calc.evaluate("(2 + 3")


def test_unexpected_character(calc: Calculator) -> None:
    with pytest.raises(CalculatorError):
        calc.evaluate("2 + a")


def test_history_records_entries(calc: Calculator) -> None:
    calc.evaluate("1 + 1")
    calc.evaluate("2 * 2")
    assert len(calc.history) == 2
    assert calc.history[0].result == 2


def test_clear_history(calc: Calculator) -> None:
    calc.evaluate("1 + 1")
    calc.clear_history()
    assert calc.history == []


def test_pipeline_directly() -> None:
    assert eval_rpn(to_rpn(tokenize("3 + 4 * 2"))) == 11
