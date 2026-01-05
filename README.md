# 📂 File Organizer

A **Python-based automation tool** that organizes your files into folders based on their type—keeping your workspace neat, tidy, and stress-free.

---

## 🚀 Features

- Automatically scans your current working directory for files.
- Sorts files by type into dedicated folders:
  - PDFs → `pdf_files/`
  - Images → `png_files/`, `jpg_files/`
  - Executables → `Programs/`
  - Text files → `text_files/`
  - Word documents → `word_files/`
- Creates the destination folders automatically if they don't exist.
- Ensures files already in their destination folders are not moved again.
- Fully built using Python’s standard `os` module — no extra installations required.

---

## ⚡ Why Use This?

If your Downloads or project folder looks like this:

report.pdf
image.png
program.exe
notes.txt


After running **File Organizer**, it becomes:

pdf_files/report.pdf
png_files/image.png
Programs/program.exe
text_files/notes.txt


No more digging through messy folders!

---

## 🛠 Installation & Usage

1. Clone or download this repository:

```bash

Place the files you want to organize in the same folder as organizer.py.

Run the script with Python:

python organizer.py
Watch as your files are neatly sorted into their respective folders.

```
📌Requirements
Python 3.x (tested on Python 3.10+)

No external libraries needed.
os is a Built-in Module.

👤 Author

Created by [Muhammad Salman] — making file management easier, one Python script at a time.

###🔗 License

This project is open-source and free to use. Feel free to modify and share!

