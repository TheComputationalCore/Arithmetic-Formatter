
Paste:

```markdown
# API Reference

This section documents the core functions provided by the package.

---

## `arithmetic_arranger(problems, show_answers=False)`

Arrange arithmetic problems vertically and side-by-side.

### Parameters

- **problems**: list of strings  
  Each item must follow `"number operator number"` format.

- **show_answers**: bool  
  Whether to include the computed answers.

---

### Returns

A formatted multi-line string.

---

### Example

```python
from arithmetic_formatter import arithmetic_arranger

print(arithmetic_arranger(["32 + 8", "1 - 3801"], True))
