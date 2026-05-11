# 🐍 Python Data Structures

## 📚 Overview

This module covers fundamental Python data structures including **lists**, **tuples**, **sets**, and **dictionaries**. Each task demonstrates core operations, safe access patterns, and built-in data type manipulation.

---

## 📂 Files

| File | Description |
|------|-------------|
| `print_list_integer.py` | Print all integers from a list using `{:d}` format |
| `element_at.py` | Safe list access (returns `None` for invalid indices) |
| `replace_in_list.py` | Replace element at index (returns original if invalid) |
| `print_matrix_integer.py` | Print 2D list (matrix) with proper formatting |
| `add_tuple.py` | Add two tuples element-wise (always returns 2-element tuple) |
| `common_elements.py` | Return intersection of two sets |
| `update_dictionary.py` | Add or update key-value pair in dictionary |
| `best_score.py` | Return key with highest integer value |

---

## 🎯 Key Concepts

### Lists (Mutable)
- Dynamic arrays that can be modified
- Indexed access: `list[0]`, `list[-1]`
- Methods: `append()`, `extend()`, `insert()`, `remove()`, `pop()`
- Slicing: `list[1:3]`, `list[::-1]`

### Tuples (Immutable)
- Fixed sequences that cannot be modified
- Used for data integrity and multiple return values
- Single element tuple: `(5,)` (comma required)
- Unpacking: `x, y, z = tuple`

### Sets (Unique, Unordered)
- No duplicate elements
- Fast membership testing
- Operations: `&` (intersection), `|` (union), `-` (difference), `^` (XOR)
- Empty set: `set()` (not `{}`)

### Dictionaries (Key-Value Pairs)
- Mutable mappings
- Fast key lookup
- Methods: `.get()`, `.keys()`, `.values()`, `.items()`
- Direct assignment: `dict[key] = value`

---

## 💡 Important Patterns

### Safe Access
Always validate indices/keys before accessing to prevent crashes:
```python
# Check bounds before list access
if 0 <= idx < len(my_list):
    return my_list[idx]
return None
```

### Format Strings
Use type-specific format specifiers:
- `{:d}` for integers (enforces type checking)
- `{:.2f}` for floats with 2 decimals
- `{}` for generic (accepts any type)

### Default Values
Handle missing data gracefully:
```python
# Tuples: treat missing as 0
a1 = tuple_a[0] if len(tuple_a) > 0 else 0

# Dictionaries: safe access
value = dict.get('key', default_value)
```

---

## 🔧 Common Operations

### Lists
```python
my_list[idx] = value          # Replace element
my_list.append(item)          # Add to end
len(my_list)                  # Get length
item in my_list               # Check membership
```

### Tuples
```python
len(tuple)                    # Get length
tuple[0]                      # Access (read-only)
tuple1 + tuple2               # Concatenate (creates new)
```

### Sets
```python
set1 & set2                   # Intersection
set1 | set2                   # Union
set1 - set2                   # Difference
item in set                   # Fast membership test
```

### Dictionaries
```python
dict[key] = value             # Add/update
dict.get(key)                 # Safe access
key in dict                   # Check key exists
max(dict, key=dict.get)       # Key with max value
```

---

## ✅ Skills Demonstrated

✅ Format strings with type specifiers  
✅ Safe list/dictionary access patterns  
✅ Ternary operators for concise conditionals  
✅ Set operations for mathematical logic  
✅ Dictionary manipulation and queries  
✅ Enumerate for index+value iteration  
✅ Max/min with custom key functions  
✅ Tuple immutability and unpacking  
✅ Difference between mutable/immutable types  

---

## 🎓 Learning Outcomes

After completing this module, you can:
- Choose the appropriate data structure for each use case
- Safely access elements without causing crashes
- Perform set operations for filtering and comparisons
- Manipulate dictionaries efficiently
- Understand mutability implications
- Write defensive, production-ready code

---

## 📖 PEP 8 Compliance

All files follow Python style guidelines:
- 4 spaces for indentation (no tabs)
- Maximum line length: 79 characters
- Two blank lines between top-level definitions
- Descriptive variable names
- Proper shebang: `#!/usr/bin/env python3`

---

## 🚀 Usage Example

```python
# Import and use
from print_list_integer import print_list_integer
from best_score import best_score

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)  # Prints: 1 2 3 4 5

scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
winner = best_score(scores)  # Returns: 'Alice'
```

---

## 🏆 Repository

**GitHub:** `holbertonschool-core-engineering`  
**Directory:** `python_fundamentals/data_structures`

---

*Master Python's core data structures to build robust, efficient applications.*