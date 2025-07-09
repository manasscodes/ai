# 🧯 Exception Handling in Python

This folder focuses on **handling runtime errors in Python** — a must-have skill for writing safe, production-ready code. Whether you're building AI APIs, data pipelines, or CLI tools, you must gracefully catch and manage errors.

---

## 🧠 What’s Covered?

| Program Name           | Description                                 |
| ---------------------- | ------------------------------------------- |
| `basic_try_except.py`  | Basic try-except block                      |
| `multiple_excepts.py`  | Handling multiple exception types           |
| `else_finally_demo.py` | Using `else` and `finally` blocks           |
| `raise_exception.py`   | Manually raising exceptions                 |
| `custom_exception.py`  | Creating and using custom exception classes |

---

## 🔧 Key Concepts

### ✅ Try-Except

Safely catch runtime errors without crashing the program.

```python
try:
    risky_code()
except ZeroDivisionError:
    print("You can’t divide by zero!")
```

### ✅ Multiple Exceptions

Catch different error types separately.

### ✅ Else Block

Executes only if no exception was raised.

### ✅ Finally Block

Always runs, even if an exception occurs (used to close files, DB, etc.)

### ✅ Raise Statement

Used to raise exceptions manually.

### ✅ Custom Exceptions

You can define your own exception class for specific errors.

---

## 🧪 How to Run

```bash
python basic_try_except.py
```

---

## ✍️ Practice Tips

* Wrap input/output, file operations, and conversions in try-except
* Always handle exceptions at the right level — not too broad
* Use `finally` for cleanup logic (closing files, releasing resources)

---

## 🔗 Learn More

* [W3Schools – Python Try Except](https://www.w3schools.com/python/python_try_except.asp)
* [Real Python – Exceptions](https://realpython.com/python-exceptions/)
* [Python Docs – Errors & Exceptions](https://docs.python.org/3/tutorial/errors.html)

---

> *“Well-handled exceptions keep your program running safely and make debugging easier.”* 🚨
