# Diagonal Length Calculator

**Project:** Rectangle Diagonal Calculator  
**Branch:** `main`  
**Developer:** Berke Kurnaz (@berke-kurnaz)

## 🎯 Purpose
This repository contains a lightweight, modular Python command-line application designed to calculate the diagonal length of a rectangle using the Pythagorean theorem. It focuses on core mathematical functions, user input validation, and structural documentation.

## 📁 Artefact Index

| File | What it records |
|---|---|
| `README.md` | Project overview, setup instructions, and execution guide |
| `main.py` | Core calculation script with error handling and CLI prompts |
| `BACKLOG.md` | Product backlog, Epic definitions, and task tracking |

## 📊 Project at a Glance
- **Core Functionality:** Utilizes `math.sqrt()` to compute the hypotenuse accurately (a² + b² = c²).
- **User Experience:** Provides a clear, interactive terminal interface for inputting width and height.
- **Error Handling:** Implements robust `try-except` blocks to catch and gracefully handle `ValueError` exceptions (e.g., string inputs or negative values).
- **Target Quality:** Code is structured for modularity, making the `calculate_diagonal()` function easy to export into larger engineering or architectural tools.

## ✅ Verification and Working Agreements
1. Check that `BACKLOG.md` items are updated (checked off) as tasks are completed.
2. Ensure Python 3.x is installed on the host environment.
3. Verify functionality by running: `python main.py` in the terminal.
4. Input test cases: test positive floats (e.g., entering 3 and 4 should output 5.00), and test string inputs to ensure the program catches errors without a traceback crash.
5. Review and merge all future feature additions through a Pull Request into the `main` branch.