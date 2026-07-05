# MASTER IMPLEMENTATION GUIDE
### Python-Projects-Collection — A Professional, Open-Source Python Curriculum

> **Version:** 1.0.0 · **Status:** Source of Truth · **Scope:** 50 projects x 3 variants = 150 implementations.
> If code and this guide disagree, this guide wins until formally revised.

## Table of Contents
1. Project Vision & Goals
2. Target Audience
3. Learning Philosophy
4. Complete List of All 50 Projects
5. Feature Roadmap per Variant
6. Recommended Folder Hierarchy
7. Adaptive File Structure
8. Coding Standards
9. Documentation Standards
10. HTML Design Standards
11. Theme System
12. Naming Conventions
13. Dependency Rules
14. Testing Strategy
15. Quality Checklist
16. Development Workflow
17. Project Milestones
18. Final Deliverables

---

## 1. Project Vision & Goals

**Vision.** One repository that carries a learner from `print("Hello")` to production-grade, tested, deployable software, using the same 50 real-world projects rebuilt at three escalating levels of mastery.

**Why three variants?** The fastest way to feel your growth is to build the same thing again, better. Beginner sees the idea, Intermediate sees the architecture, Advanced sees the engineering.

**Goals:** (G1) always runnable on clean Python 3.11+; (G2) self-teaching via Markdown + interactive HTML; (G3) visible progression across levels; (G4) professional craft (PEP 8, docstrings, tests, type hints); (G5) portfolio-ready.

**Non-Goals:** not a stdlib reference, not framework-exhaustive, not a video course.

## 2. Target Audience

| Persona | Starting point | Entry level |
|---|---|---|
| Absolute Beginner | Never coded / freezes on a blank file | Beginner |
| Self-Taught Plateauer | Writes scripts, can't structure a project | Intermediate |
| Job-Seeker / Bootcamp Grad | Comfortable, weak on production practices | Advanced |
| Educator | Teaches Python | All three |

**Prerequisites:** Beginner needs Python installed + an editor. Intermediate needs functions/lists/dicts/loops. Advanced needs classes, venvs, pip, CLI.

## 3. Learning Philosophy
1. Build first, theorize second.
2. Escalate, don't restart. Each level assumes the one below.
3. Read before you write (Predict the Output, Code Walkthrough).
4. Errors are curriculum (Common Errors in every guide).
5. One idea per project bump.
6. Docs and code are one artifact. Divergence is a bug.

## 4. Complete List of All 50 Projects

| # | Project | Domain | # | Project | Domain |
|---|---------|--------|---|---------|--------|
| 01 | Calculator | Fundamentals | 26 | Batch File Renamer | Automation |
| 02 | To-Do List | Fundamentals | 27 | Web Scraper | Data |
| 03 | Number Guessing Game | Games | 28 | Weather App | Data |
| 04 | Rock Paper Scissors | Games | 29 | News Aggregator | Data |
| 05 | Dice Roller | Games | 30 | URL Shortener | Web |
| 06 | Password Generator | Security | 31 | QR Code Generator | Tools |
| 07 | Unit Converter | Utilities | 32 | Barcode Scanner | Tools |
| 08 | Temperature Converter | Utilities | 33 | Image Editor | Media |
| 09 | Tip Calculator | Finance | 34 | PDF Tools | Documents |
| 10 | BMI Calculator | Health | 35 | Email Automation | Automation |
| 11 | Countdown Timer | Utilities | 36 | Chat Application | Networking |
| 12 | Stopwatch | Utilities | 37 | Blog Platform | Web |
| 13 | Alarm Clock | Utilities | 38 | E-commerce Store | Web |
| 14 | Currency Converter | Finance | 39 | Task Scheduler | Automation |
| 15 | Hangman | Games | 40 | Habit Tracker | Productivity |
| 16 | Tic-Tac-Toe | Games | 41 | Pomodoro Timer | Productivity |
| 17 | Quiz App | Education | 42 | Music Player | Media |
| 18 | Flashcards | Education | 43 | Video Downloader | Media |
| 19 | Contact Book | Productivity | 44 | Snake Game | Games |
| 20 | Expense Tracker | Finance | 45 | Chess Game | Games |
| 21 | Budget Manager | Finance | 46 | Data Visualizer | Data Science |
| 22 | Notes App | Productivity | 47 | Stock Tracker | Finance |
| 23 | Markdown Editor | Tools | 48 | Cryptocurrency Dashboard | Finance |
| 24 | Text Editor | Tools | 49 | REST API Service | Backend |
| 25 | File Organizer | Automation | 50 | Machine Learning | Data Science |

## 5. Feature Roadmap per Variant

**Universal escalation contract:**

| Dimension | Beginner | Intermediate | Advanced |
|---|---|---|---|
| Interface | Console, linear | Console, menu-driven | GUI / Web / rich CLI |
| Architecture | Single file, procedural | 2-4 files, helper modules | Full package, OOP, layers |
| State | In-memory | File persistence (JSON/CSV) | Database / structured storage |
| Errors | Basic try/except | Validated input | Custom exceptions, logging |
| Types | None | Selective | Full type hints, mypy-clean |
| Tests | Manual | A few cases | pytest suite |
| Deps | stdlib only | <= 1-2 justified | as needed, pinned |
| Lines | 50-150 | 150-400 | 400-1000+ |

**Worked example (01-Calculator):** Beginner = `main.py` two-number calc; Intermediate = `main.py` + `utils.py`, menu + JSON history; Advanced = safe expression parser, OOP, Tkinter GUI, pytest, requirements.txt. Each project instantiates this contract for its own domain.

