# Python - Abstract Classes & Interfaces

## 📋 Overview

Exploration of abstract base classes, interfaces, duck typing, multiple inheritance, and mixins in Python through practical implementations.

---

## 🎯 Learning Objectives

- Use ABC and @abstractmethod to create abstract classes
- Implement subclasses satisfying abstract contracts
- Apply duck typing for flexible polymorphism
- Work with multiple inheritance and understand MRO
- Use mixins for composable behaviors
- Extend built-in classes with custom functionality

---

## 📚 Core Concepts

### Abstract Base Class (ABC)
Class defining methods that must be implemented by subclasses. Cannot be instantiated.

### @abstractmethod
Decorator forcing subclasses to implement a method.

### Duck Typing
Using objects based on their behavior (methods available), not their type.

### Multiple Inheritance
Class inheriting from multiple parent classes: `class Child(Parent1, Parent2):`

### Mixin
Small class providing single reusable capability. Name ends with `Mixin`.

### Method Resolution Order (MRO)
Order Python searches for methods in multiple inheritance.

### super()
Calls method from parent class while preserving functionality.

---

## 📖 Tasks

### Task 0: Abstract Animal Class
**File:** `animals.py`

Create abstract `Animal` class with abstract `sound()` method. Implement `Dog` (returns "Bark") and `Cat` (returns "Meow").

**Key Points:**
- Animal cannot be instantiated (TypeError)
- Dog and Cat must implement sound()
- Demonstrates abstract contract enforcement

---

### Task 1: Shapes and Duck Typing
**File:** `shapes.py`

Create abstract `Shape` with `area()` and `perimeter()`. Implement `Circle` and `Rectangle`. Write `shape_info()` function using duck typing (no isinstance checks).

**Key Points:**
- Circle: area = πr², perimeter = 2πr
- Rectangle: area = w×h, perimeter = 2(w+h)
- shape_info() works with any object having area() and perimeter()

---

### Task 2: FlyingFish - Multiple Inheritance
**File:** `flyingfish.py`

Create `Fish` (swim, habitat) and `Bird` (fly, habitat). Implement `FlyingFish` inheriting from both, overriding all methods.

**Key Points:**
- Multiple inheritance: `class FlyingFish(Fish, Bird):`
- MRO: FlyingFish → Fish → Bird → object
- Override resolves habitat() conflict

---

### Task 3: Dragon - Mixins
**File:** `dragon.py`

Create `SwimMixin` (swim method) and `FlyMixin` (fly method). Implement `Dragon` combining both mixins with its own `roar()` method.

**Key Points:**
- Mixins provide single focused capability
- Dragon combines multiple behaviors
- Modular and reusable design

---

### Task 4: VerboseList - Extending Built-ins
**File:** `verboselist.py`

Extend Python's `list` class to print notifications when items are added or removed.

**Override Methods:**
- `append(item)` - "Added [item] to the list."
- `extend(iterable)` - "Extended the list with [n] items."
- `remove(item)` - "Removed [item] from the list."
- `pop(index=-1)` - "Popped [item] from the list."

**Key Points:**
- Use super() to preserve original functionality
- Add custom behavior while keeping all list features

---

## 📁 Project Structure
python_oop/abc/
├── animals.py          # Abstract Animal, Dog, Cat
├── shapes.py           # Shape, Circle, Rectangle, shape_info()
├── flyingfish.py       # Fish, Bird, FlyingFish
├── dragon.py           # SwimMixin, FlyMixin, Dragon
└── verboselist.py      # VerboseList extending list

---

## 🔑 Key Definitions

**Abstract Class:** Cannot be instantiated, defines interface for subclasses  
**Concrete Class:** Implements all abstract methods, can be instantiated  
**Duck Typing:** "If it quacks like a duck, it's a duck" - behavior over type  
**MRO:** Method Resolution Order - search path in inheritance hierarchy  
**Mixin:** Provides single capability, designed to be combined with other classes  
**Override:** Redefine parent method in child class  
**super():** Access parent class methods

---

## 📋 Requirements

- Python 3.8 on Ubuntu 20.04
- Executable files with `#!/usr/bin/env python3`
- PEP8 compliant
- Docstrings for all modules, classes, functions
- Standard library only

---

## ✅ Quick Checklist

- ✅ Use `from abc import ABC, abstractmethod`
- ✅ Abstract classes inherit from ABC
- ✅ Abstract methods use @abstractmethod decorator
- ✅ Concrete classes implement all abstract methods
- ✅ Duck typing functions avoid isinstance checks
- ✅ Multiple inheritance: mind the order `(Parent1, Parent2)`
- ✅ Mixins: single responsibility, reusable
- ✅ Extending built-ins: always use super()

---

**Institution:** Holberton School
