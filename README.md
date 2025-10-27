# Lab 5: Static Code Analysis

This file contains the deliverables for the static code analysis lab.
**Deliverable 1:** The cleaned code is saved as `updated_inventory_sys.py`.
**Deliverable 2:** The issue-tracking table is below.
**Deliverable 3:** The reflection questions and answers are in reflection.md.

---

## Deliverable 2: Identified Issues Table

This table documents a minimum of four high- and medium-priority issues identified by `bandit`, `pylint`, and `flake8` and the approach taken to fix them.

| Issue | Type | Tool(s) | Line(s) | Description | Fix Approach |
| --- | --- | --- | --- | --- | --- |
| **Dangerous `eval()` use** | Security | Bandit (B307), Pylint (W0123) | 59 | Use of `eval()` is a high-security risk as it can execute arbitrary code. | Removed the `eval()` call and replaced it with a standard `print('eval used')` statement. |
| **Mutable Default Argument** | Bug | Pylint (W0102) | 8 | Using `logs=[]` as a default argument means the *same list* is shared across all calls, leading to unexpected behavior. | Changed the default argument to `logs=None` and initialized a new `logs = []` list inside the function if it was `None`. |
| **Bare `except` / `pass`** | Bug / Style | Bandit (B110), Pylint (W0702), Flake8 (E722) | 19 | Using a bare `except:` catches all exceptions, including `SystemExit` or `KeyboardInterrupt`, and can hide bugs. | Replaced the bare `except:` with a specific `except KeyError:`. This now only catches the expected error (trying to remove an item that doesn't exist) and lets other errors surface. |
| **Unused Import** | Style / Maint. | Pylint (W0611), Flake8 (F401) | 2 | The `logging` module was imported but never used, adding unnecessary clutter to the file. | Removed the `import logging` line completely. |

---

## Deliverable 3: Reflection
Check the file [reflection.md](reflection.md)

