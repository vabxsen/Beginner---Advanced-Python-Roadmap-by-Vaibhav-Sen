# 🐍 Advanced Python Roadmap

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.x"/>
  <img src="https://img.shields.io/github/license/vabxsen/Advanced-Python-Roadmap-by-vabxsen?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/github/stars/vabxsen/Advanced-Python-Roadmap-by-vabxsen?style=for-the-badge&color=yellow" alt="Stars"/>
  <img src="https://img.shields.io/github/last-commit/vabxsen/Advanced-Python-Roadmap-by-vabxsen?style=for-the-badge" alt="Last commit"/>
</p>

> A structured, code-first Python roadmap — from absolute fundamentals to advanced topics, data science libraries, and mini-projects. Every concept below has a runnable `.py` file to go with it.

---

## 📖 About

This repository is a complete Python learning path, organized into 15 numbered folders that go from the basics straight through to advanced and applied topics. It's built for systematic, hands-on learning rather than just reading — every topic links directly to working code.

Whether you're preparing for interviews, coursework, or just leveling up, the folders are meant to be worked through roughly in order.

**Who it's for:**
- 🌱 Complete beginners with no programming experience
- 🎓 CS/IT students preparing for coursework or exams
- 💼 Interview and placement preparation
- 🚀 Self-learners who want a structured, code-backed roadmap

---

## 📂 Repository Structure

| # | Folder | Topic | Files |
|---|---|---|---|
| 01 | [`01-fundamentals/`](01-fundamentals) | Variables & data types | [`variables_and_data_types.py`](01-fundamentals/variables_and_data_types.py) |
| 02 | [`02-operators/`](02-operators) | Arithmetic, logical, bitwise & more | [`operators.py`](02-operators/operators.py) |
| 03 | [`03-control-flow/`](03-control-flow) | Conditionals & loops | [`if_else.py`](03-control-flow/if_else.py), [`loops.py`](03-control-flow/loops.py) |
| 04 | [`04-functions/`](04-functions) | Functions, lambdas & recursion | [`functions.py`](04-functions/functions.py), [`lambda.py`](04-functions/lambda.py), [`recursion.py`](04-functions/recursion.py) |
| 05 | [`05-collections/`](05-collections) | Strings, lists, tuples, sets, dicts | [`strings.py`](05-collections/strings.py), [`lists.py`](05-collections/lists.py), [`tuples.py`](05-collections/tuples.py), [`sets.py`](05-collections/sets.py), [`dictionaries.py`](05-collections/dictionaries.py) |
| 06 | [`06-file-handling/`](06-file-handling) | Reading/writing files, CSV, JSON | [`file_handling.py`](06-file-handling/file_handling.py), [`csv.py`](06-file-handling/csv.py), [`json.py`](06-file-handling/json.py) |
| 07 | [`07-exception-handling/`](07-exception-handling) | try / except / finally, custom exceptions | [`exception_handling.py`](07-exception-handling/exception_handling.py) |
| 08 | [`08-oop/`](08-oop) | Classes, encapsulation, inheritance, polymorphism, abstraction | [`oop.py`](08-oop/oop.py), [`encapsulation.py`](08-oop/encapsulation.py), [`inheritance.py`](08-oop/inheritance.py), [`polymorphism.py`](08-oop/polymorphism.py), [`abstraction.py`](08-oop/abstraction.py) |
| 09 | [`09-modules-and-packages/`](09-modules-and-packages) | Creating & importing modules and packages | [`modules.py`](09-modules-and-packages/modules.py), [`packages.py`](09-modules-and-packages/packages.py) |
| 10 | [`10-advanced-python/`](10-advanced-python) | Iterators, generators, decorators, concurrency | [`iterators.py`](10-advanced-python/iterators.py), [`generators.py`](10-advanced-python/generators.py), [`decorators.py`](10-advanced-python/decorators.py), [`multithreading.py`](10-advanced-python/multithreading.py), [`multiprocessing.py`](10-advanced-python/multiprocessing.py) |
| 11 | [`11-standard-library-and-utilities/`](11-standard-library-and-utilities) | datetime, regex, argparse, logging, requests | [`datetime.py`](11-standard-library-and-utilities/datetime.py), [`regular_expressions.py`](11-standard-library-and-utilities/regular_expressions.py), [`argparse.py`](11-standard-library-and-utilities/argparse.py), [`logging.py`](11-standard-library-and-utilities/logging.py), [`requests_api.py`](11-standard-library-and-utilities/requests_api.py) |
| 12 | [`12-databases/`](12-databases) | SQLite basics | [`sqlite.py`](12-databases/sqlite.py) |
| 13 | [`13-data-science-libraries/`](13-data-science-libraries) | NumPy, pandas, matplotlib | [`numpy.py`](13-data-science-libraries/numpy.py), [`pandas.py`](13-data-science-libraries/pandas.py), [`matplotlib.py`](13-data-science-libraries/matplotlib.py) |
| 14 | [`14-gui-programming/`](14-gui-programming) | Desktop GUIs with Tkinter | [`tkinter.py`](14-gui-programming/tkinter.py) |
| 15 | [`15-algorithms-and-projects/`](15-algorithms-and-projects) | Search algorithms & a full mini-project | [`b-Search.py`](15-algorithms-and-projects/b-Search.py) (binary search), [`8-Puzzle.py`](15-algorithms-and-projects/8-Puzzle.py) (Pygame-based 8-puzzle solver) |

---

## 🚀 Getting Started

```bash
git clone https://github.com/vabxsen/Advanced-Python-Roadmap-by-vabxsen.git
cd Advanced-Python-Roadmap-by-vabxsen
```

Work through the folders in numeric order (`01-fundamentals` → `15-algorithms-and-projects`), running each file as you go:

```bash
python 01-fundamentals/variables_and_data_types.py
```

Some topics need extra packages — install what a given file imports as you reach it, e.g.:

```bash
pip install numpy pandas matplotlib requests pygame
```

**Prerequisites:** Python 3.x and basic comfort with a terminal — no prior programming experience required otherwise.

---

## 🎓 Learning Outcome

By working through this roadmap you should be able to:
- Write clean, idiomatic Python
- Work confidently with Python's core data structures
- Build object-oriented programs
- Handle files, exceptions, and standard library utilities
- Use iterators, generators, decorators, and concurrency
- Query a database, build a simple GUI, and use NumPy/pandas/matplotlib
- Apply the fundamentals to a real project (the 8-puzzle solver)

---

## 🤝 Contributing

Contributions that improve explanations, fix bugs, or add topics are welcome.

1. Fork the repository
2. Create a branch for your change
3. Commit your changes
4. Open a Pull Request

---

## ⭐ Support

If this helped you, consider starring the repo, sharing it, or contributing improvements.

---

## 📄 License

Distributed under the license in [`LICENSE`](LICENSE).

---

<p align="center">Made with 🐍 by <a href="https://github.com/vabxsen">Vaibhav Sen</a></p>
