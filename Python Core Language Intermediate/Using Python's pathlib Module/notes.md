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
```python
from pathlib import Path
path = Path.cwd() / 'notes.md'
print(path.read_text(encoding='utf-8'))
print(repr(path.resolve()))
```
# Moving and deleting files
- .rename(): Renames or moves a file or directory.
- .unlink(): Deletes a file or symbolic link. Use .rmdir() to delete an empty directory.

```python
from pathlib import Path
path = Path.cwd() / 'notes.md'
new_path = Path.cwd() / 'notes_renamed.md'
path.rename(new_path)  # Renames the file
new_path.unlink()  # Deletes the file
```
# Picking up the parts of a path
- .name: The final component of the path (file or directory name).
- .stem: The final component of the path without its suffix (file extension).
- .suffix: The file extension of the final component, including the dot.
- .parent: The directory containing the file or directory.
- .anchor: The part of the path before the root (e.g., 'C:\' on Windows or '/' on Unix).

```python
from pathlib import Path
path = Path('/home/user/projects/notes.md')
print(path.name)   # Output: 'notes.md'
print(path.stem)   # Output: 'notes'
print(path.suffix) # Output: '.md'
print(path.parent) # Output: '/home/user/projects'
print(path.anchor) # Output: '/'
```
