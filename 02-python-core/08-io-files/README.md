# 🗂️ File Handling in Python

This folder covers **File I/O operations** — reading, writing, appending, and working with text files in Python. These are essential for logging, data preprocessing, and working with external files in AI/ML workflows.

---

## 🧠 What’s Covered?

| Program Name           | Description                              |
| ---------------------- | ---------------------------------------- |
| `write_to_file.py`     | Write text to a file                     |
| `read_file.py`         | Read file content (whole, line by line)  |
| `append_to_file.py`    | Append new content to a file             |
| `file_with_try.py`     | File operations with exception handling  |
| `file_with_context.py` | Using `with open()` context manager      |
| `file_word_count.py`   | Count lines, words, characters in a file |

---

## 🔧 Key Concepts

### ✅ Basic Operations

* `open(file, mode)` with `'r'`, `'w'`, `'a'`, `'r+'`
* `.read()`, `.readline()`, `.readlines()`
* `.write()` and `.writelines()`

### ✅ Context Manager

```python
with open("file.txt", "r") as file:
    content = file.read()
```

Safely handles file closing.

### ✅ Exception Handling

Use `try-except` blocks around file operations to avoid crashes on missing files or permission errors.

---

## 🧪 How to Run

```bash
python write_to_file.py
```

---

## ✍️ Practice Tips

* Practice reading and processing log files
* Always close files or use `with open()`
* Build small tools like a **file merger**, **notepad clone**, or **line counter**

---

## 🔗 Learn More

* [W3Schools – File Handling](https://www.w3schools.com/python/python_file_handling.asp)
* [Real Python – Working with Files](https://realpython.com/read-write-files-python/)
* [Python Docs – File Objects](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

---

> *“If data is the new oil, then file I/O is your drill.”* ⛏️
