soon# Python - File Handling

## Description
This project teaches the basics of file manipulation in Python: reading, writing, and appending content to UTF-8 text files.

## Skills Learned
- Using the `with` statement to manage files
- File opening modes: `r` (read), `w` (write), `a` (append)
- Methods: `read()`, `write()`, `readline()`, `readlines()`
- UTF-8 encoding management
- Automatic system resource release

## Files

| File | Description |
|------|-------------|
| `read_file.py` | Reads a UTF-8 file and prints it |
| `write_file.py` | Writes text to a file (overwrites content) |
| `append_write.py` | Appends text to the end of a file |

## Usage

```python
# Read a file
read_file("example.txt")

# Write to a file
nb_chars = write_file("output.txt", "Hello World\n")

# Append to a file
nb_chars = append_write("output.txt", "New line\n")
```

## Author
Project completed as part of the Holberton School curriculum