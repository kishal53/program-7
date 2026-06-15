# Multi-Utility Toolkit

A menu-driven Python CLI toolkit that bundles six utility categories into one interactive program — no external dependencies required.

---

## Features

| # | Module | What it does |
|---|--------|-------------|
| 1 | **Datetime & Time** | Current date/time, date difference, date formatting, stopwatch, countdown timer |
| 2 | **Math** | Factorial, compound interest, trigonometry (sin/cos/tan/cosec/sec/cot), area of shapes |
| 3 | **Random Data** | Random number, random list, password generator, OTP generator |
| 4 | **UUID** | Generate a unique UUID v4 identifier |
| 5 | **File Operations** | Create, write, read, and append files (saved to `saved_files/`) |
| 6 | **Module Explorer** | Inspect any Python module's attributes using `dir()` |

---

## Project Structure

```
toolkit/
├── main.py                      # Entry point
└── utilities/
    ├── __init__.py
    ├── datetime_utils.py
    ├── math_utils.py
    ├── random_utils.py
    ├── uuid_utils.py
    └── file_ops/
        ├── __init__.py
        └── file_module.py
```

---

## Requirements

- Python **3.10+** (uses `match`/`case` syntax)
- No third-party packages — standard library only

---

## How to Run

**1. Extract the zip**
```bash
unzip multi_utility_toolkit_v2.zip
cd toolkit
```

**2. Run the program**
```bash
python main.py
```

**3. Navigate the menu**
```
=========================
Welcome to Multi-Utility Toolkit
=========================
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
```
Enter the number for the feature you want, follow the prompts, and press `6`/`5`/`7` (depending on the sub-menu) to go back or exit.

---

## Notes

- Files created via the File Operations module are stored in `toolkit/saved_files/` (auto-created on first use).
- Individual utility modules can also be run standalone for quick testing, e.g. `python utilities/math_utils.py`.
