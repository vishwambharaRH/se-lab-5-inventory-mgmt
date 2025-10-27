### 1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest fix was to fix the casing of the functions from camel case to snake case.
Hardest (relatively) fix was to fix the file import error handling and the print eval statements.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

Document whitespace and line length was a false positive as noted. Any degradation in code score as given by Pylint is due to the supposed lack of whitespace.
The same can be said about camelcasing, because post camelcase to snake-case conversion, the total mark given by Pylint went from 7.01 to 8.06

### 3. How would you integrate static analysis tools into your actual software development workflow?

One local set of tests prior to integration, one post-integration test, and one complete test.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

A generally better error handling was observed. Code is overall more secure and neat, uniform also.