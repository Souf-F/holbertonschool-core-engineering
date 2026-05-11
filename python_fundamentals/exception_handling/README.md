# 🐍 Python Exception Handling

## 📚 Core Concepts

### try / except
**Purpose:** Execute risky code and catch errors without crashing.

**Key Points:**
- Separates normal code from error handling
- Always catch **specific exceptions** (never bare `except:`)
- Makes code resilient and predictable

---

### finally
**Purpose:** Code that **ALWAYS executes**, regardless of success or failure.

**Use Cases:**
- Close files
- Release resources
- Clean up connections
- Log operations

**Guaranteed Execution:**
- ✅ If try succeeds
- ✅ If exception occurs
- ✅ Even with return/break/continue

---

### raise
**Purpose:** Manually trigger exceptions.

**Common Uses:**
- Validate parameters
- Enforce business rules
- Signal impossible operations
- Propagate errors upward

---

## 🎯 Common Exception Types

| Exception | When It Occurs |
|-----------|----------------|
| `ValueError` | Invalid value |
| `TypeError` | Wrong type |
| `IndexError` | Index out of range |
| `KeyError` | Missing dictionary key |
| `ZeroDivisionError` | Division by zero |
| `NameError` | Undefined variable |

---

## ✅ Best Practices

### DO:
- ✅ Catch **specific exceptions**
- ✅ Use `finally` for cleanup
- ✅ Provide clear error messages
- ✅ Fail fast with validation

### DON'T:
- ❌ Use bare `except:`
- ❌ Silently ignore errors with `pass`
- ❌ Use exceptions for normal flow control

---

## 🔄 Execution Order

**No Error:**
try → else (if present) → finally

**Error Caught:**
try → except → finally

**Error Not Caught:**
try → finally → crash

---

## 💡 Key Takeaway

**Exception handling transforms fragile code into robust, production-ready software by gracefully managing errors instead of crashing.**

---

## 🏆 Skills Learned

✅ Identify common exceptions  
✅ Use try/except/finally correctly  
✅ Catch specific exception types  
✅ Raise exceptions with clear messages  
✅ Write defensive, fail-safe code  
✅ Clean up resources reliably
