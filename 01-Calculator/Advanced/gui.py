"""Tkinter graphical interface for the Advanced calculator.

The GUI is a thin presentation layer: all arithmetic is delegated to the
``Calculator`` engine in ``models.py``, keeping logic and interface cleanly
separated.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from models import Calculator, CalculatorError

_BUTTONS = [
    ["7", "8", "9", "/", "C"],
    ["4", "5", "6", "*", "("],
    ["1", "2", "3", "-", ")"],
    ["0", ".", "%", "+", "**"],
]


class CalculatorApp(ttk.Frame):
    """The main application frame holding the display and buttons."""

    def __init__(self, master: tk.Tk, calculator: Calculator) -> None:
        super().__init__(master, padding=12)
        self.calculator = calculator
        self.expression = tk.StringVar(value="")
        self.grid(sticky="nsew")
        self._build_display()
        self._build_buttons()

    def _build_display(self) -> None:
        entry = ttk.Entry(
            self,
            textvariable=self.expression,
            justify="right",
            font=("JetBrains Mono", 18),
        )
        entry.grid(row=0, column=0, columnspan=5, sticky="ew", pady=(0, 10), ipady=8)
        entry.focus_set()
        entry.bind("<Return>", lambda _event: self._evaluate())

    def _build_buttons(self) -> None:
        for r, row in enumerate(_BUTTONS, start=1):
            for c, label in enumerate(row):
                ttk.Button(self, text=label, command=self._make_action(label)).grid(
                    row=r, column=c, sticky="nsew", padx=2, pady=2, ipady=8
                )
        ttk.Button(self, text="=", command=self._evaluate).grid(
            row=len(_BUTTONS) + 1,
            column=0,
            columnspan=5,
            sticky="nsew",
            padx=2,
            pady=(6, 0),
            ipady=10,
        )
        for c in range(5):
            self.columnconfigure(c, weight=1)

    def _make_action(self, label: str):
        """Return the callback for a given button label."""
        if label == "C":
            return self._clear
        return lambda: self._append(label)

    def _append(self, text: str) -> None:
        self.expression.set(self.expression.get() + text)

    def _clear(self) -> None:
        self.expression.set("")

    def _evaluate(self) -> None:
        try:
            result = self.calculator.evaluate(self.expression.get())
            self.expression.set(str(result))
        except CalculatorError as error:
            self.expression.set(f"Error: {error}")


def launch(calculator: Calculator | None = None) -> None:
    """Create the root window and start the Tkinter event loop."""
    root = tk.Tk()
    root.title("PyCalc Advanced")
    root.minsize(320, 380)
    CalculatorApp(root, calculator or Calculator())
    root.mainloop()


if __name__ == "__main__":
    launch()
