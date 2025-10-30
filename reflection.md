**Reflection**



1. Which issues were easiest and hardest to fix?

The easiest fixes were replacing `print` statements with proper logging and changing mutable default arguments.  

The hardest fix involved restructuring exception handling and ensuring safe file operations using context managers.



2. Did the tools report any false positives?

Yes, Bandit warned about the use of global variables, which was acceptable for this small script.  

Otherwise, all reported issues were valid and improved the code quality.



3. How would you integrate static analysis tools into real projects?

These tools can be added to a CI/CD pipeline (like GitHub Actions) so that every pull request automatically runs Pylint, Flake8, and Bandit before merging.  

Developers can also run them locally before committing.



4. Tangible improvements observed:

\- Code readability and maintainability improved significantly.  

\- Logging replaced print statements, making debugging easier.  

\- The script became safer and followed Python best practices.  

\- Security risks like `eval()` were completely removed.



