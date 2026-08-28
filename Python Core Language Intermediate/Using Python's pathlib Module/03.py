from pathlib import Path
path = Path.cwd() / 'notes.md'

# Using the open() function with a Path object
print("--- Using open() with a Path object ---")
with open(path, 'r', encoding='utf-8') as file:
    headers = [line.strip() for line in file if line.startswith('#') ]
print('\n'.join(headers))

# Using Path objects with the open() function is a convenient way to read and write files. The open() function can accept a Path object directly, so you don't need to convert it to a string first. This allows you to work with file paths in a more intuitive and object-oriented way.
print("--- Using Path objects with open() ---")
with path.open('r', encoding='utf-8') as file:
    headers = [line.strip() for line in file if line.startswith('#') ]
print('\n'.join(headers))