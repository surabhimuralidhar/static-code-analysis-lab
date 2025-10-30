\# 🧪 Static Code Analysis Lab



\## 🎯 Objective

Enhance Python code quality, security, and style using \*\*Pylint\*\*, \*\*Bandit\*\*, and \*\*Flake8\*\* on the `inventory\_system.py` file.



---



\## 📊 Known Issues and Fixes



| Issue Type | Line(s) | Description | Fix Approach |

|-------------|----------|--------------|---------------|

| Mutable Default Argument | 12 | `logs=\[]` shared across calls | Change default to `None` and initialize inside method |

| Broad Exception | 45 | Using `except:` without specifying error type | Replace with `except Exception as e:` |

| Insecure Function | 78 | Use of `eval()` on input | Replace with `ast.literal\_eval()` or safer logic |

| Poor Logging | 90 | Print statements used for debugging | Replace with `logging` module usage |



---



\## 🧰 Tools Used

\- \*\*Pylint\*\* → Code quality checker  

\- \*\*Flake8\*\* → PEP8 style and syntax checker  

\- \*\*Bandit\*\* → Security vulnerability scanner  



---



\## 🧩 Reflection



\*\*1. Which issues were easiest/hardest to fix?\*\*  

\- Easiest: Replacing print statements with logging.  

\- Hardest: Refactoring functions that used mutable defaults and broad exceptions.



\*\*2. Any false positives reported?\*\*  

\- Bandit flagged a harmless use of `input()` which was already sanitized.



\*\*3. How would you integrate static analysis into real projects?\*\*  

\- Add Pylint and Flake8 checks in a \*\*CI pipeline (GitHub Actions)\*\* before merge.



\*\*4. Improvements observed after fixes:\*\*  

\- Code readability improved, logging added structure, and potential vulnerabilities removed.



---



\## 👩‍💻 Author

\*\*Surabhi Muralidhar\*\*  

5th Semester — Software Engineering Lab  