## 6. Recommended Folder Hierarchy

```
Python-Projects-Collection/
  README.md
  MASTER_IMPLEMENTATION_GUIDE.md
  LICENSE  CONTRIBUTING.md  .gitignore
  assets/themes/{beginner,intermediate,advanced}.css
  01-Calculator/
    README.md
    Beginner/     { main.py, GUIDE.md, guide.html }
    Intermediate/ { main.py, utils.py, data/, GUIDE.md, guide.html }
    Advanced/     { main.py, gui.py, models.py, config.py, tests.py, requirements.txt, GUIDE.md, guide.html }
  ...
  50-Machine-Learning/
```
Folder prefixes are zero-padded and permanent. Project folders are `NN-Kebab-Case`.

## 7. Adaptive File Structure
Create a file only when the code needs it. `main.py` always; `utils.py` when >=2 reusable helpers; `gui.py` for a GUI; `models.py` for domain entities; `api.py` for HTTP; `config.py` for >=3 settings; `database.py` for SQLite/ORM; `scheduler.py` for recurring execution; `tests.py` for Intermediate/Advanced; `requirements.txt` when any external dep is used; `assets/` and `data/` as needed. Reject unused module files and single-constant config files.

## 8. Coding Standards
PEP 8 (Black line length 88, Ruff). Runnable on 3.11+. `snake_case`/`PascalCase`/`UPPER_SNAKE`, meaningful names. Module docstrings everywhere; function docstrings where behavior isn't obvious. Never bare `except`, never `eval`/`exec` on user input. Beginner = procedural, heavy comments. Intermediate = grouped functions, selective type hints. Advanced = OOP, full type hints (mypy clean), custom exceptions, `logging`, clean separation of concerns.

## 9. Documentation Standards
Every variant ships `GUIDE.md` and `guide.html` with identical educational content, in this order: (1) Project Overview (2) Learning Objectives (3) Prerequisites (4) Setup (5) Key Concepts (6) Glossary (7) Predict the Output (8) Complete Source Code (9) Code Walkthrough (10) Execution (11) Expected Output (12) Common Errors (13) Real-World Applications (14) Deep Dive (15) Practice Challenges (16) Knowledge Check (17) Next Project. Markdown is GitHub-flavored with Mermaid fences. HTML adds interactivity only, never extra or missing content.

## 10. HTML Design Standards
Each `guide.html` is a single self-contained offline file: responsive, Mermaid diagrams, syntax highlighting, copy-code buttons, theme switcher, progress tracking (localStorage), interactive quizzes, sticky scroll-spy nav, mobile support. Vendor libraries inline for true offline use; no runtime network requests; content is real HTML that degrades gracefully with JS disabled. Semantic HTML5, aria labels, WCAG AA contrast.

## 11. Theme System
**Beginner (Friendly):** soft pastels, large radius, rounded friendly type (Nunito). **Intermediate (Dashboard):** glassmorphism, medium radius, Inter. **Advanced (IDE):** GitHub Dark palette, tight radius, JetBrains Mono. Shared contract: CSS custom properties (`--bg`, `--surface`, `--text`, `--muted`, `--accent`, `--radius`, `--font-body`, `--font-mono`, `--code-bg`); light/dark via a `data-mode` attribute.

## 12. Naming Conventions
Project folders `NN-Kebab-Case` (permanent). Variant folders exactly `Beginner`/`Intermediate`/`Advanced`. Python files `snake_case.py`. Docs `GUIDE.md`, `guide.html`. Branches `project/NN-<slug>-<level>`. Conventional Commits (`feat(07-advanced): add GUI`).

## 13. Dependency Rules
Beginner: stdlib only, no requirements.txt. Intermediate: <= 1-2 justified deps. Advanced: as needed, pinned `==` versions, venv instructions. Approved libs: requests, pytest, rich, Pillow, pandas, matplotlib, fastapi+uvicorn, pygame, pypdf, scikit-learn, qrcode, beautifulsoup4. Permissive licenses only. No dead deps.

## 14. Testing Strategy
Beginner: manual run + Expected Output match. Intermediate: a handful of unit tests in `tests.py`. Advanced: real pytest suite, mypy clean. Tests are deterministic (seed random, mock network). Predict/Expected Output sections must match real behavior.

## 15. Quality Checklist
**Code:** runs on clean 3.11+; PEP 8; meaningful names; error handling + validation; docstrings; type hints per level; no eval/bare except; line count in band; adaptive structure. **Docs:** both guides, all 17 sections, identical content, code matches source, Mermaid renders, correct theme, offline, widgets functional, mobile verified. **Tests:** present and passing. **Meta:** project README links variant, Next Project link correct, Conventional Commit.

## 16. Development Workflow
Per variant: (1) plan (2) decide files (3) implement (4) test (5) write GUIDE.md (6) build guide.html (7) verify parity (8) quality review (9) next variant (10) repeat. Complete a project fully before starting the next; ship in waves of ~5 projects.

## 17. Project Milestones
M0 Blueprint (this guide + scaffold). M1 Foundations 01-10. M2 Utilities & Games 11-20. M3 Tools & Automation 21-30. M4 Media & Networking 31-40. M5 Advanced & Data 41-50. M6 Polish & Release (master index, v1.0 tag). Each M1-M5 = 30 implementations passing the checklist.

## 18. Final Deliverables
50 project folders; 150 implementations; adaptive structures; production-quality Python; complete educational docs; interactive HTML guides; master README; this guide; repo hygiene (LICENSE, CONTRIBUTING, .gitignore, shared themes). **Complete** = every checklist box passes for all 150 variants and the repo runs green from a fresh clone.
