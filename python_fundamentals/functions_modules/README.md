# 🐍 Functions & Modularity - Quick Guide

Essential concepts for Python functions and modules.

---

## 📚 What You Learned

### 1. Functions

**Create reusable code blocks**

```python
def add(a, b):
    return a + b
```

- `def` = define function
- `return` = send value back
- Parameters = inputs (a, b)

---

### 2. Return vs Print

```python
# return - gives value back (reusable)
def get_result(x):
    return x * 2

value = get_result(5)  # value = 10

# print - just displays (not reusable)
def show_result(x):
    print(x * 2)

value = show_result(5)  # value = None
```

**Rule:** Use `return` in functions, `print` for output.

---

### 3. Imports

**Use code from other files**

```python
# file1.py
def greet(name):
    return f"Hello {name}"

# file2.py
from file1 import greet
print(greet("Alice"))
```

**Import styles:**
- `from module import function` ✅ Best
- `from module import *` ❌ Avoid

---

### 4. if __name__ == "__main__"

**Prevent code from running when imported**

```python
def my_function():
    return 42

if __name__ == "__main__":
    # Only runs when file executed directly
    print(my_function())
```

| Action | __name__ value | Code runs? |
|--------|---------------|------------|
| `python3 file.py` | `"__main__"` | ✅ Yes |
| `import file` | `"file"` | ❌ No |

---

## 🔧 Useful Functions

### ord() and chr()

**Convert between characters and ASCII codes**

```python
ord('a')  # 97 (character → number)
chr(65)   # 'A' (number → character)

# Lowercase to uppercase
char = 'h'
upper = chr(ord(char) - 32)  # 'H'
```

**ASCII ranges:**
- `a-z` = 97-122 (lowercase)
- `A-Z` = 65-90 (uppercase)

---

### abs()

**Get absolute value (remove negative sign)**

```python
abs(-10)   # 10
abs(5)     # 5
abs(-3.14) # 3.14
```

---

### Modulo (%)

**Get remainder of division**

```python
10 % 3 = 1  # 10 ÷ 3 = 3 remainder 1

# Extract last digit
1234 % 10 = 4
abs(-567) % 10 = 7
```

---

## 📝 Common Patterns

### Basic Function
```python
def multiply(a, b):
    return a * b
```

### Function with Loop
```python
def power(a, b):
    result = 1
    for i in range(b):
        result *= a
    return result
```

### Importing Functions
```python
from calculator import add, sub

a = 10
b = 5
print(add(a, b))  # 15
```

### Importing Variables
```python
# config.py
MAX_VALUE = 100

# main.py
from config import MAX_VALUE
print(MAX_VALUE)  # 100
```

---

## ✅ Key Rules

1. **Functions** = Reusable code with `def`
2. **Return** = Send value back (use in functions)
3. **Print** = Display only (use for output)
4. **Import** = Use code from other files
5. **`if __name__ == "__main__"`** = Protect code from running during import

---

## 🎯 Quick Reference

```python
# Define function
def function_name(param):
    return value

# Import function
from module import function_name

# Import variable
from module import variable_name

# Execution guard
if __name__ == "__main__":
    code_here()

# ASCII conversion
ord('a')  # char → number
chr(65)   # number → char

# Get last digit
abs(number) % 10

# Power without **
result = 1
for i in range(exponent):
    result *= base
```

---

**Built with** 🐍 Python 3.8