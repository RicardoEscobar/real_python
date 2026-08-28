"""Exercise: Read a File With Pathlib
Write a function read_file() that takes a directory path string and a filename string, builds a Path object, and returns the text content of the file.

Examples
read_file("/home/user/docs", "notes.txt")
outputs
'Meeting at 3pm'
read_file("/tmp", "hello.txt")
outputs
'Hello, World!'

Requirements
Accept a directory path string and a filename string
Use the / operator to join them into a Path
Return the text content of the file using .read_text()
"""
from pathlib import Path


def read_file(directory = ".", filename = None):
    """Read and return the text content of a file."""
    if directory is None:
        directory = "."
    if filename is None:
        raise ValueError("Filename must be provided.")

    path = Path(directory) / filename
    return path.read_text()

if __name__ == '__main__':
    dir = None
    filename = "example.txt"
    print(read_file(dir, filename))
