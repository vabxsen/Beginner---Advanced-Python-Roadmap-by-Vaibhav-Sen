"""
=========================================================
Topic : Multithreading in Python
=========================================================

This program demonstrates:
1. Creating Threads
2. Starting Threads
3. Joining Threads
4. Thread Names
5. Daemon Threads
6. Thread Synchronization
7. Lock Objects
8. Practical Examples

Module Used:
threading
time
"""

import threading
import time

print("=" * 60)
print("MULTITHREADING IN PYTHON")
print("=" * 60)

# =======================================================
# SIMPLE THREAD
# =======================================================

def display_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(0.5)

print("\n1. Simple Thread")

thread1 = threading.Thread(target=display_numbers)

thread1.start()
thread1.join()

# =======================================================
# MULTIPLE THREADS
# =======================================================

def print_letters():
    for letter in ["A", "B", "C", "D", "E"]:
        print("Letter:", letter)
        time.sleep(0.4)

print("\n2. Multiple Threads")

thread2 = threading.Thread(target=display_numbers)
thread3 = threading.Thread(target=print_letters)

thread2.start()
thread3.start()

thread2.join()
thread3.join()

# =======================================================
# THREAD NAMES
# =======================================================

print("\n3. Thread Names")

def thread_info():
    print("Current Thread:", threading.current_thread().name)

thread4 = threading.Thread(target=thread_info, name="Worker-1")
thread4.start()
thread4.join()

# =======================================================
# DAEMON THREAD
# =======================================================

print("\n4. Daemon Thread")

def background_task():
    while True:
        print("Background Task Running...")
        time.sleep(1)

daemon = threading.Thread(target=background_task)
daemon.daemon = True
daemon.start()

time.sleep(3)

print("Main Program Continues")

# =======================================================
# THREAD LOCK
# =======================================================

lock = threading.Lock()

counter = 0

def increase_counter():

    global counter

    for _ in range(100000):

        lock.acquire()

        counter += 1

        lock.release()

print("\n5. Thread Synchronization")

t1 = threading.Thread(target=increase_counter)
t2 = threading.Thread(target=increase_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print("Counter:", counter)

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

def download(file):

    print(f"Downloading {file}...")
    time.sleep(2)
    print(f"{file} Download Complete!")

print("\n6. File Downloads")

files = [
    "Python.pdf",
    "Video.mp4",
    "Image.png"
]

threads = []

for file in files:

    thread = threading.Thread(
        target=download,
        args=(file,)
    )

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

def worker(worker_id):

    for i in range(3):
        print(f"Worker {worker_id}: Task {i+1}")
        time.sleep(0.5)

print("\n7. Workers")

workers = []

for i in range(1, 4):

    thread = threading.Thread(
        target=worker,
        args=(i,)
    )

    workers.append(thread)
    thread.start()

for thread in workers:
    thread.join()

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n8. Active Thread Count")

print("Active Threads:",
      threading.active_count())

print("Main Thread:",
      threading.main_thread().name)

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. Thread -> Smallest unit of execution.")
print("2. threading.Thread() creates a thread.")
print("3. start() begins thread execution.")
print("4. join() waits for a thread to finish.")
print("5. Daemon threads run in the background.")
print("6. Lock prevents race conditions.")
print("7. active_count() returns active threads.")
print("8. current_thread() returns current thread.")
print("9. Multithreading improves responsiveness.")
print("10. Best for I/O-bound tasks.")

print("\nEnd of Program")