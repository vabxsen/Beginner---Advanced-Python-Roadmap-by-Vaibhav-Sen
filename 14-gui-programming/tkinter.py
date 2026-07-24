"""
=========================================================
Topic : Tkinter GUI Programming in Python
=========================================================

This program demonstrates:
1. Creating a Window
2. Labels
3. Buttons
4. Entry Widgets
5. Frames
6. Checkbuttons
7. Radiobuttons
8. Combobox
9. Message Boxes
10. Practical Examples

Install:
Tkinter comes pre-installed with Python.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# =======================================================
# MAIN WINDOW
# =======================================================

root = tk.Tk()

root.title("Tkinter Demo")
root.geometry("500x550")
root.resizable(False, False)

# =======================================================
# LABEL
# =======================================================

title = tk.Label(
    root,
    text="Python Tkinter Demo",
    font=("Arial", 18, "bold")
)

title.pack(pady=10)

# =======================================================
# ENTRY
# =======================================================

tk.Label(root, text="Enter Your Name").pack()

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# =======================================================
# BUTTON FUNCTION
# =======================================================

def greet():

    name = name_entry.get()

    if name == "":
        messagebox.showwarning(
            "Warning",
            "Please enter your name!"
        )

    else:
        messagebox.showinfo(
            "Welcome",
            f"Hello {name}!"
        )

# =======================================================
# BUTTON
# =======================================================

button = tk.Button(
    root,
    text="Submit",
    command=greet
)

button.pack(pady=10)

# =======================================================
# CHECKBUTTON
# =======================================================

python_var = tk.BooleanVar()

check = tk.Checkbutton(
    root,
    text="I Know Python",
    variable=python_var
)

check.pack()

# =======================================================
# RADIO BUTTONS
# =======================================================

gender = tk.StringVar(value="Male")

tk.Label(root, text="Select Gender").pack()

tk.Radiobutton(
    root,
    text="Male",
    variable=gender,
    value="Male"
).pack()

tk.Radiobutton(
    root,
    text="Female",
    variable=gender,
    value="Female"
).pack()

# =======================================================
# COMBOBOX
# =======================================================

tk.Label(root, text="Choose Course").pack()

courses = ttk.Combobox(
    root,
    values=[
        "Python",
        "Java",
        "AI",
        "Machine Learning"
    ]
)

courses.current(0)

courses.pack(pady=5)

# =======================================================
# FRAME
# =======================================================

frame = tk.Frame(root, bd=2, relief="solid")

frame.pack(pady=15)

tk.Label(
    frame,
    text="This is inside a Frame"
).pack(padx=20, pady=10)

# =======================================================
# LISTBOX
# =======================================================

tk.Label(root, text="Programming Languages").pack()

listbox = tk.Listbox(root, height=5)

languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Go"
]

for language in languages:
    listbox.insert(tk.END, language)

listbox.pack()

# =======================================================
# PRACTICAL EXAMPLE
# =======================================================

def show_information():

    message = f"""
Name      : {name_entry.get()}
Python    : {python_var.get()}
Gender    : {gender.get()}
Course    : {courses.get()}
"""

    messagebox.showinfo(
        "Student Information",
        message
    )

tk.Button(
    root,
    text="Show Information",
    command=show_information
).pack(pady=20)

# =======================================================
# STATUS LABEL
# =======================================================

status = tk.Label(
    root,
    text="Ready",
    relief="sunken",
    anchor="w"
)

status.pack(side="bottom", fill="x")

# =======================================================
# START APPLICATION
# =======================================================

root.mainloop()