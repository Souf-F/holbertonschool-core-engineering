# 🔄 Control Flow in Python

Master the fundamental concepts that control program execution flow.

---

## 📚 Table of Contents

- [Loops](#loops)
- [Conditions](#conditions)
- [Operators](#operators)
- [String Formatting](#string-formatting)
- [Print Function](#print-function)
- [Utility Functions](#utility-functions)

---

## 🔁 Loops

### `for` Loop
Repeats actions for each item in a collection or sequence.

### `range()`
Generates sequences of numbers for iteration.
- `range(stop)` - 0 to stop-1
- `range(start, stop)` - start to stop-1
- `range(start, stop, step)` - with custom increment

**Key Rule:** Stop value is always excluded.

### Nested Loops
Loop inside another loop for handling multi-dimensional iterations or generating combinations.

---

## 🤔 Conditions

### `if` / `elif` / `else`
Makes decisions in code based on conditions being True or False.

**Key Behavior:** Python stops at the first True condition.

---

## ⚖️ Operators

### Comparison Operators
- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal
- `<=` Less than or equal

### Logical Operators
- `and` - Both conditions must be True
- `or` - At least one condition must be True
- `not` - Inverts the boolean value

### Membership Operators
- `in` - Checks if element exists in collection
- `not in` - Checks if element doesn't exist in collection

---

## 🎨 String Formatting

### f-strings
Modern way to embed variables and expressions in strings using `f"text {variable}"`.

### `.format()`
Classic method using placeholders `"text {}".format(variable)`.

### Format Specifiers
- `{:02d}` - Zero-padded integers (e.g., 05)
- `{:.2f}` - Float with decimal precision (e.g., 3.14)
- `{:d}` - Decimal integer

---

## 🖨️ Print Function

### `end` Parameter
Controls what's printed at the end instead of default newline (`\n`).

### `sep` Parameter
Controls separator between multiple values (default is space).

---

## 🔧 Utility Functions

### `chr()`
Converts ASCII code to character.

### `ord()`
Converts character to ASCII code.

### `hex()`
Converts decimal number to hexadecimal string.

### `continue`
Skips to next iteration in a loop.

### `break`
Exits loop completely.

### `join()`
Combines list of strings into single string with separator.

---

## 📊 Key Concepts

| Concept | Purpose |
|---------|---------|
| **Loops** | Repeat actions |
| **Conditions** | Make decisions |
| **Operators** | Compare and combine values |
| **Formatting** | Display data professionally |
| **Print Control** | Manage output appearance |
| **Utilities** | Convert and manipulate data |

---

## ⚠️ Common Mistakes

1. **Off-by-one errors** - Forgetting `range()` excludes stop value
2. **`=` vs `==`** - Assignment vs comparison
3. **Missing colons** - Required after `if`, `for`, `def`
4. **Indentation** - Python uses it for code blocks
5. **Modulo with negatives** - Use `% -10` for negative numbers

---

**Built with** 🐍 Python 3.8 | **Style** PEP8 | **Environment** Ubuntu 20.04 LTS