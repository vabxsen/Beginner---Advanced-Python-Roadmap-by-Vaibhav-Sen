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

## 📘 Topics Explained

Each entry below has a short explanation and a real snippet pulled from that folder's file — click to expand. See the linked `.py` file for the full, runnable version with more examples.

<details>
<summary><b>01 · Fundamentals</b> — variables & data types</summary>

Python variables don't need a declared type — the type is inferred from the assigned value and can change at runtime (dynamic typing). This section covers naming conventions, multiple assignment, the built-in types (`int`, `float`, `complex`, `str`, `bool`), converting between them, and inspecting identity/type with `id()` and `isinstance()`.

```python
value = 100
print(type(value))          # <class 'int'>

value = "Now I'm a string"
print(type(value))          # <class 'str'>

number_string = "150"
converted_integer = int(number_string)
converted_float = float(number_string)
```

📄 [`01-fundamentals/variables_and_data_types.py`](01-fundamentals/variables_and_data_types.py)
</details>

<details>
<summary><b>02 · Operators</b> — arithmetic, comparison, logical, bitwise</summary>

Covers arithmetic, assignment, comparison, logical, identity, membership, and bitwise operators, plus how operator precedence decides evaluation order.

```python
a, b = 15, 4
print("Addition       :", a + b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Exponentiation :", a ** b)
```

📄 [`02-operators/operators.py`](02-operators/operators.py)
</details>

<details>
<summary><b>03 · Control Flow</b> — conditionals & loops</summary>

`if` / `elif` / `else` branches control which code runs based on a condition; `for` and `while` loops repeat code, with `break`, `continue`, and `pass` controlling flow inside them.

```python
age = 20
if age >= 18:
    print("You are eligible to vote.")

for i in range(1, 6):
    print("Iteration:", i)
```

📄 [`03-control-flow/if_else.py`](03-control-flow/if_else.py), [`03-control-flow/loops.py`](03-control-flow/loops.py)
</details>

<details>
<summary><b>04 · Functions</b> — definitions, arguments, lambdas, recursion</summary>

Functions bundle reusable logic behind a name. This section covers positional/default/keyword arguments, `*args`/`**kwargs`, return values, variable scope, recursive functions, and one-line anonymous `lambda` functions.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

square = lambda x: x * x
print(square(5))            # 25
```

📄 [`04-functions/functions.py`](04-functions/functions.py), [`04-functions/lambda.py`](04-functions/lambda.py), [`04-functions/recursion.py`](04-functions/recursion.py)
</details>

<details>
<summary><b>05 · Collections</b> — strings, lists, tuples, sets, dictionaries</summary>

Python's core built-in data structures: mutable ordered `list`s, immutable ordered `tuple`s, unordered unique-value `set`s, key-value `dict`s, and `str` text sequences — including indexing, slicing, built-in methods, and comprehensions.

```python
squares = [x ** 2 for x in range(1, 11)]
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
```

📄 [`05-collections/lists.py`](05-collections/lists.py), [`05-collections/dictionaries.py`](05-collections/dictionaries.py), [`05-collections/sets.py`](05-collections/sets.py), [`05-collections/tuples.py`](05-collections/tuples.py), [`05-collections/strings.py`](05-collections/strings.py)
</details>

<details>
<summary><b>06 · File Handling</b> — text files, CSV, JSON</summary>

The `with` statement safely opens and automatically closes files. This section covers reading/writing plain text with file modes, plus structured formats: CSV (via the `csv` module) and JSON (via the `json` module).

```python
with open("student.txt", "w") as file:
    file.write("Name : Alice\n")

with open("student.txt", "r") as file:
    content = file.read()
```

📄 [`06-file-handling/file_handling.py`](06-file-handling/file_handling.py), [`06-file-handling/csv.py`](06-file-handling/csv.py), [`06-file-handling/json.py`](06-file-handling/json.py)
</details>

<details>
<summary><b>07 · Exception Handling</b> — try / except / finally</summary>

`try`/`except` catches errors so they don't crash the program; `else` runs when no exception occurred, `finally` always runs for cleanup. Also covers catching specific exception types, raising exceptions, and defining custom exception classes.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
```

📄 [`07-exception-handling/exception_handling.py`](07-exception-handling/exception_handling.py)
</details>

<details>
<summary><b>08 · OOP</b> — classes, encapsulation, inheritance, polymorphism, abstraction</summary>

