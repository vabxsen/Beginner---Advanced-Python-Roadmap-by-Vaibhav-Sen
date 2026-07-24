"""
=========================================================
Topic : Multiprocessing in Python
=========================================================

This program demonstrates:
1. Creating Processes
2. Starting Processes
3. Joining Processes
4. Process ID (PID)
5. Current Process
6. Sharing Data
7. Process Communication
8. Process Pool
9. Practical Examples

Modules Used:
multiprocessing
os
time
"""

from multiprocessing import Process, Pool, Value, current_process
import os
import time

print("=" * 60)
print("MULTIPROCESSING IN PYTHON")
print("=" * 60)

# =======================================================
# SIMPLE PROCESS
# =======================================================

def print_numbers():
    for i in range(1, 6):
        print(f"Process Number: {i}")
        time.sleep(0.5)

print("\n1. Creating a Process")

process1 = Process(target=print_numbers)

process1.start()
process1.join()

# =======================================================
# MULTIPLE PROCESSES
# =======================================================

def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print("Letter:", letter)
        time.sleep(0.5)

print("\n2. Multiple Processes")

p1 = Process(target=print_numbers)
p2 = Process(target=print_letters)

p1.start()
p2.start()

p1.join()
p2.join()

# =======================================================
# PROCESS INFORMATION
# =======================================================

def process_info():
    print("Current Process:", current_process().name)
    print("Process ID (PID):", os.getpid())

print("\n3. Process Information")

p3 = Process(target=process_info, name="Worker-Process")

p3.start()
p3.join()

# =======================================================
# SHARING DATA USING VALUE
# =======================================================

counter = Value('i', 0)

def increase(shared_value):

    for _ in range(1000):
        with shared_value.get_lock():
            shared_value.value += 1

print("\n4. Shared Value")

p4 = Process(target=increase, args=(counter,))
p5 = Process(target=increase, args=(counter,))

p4.start()
p5.start()

p4.join()
p5.join()

print("Counter Value:", counter.value)

# =======================================================
# PROCESS POOL
# =======================================================

def square(number):
    return number ** 2

print("\n5. Process Pool")

numbers = [1, 2, 3, 4, 5]

with Pool(processes=2) as pool:
    result = pool.map(square, numbers)

print("Squares:", result)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

def calculate_cube(number):
    print(f"Cube of {number} = {number ** 3}")

print("\n6. Cube Calculation")

processes = []

for i in range(1, 6):

    process = Process(
        target=calculate_cube,
        args=(i,)
    )

    processes.append(process)
    process.start()

for process in processes:
    process.join()

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

def download(file_name):
    print(f"Downloading {file_name}...")
    time.sleep(2)
    print(f"{file_name} Download Complete!")

print("\n7. File Download Simulation")

files = [
    "Python.pdf",
    "Video.mp4",
    "Image.png"
]

download_processes = []

for file in files:

    process = Process(
        target=download,
        args=(file,)
    )

    download_processes.append(process)
    process.start()

for process in download_processes:
    process.join()

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

def worker(task):
    print(f"Process {os.getpid()} completed {task}")

print("\n8. Worker Processes")

tasks = [
    "Task-1",
    "Task-2",
    "Task-3"
]

workers = []

for task in tasks:

    process = Process(
        target=worker,
        args=(task,)
    )

    workers.append(process)
    process.start()

for process in workers:
    process.join()

# =======================================================
# MAIN PROCESS INFORMATION
# =======================================================

print("\n9. Main Process")

print("Main Process Name :", current_process().name)
print("Main Process PID  :", os.getpid())

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Process -> Independent execution unit.")
print("2. Process() creates a new process.")
print("3. start() starts a process.")
print("4. join() waits for completion.")
print("5. Pool executes tasks efficiently.")
print("6. Value shares data between processes.")
print("7. Each process has its own memory.")
print("8. Multiprocessing is best for CPU-bound tasks.")
print("9. os.getpid() returns the Process ID.")
print("10. multiprocessing uses multiple CPU cores.")

print("\nEnd of Program")