# Using Python's pathlib Module

In this video course, you’ll learn how to:

- Work with file paths in Python
- Read and write files in new ways
- Manipulate paths and the underlying file system
- List files and iterate over them

# Creating paths
```python
import pathlib
print(pathlib.Path.cwd())
# Output: /home/user/projects
```
Or
```python
from pathlib import Path
print(Path.cwd())
# Output: /home/user/projects
```
# Raw strings for Windows paths
To avoid problems with backslashes in Windows file paths, you can use raw strings by prefixing the string with 'r'.

```python
from pathlib import Path
path = Path(r'C:\Users\Ricardo\Git\real_python\Python Core Language Intermediate\Using Python\'s pathlib Module\02.py')
print(path)
```
# Path file methods
- .read_text(): Reads the contents of the file as a string.
- .read_bytes(): Reads the contents of the file as bytes.
- .write_text(): Writes a string to the file, creating it if it doesn't exist or overwriting it if it does.
- .write_bytes(): Writes bytes to the file, creating it if it doesn't exist or overwriting it if it does.

# Reading and writing files
# Moving and deleting files