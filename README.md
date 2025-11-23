# 📐 Arithmetic Formatter

[![Build Status](https://github.com/TheComputationalCore/Arithmetic-Formatter/actions/workflows/tests.yml/badge.svg)](https://github.com/TheComputationalCore/Arithmetic-Formatter/actions/workflows/tests.yml)
[![Docs](https://img.shields.io/badge/Documentation-Online-brightgreen)](https://thecomputationalcore.github.io/Arithmetic-Formatter/)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

A clean, modern, and well‑structured Python package that formats arithmetic problems vertically and side‑by‑side.  
Includes a CLI tool, full test suite, modern documentation (MkDocs), and a clean project layout.

---

## 🌐 Documentation

📖 Full documentation is available here:  
👉 **https://thecomputationalcore.github.io/Arithmetic-Formatter/**

---

## 📸 Screenshots

> Make sure that your repository contains these images inside the `screenshots/` directory.

### **Project Structure**
![Project Structure](screenshots/project_structure.png)

### **Documentation (MkDocs)**
![Documentation Screenshot](screenshots/docs_screenshot.png)

### **CLI Output Example**
![CLI Output](screenshots/cli_output.png)

---

## 🚀 Features

- Formats arithmetic problems vertically
- Supports **addition** and **subtraction**
- Strict validation:
  - Max 5 problems
  - Numbers must be digits
  - Max 4-digit operands
  - Operators must be `+` or `-`
- Optional answer output
- Clean spacing and consistent layout
- Works as both:
  - 📦 Library (`arithmetic_arranger`)
  - 💻 CLI (`arithmetic-formatter`)
- Fully documented
- Test‑driven
- Modern Python packaging

---

## 📦 Installation

Install locally:

```bash
pip install .
```

---

## 🧪 Python Usage Example

```python
from arithmetic_formatter import arithmetic_arranger

print(
    arithmetic_arranger(
        ["32 + 698", "1 - 2", "45 + 43", "123 + 49"],
        show_answers=True
    )
)
```

Output:

```
   32         1      45      123
+ 698       - 2    + 43    +  49
-----     -----    ----    -----
  730        -1      88      172
```

---

## 💻 CLI Usage

### Basic usage:

```bash
arithmetic-formatter "32 + 698" "1 - 2"
```

### With answers:

```bash
arithmetic-formatter "32 + 8" "1 - 3801" --answers
```

---

## 🧪 Running Tests

```bash
pytest -v
```

---

## 📁 Project Structure

```
arithmetic_formatter/
    core.py
    cli.py
    formats/
docs/
tests/
screenshots/
.github/workflows/
mkdocs.yml
pyproject.toml
README.md
LICENSE
```

---

## 🤝 Contributing

Contributions are welcome!  
Please read the **CONTRIBUTING.md** file before submitting pull requests.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## ⭐ Roadmap

- Add JSON output mode
- Add LaTeX formatter
- Add colorized/pretty terminal formatting
- Add strict vs loose formatting modes
- Optionally publish to PyPI
