# Python - Abstract Classes & Interfaces

================================================================================
                          PYTHON OOP - ADVANCED CONCEPTS
================================================================================

AUTHOR      : Training / Learning Module
LEVEL       : Beginner → Intermediate
TOPIC       : Abstract Classes & Interfaces
LANGUAGE    : Python 3.x
================================================================================


## 1. OBJECTIVE
--------------------------------------------------------------------------------
Learn how to structure Python programs using:

- Abstract Classes
- Abstract Methods
- Interface-like design
- Code contracts between classes


## 2. WHY USING ABSTRACT CLASSES ?
--------------------------------------------------------------------------------

In real applications, you often want to define a common structure.

Example:
- Animal → Dog, Cat, Bird
- Shape  → Circle, Square, Triangle
- Payment → CreditCard, PayPal, Bitcoin

You want to FORCE child classes to implement specific methods.


## 3. MODULE USED
--------------------------------------------------------------------------------

Python provides the `abc` module:

```python
from abc import ABC, abstractmethod
