"""
=========================================================
Topic : Logging in Python
=========================================================

This program demonstrates:
1. Basic Logging
2. Logging Levels
3. Log Formatting
4. Logging to a File
5. Exception Logging
6. Custom Logger
7. Multiple Handlers
8. Practical Examples
"""

import logging

print("=" * 60)
print("LOGGING IN PYTHON")
print("=" * 60)

# =======================================================
# BASIC LOGGING CONFIGURATION
# =======================================================

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="application.log",
    filemode="w"
)

print("\n1. Basic Logging")

logging.debug("Debug Message")
logging.info("Information Message")
logging.warning("Warning Message")
logging.error("Error Message")
logging.critical("Critical Message")

print("Messages written to application.log")

# =======================================================
# LOGGING LEVELS
# =======================================================

print("\n2. Logging Levels")

logging.debug("Debugging Program")
logging.info("Program Started")
logging.warning("Low Memory Warning")
logging.error("File Not Found")
logging.critical("Application Crashed")

# =======================================================
# EXCEPTION LOGGING
# =======================================================

print("\n3. Exception Logging")

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.exception("Division by Zero Error")

# =======================================================
# CUSTOM LOGGER
# =======================================================

print("\n4. Custom Logger")

logger = logging.getLogger("StudentLogger")

logger.setLevel(logging.INFO)

logger.info("Student Record Created")
logger.warning("Attendance is Low")

# =======================================================
# CONSOLE HANDLER
# =======================================================

print("\n5. Console Handler")

console = logging.StreamHandler()

formatter = logging.Formatter(
    "%(levelname)s -> %(message)s"
)

console.setFormatter(formatter)

logger.addHandler(console)

logger.info("Console Logging Enabled")

# =======================================================
# PRACTICAL EXAMPLE 1
# =======================================================

print("\n6. Login System")

username = "admin"
password = "12345"

if username == "admin" and password == "12345":
    logging.info("User Logged In Successfully")
else:
    logging.error("Invalid Login Attempt")

# =======================================================
# PRACTICAL EXAMPLE 2
# =======================================================

print("\n7. Bank Transaction")

balance = 5000
withdraw = 6000

if withdraw <= balance:
    balance -= withdraw
    logging.info("Withdrawal Successful")
else:
    logging.warning("Insufficient Balance")

# =======================================================
# PRACTICAL EXAMPLE 3
# =======================================================

print("\n8. File Processing")

filename = "students.txt"

try:
    with open(filename, "r") as file:
        logging.info(f"{filename} Opened Successfully")

except FileNotFoundError:
    logging.error(f"{filename} Not Found")

# =======================================================
# PRACTICAL EXAMPLE 4
# =======================================================

print("\n9. Student Marks")

marks = 95

logging.info(f"Student Marks : {marks}")

if marks >= 90:
    logging.info("Excellent Performance")

# =======================================================
# PRACTICAL EXAMPLE 5
# =======================================================

print("\n10. Loop Logging")

for i in range(1, 6):
    logging.debug(f"Current Value : {i}")

# =======================================================
# SUMMARY
# =======================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("1. logging.debug() -> Debug messages")
print("2. logging.info() -> General information")
print("3. logging.warning() -> Warning messages")
print("4. logging.error() -> Error messages")
print("5. logging.critical() -> Critical errors")
print("6. logging.exception() -> Log exceptions")
print("7. basicConfig() configures logging")
print("8. Log files help in debugging applications")
print("9. Logging is preferred over print()")
print("10. Logging is essential in real-world applications")

print("\nEnd of Program")