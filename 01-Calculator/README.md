# 01 · Calculator

The classic first project, built three ways so you can watch the same idea grow from a beginner script into production-quality software.

| Level | What's new | Interface | Files |
|-------|-----------|-----------|-------|
| [🌱 Beginner](./Beginner) | Functions, input validation, `try/except` | Console, one run | `main.py` |
| [⚙️ Intermediate](./Intermediate) | Menu loop, persistent history | Console, menu | `main.py`, `utils.py` |
| [🚀 Advanced](./Advanced) | Safe expression parser, OOP, GUI, tests | CLI + Tkinter GUI | `main.py`, `models.py`, `gui.py`, `config.py`, `tests.py` |

Each level has a `GUIDE.md` (read on GitHub) and a `guide.html` (open in a browser for the interactive version: progress tracking, quizzes, copy buttons, theme switcher).

## Quick start

```bash
# Beginner
cd Beginner && python main.py

# Intermediate
cd Intermediate && python main.py

# Advanced (CLI, GUI, or one-shot)
cd Advanced
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py            # interactive REPL
python main.py --gui      # Tkinter calculator
python main.py "2 + 3*4"  # evaluate once -> 14.0
pytest tests.py           # run the test suite
```

## The progression at a glance

- **Beginner** does four operations on two numbers and guards divide-by-zero.
- **Intermediate** adds a menu, keeps a history, and saves it to `data/history.json`.
- **Advanced** evaluates *whole expressions* like `2 + 3 * (4 - 1) ** 2` with a safe hand-written parser (no `eval`), wraps it in a class with logging and custom errors, ships a Tkinter GUI, and is covered by a pytest suite.
