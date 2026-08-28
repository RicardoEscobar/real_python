from pathlib import Path
path = Path.cwd() / 'notes.md'
print(path.read_text(encoding='utf-8'))
print(repr(path.resolve()))