Classes bundle data (attributes) and behavior (methods) into objects. This section covers constructors, encapsulation (public/protected/private members, `@property`), inheritance via `super()`, polymorphism (method overriding, duck typing), and abstraction with `ABC`/`abstractmethod`.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")
```

📄 [`08-oop/oop.py`](08-oop/oop.py), [`08-oop/inheritance.py`](08-oop/inheritance.py), [`08-oop/encapsulation.py`](08-oop/encapsulation.py), [`08-oop/polymorphism.py`](08-oop/polymorphism.py), [`08-oop/abstraction.py`](08-oop/abstraction.py)
</details>

<details>
<summary><b>09 · Modules & Packages</b> — organizing and reusing code</summary>

Modules are just `.py` files you can import; packages are folders of modules with an `__init__.py`. Covers importing built-ins, aliasing, importing specific names, and writing your own modules.

```python
import math
print("Square Root of 64 :", math.sqrt(64))

from math import factorial, ceil
```

📄 [`09-modules-and-packages/modules.py`](09-modules-and-packages/modules.py), [`09-modules-and-packages/packages.py`](09-modules-and-packages/packages.py)
</details>

<details>
<summary><b>10 · Advanced Python</b> — iterators, generators, decorators, concurrency</summary>

Iterators implement `__iter__`/`__next__` to produce values one at a time; generators do the same lazily using `yield`. Decorators wrap a function to extend its behavior without changing its code. `threading`/`multiprocessing` cover running work concurrently.

```python
def decorator(function):
    def wrapper():
        print("Before Function Execution")
        function()
    return wrapper

def numbers():
    yield 1
    yield 2
    yield 3
```

📄 [`10-advanced-python/decorators.py`](10-advanced-python/decorators.py), [`10-advanced-python/generators.py`](10-advanced-python/generators.py), [`10-advanced-python/iterators.py`](10-advanced-python/iterators.py), [`10-advanced-python/multithreading.py`](10-advanced-python/multithreading.py), [`10-advanced-python/multiprocessing.py`](10-advanced-python/multiprocessing.py)
</details>

<details>
<summary><b>11 · Standard Library & Utilities</b> — datetime, regex, argparse, logging, requests</summary>

A tour of commonly used standard-library (and near-standard) modules: `datetime` for dates/times, `re` for pattern matching, `argparse` for CLI arguments, `logging` for structured logs, and `requests` for HTTP calls.

```python
import re
match = re.search(r"\d+", "Order number 4587")
print(match.group())        # "4587"
```

📄 [`11-standard-library-and-utilities/datetime.py`](11-standard-library-and-utilities/datetime.py), [`11-standard-library-and-utilities/regular_expressions.py`](11-standard-library-and-utilities/regular_expressions.py), [`11-standard-library-and-utilities/argparse.py`](11-standard-library-and-utilities/argparse.py), [`11-standard-library-and-utilities/logging.py`](11-standard-library-and-utilities/logging.py), [`11-standard-library-and-utilities/requests_api.py`](11-standard-library-and-utilities/requests_api.py)
</details>

<details>
<summary><b>12 · Databases</b> — SQLite with sqlite3</summary>

Python's built-in `sqlite3` module talks to a local SQLite database file with no separate server. Covers connecting, creating tables, and CRUD operations using parameterized queries (to avoid SQL injection).

```python
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
```

📄 [`12-databases/sqlite.py`](12-databases/sqlite.py)
</details>

<details>
<summary><b>13 · Data Science Libraries</b> — NumPy, pandas, matplotlib</summary>

NumPy provides fast, vectorized arrays for numerical work; pandas builds on top of it with `Series`/`DataFrame` for tabular data; matplotlib turns either into charts.

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr.mean(), arr.sum())
```

📄 [`13-data-science-libraries/numpy.py`](13-data-science-libraries/numpy.py), [`13-data-science-libraries/pandas.py`](13-data-science-libraries/pandas.py), [`13-data-science-libraries/matplotlib.py`](13-data-science-libraries/matplotlib.py)
</details>

<details>
<summary><b>14 · GUI Programming</b> — desktop apps with Tkinter</summary>

Tkinter (Python's built-in GUI toolkit) builds desktop windows out of widgets — labels, buttons, entry fields, frames, and dialogs — arranged with a layout manager.

```python
import tkinter as tk

root = tk.Tk()
root.title("Tkinter Demo")
tk.Label(root, text="Hello, Tkinter!").pack()
root.mainloop()
```

📄 [`14-gui-programming/tkinter.py`](14-gui-programming/tkinter.py)
</details>

<details>
<summary><b>15 · Algorithms & Projects</b> — binary search & an 8-puzzle solver</summary>

Applies the fundamentals to real problems: a classic binary search implementation, and a full Pygame-based 8-puzzle solver that combines search algorithms (via `heapq`), threading, and a graphical interface into one project.

```python
def binary_search(arr, key):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
```

📄 [`15-algorithms-and-projects/b-Search.py`](15-algorithms-and-projects/b-Search.py), [`15-algorithms-and-projects/8-Puzzle.py`](15-algorithms-and-projects/8-Puzzle.py)
</details>

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
