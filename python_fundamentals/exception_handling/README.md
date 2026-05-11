# Python - Exceptions Handling

## Introduction

Real-world programs must be resilient. Inputs may be invalid,
data may be missing, and operations may fail unexpectedly.

Exception handling allows a program to detect errors,
respond appropriately, and continue execution safely when possible.

This project focuses on Python exception handling
and defensive programming techniques.

--------------------------------------------------

## Learning Objectives

At the end of this project, you should be able to explain:

- What exceptions are and why they are useful
- How to use try and except
- How to catch specific exception types
- The purpose of else and finally
- How to raise exceptions manually
- How to write predictable and resilient Python programs

--------------------------------------------------

## Concepts Covered

### 1. try / except

Used to catch runtime errors without stopping the program.

Example:

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

--------------------------------------------------

### 2. Catching Specific Exceptions

Handling only expected exceptions improves readability and safety.

Example:

try:
    number = int("abc")
except ValueError:
    print("Invalid integer")

--------------------------------------------------

### 3. else Block

Executed only if no exception occurs.

Example:

try:
    value = int("42")
except ValueError:
    print("Error")
else:
    print("Conversion successful")

--------------------------------------------------

### 4. finally Block

Always executed whether an exception occurs or not.

Example:

try:
    file = open("test.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")

--------------------------------------------------

### 5. Raising Exceptions

You can manually raise exceptions with raise.

Example:

age = -1

if age < 0:
    raise ValueError("Age cannot be negative")

--------------------------------------------------

## Requirements

- Allowed editors: vi, vim, emacs
- Ubuntu 22.04 LTS
- Python 3.10.*
- All files must end with a new line
- First line of Python files:

#!/usr/bin/python3

- Code must follow pycodestyle
- Files must be executable

--------------------------------------------------

## Project Structure

.
├── 0-safe_print_list.py
├── 1-safe_print_integer.py
├── 2-safe_print_list_integers.py
├── 3-safe_print_division.py
├── 4-list_division.py
├── 5-raise_exception.py
├── 6-raise_exception_msg.py
└── README.md

--------------------------------------------------

## Example

$ ./main.py
12
nb_print: 2

--------------------------------------------------

## Author

Project about Python exception handling
and defensive programming practices.
