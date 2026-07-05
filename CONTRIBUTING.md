# Contributing

Thanks for helping build the curriculum. Everything here follows [`MASTER_IMPLEMENTATION_GUIDE.md`](./MASTER_IMPLEMENTATION_GUIDE.md) — read it first; it is the source of truth.

## Adding or fixing a variant

1. Pick a project and level.
2. Follow the **Development Workflow** (guide section 16): plan, decide files, implement, test, write `GUIDE.md`, build `guide.html`, verify parity, quality review.
3. Respect the **Adaptive File Structure** (section 7): only create files the code actually needs.
4. Match the **Coding Standards** (section 8) for the level and the **Theme System** (section 11) for the HTML.
5. Run the full **Quality Checklist** (section 15) before opening a PR.

## Standards quick reference

- Format with Black (line length 88), lint with Ruff.
- Beginner: stdlib only, no type hints, heavy comments.
- Intermediate: light modules, selective type hints, file persistence.
- Advanced: full type hints (mypy clean), OOP, pytest, pinned `requirements.txt`.
- Never use `eval`/`exec` on user input. Never use a bare `except`.

## Commits

Conventional Commits, scoped by project/level:

```
feat(07-advanced): add Tkinter GUI
docs(07): write intermediate markdown guide
fix(07-beginner): handle empty input
```
