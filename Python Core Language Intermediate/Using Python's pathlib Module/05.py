from pathlib import Path

source = Path.cwd() / 'notes.md'
destination = Path.cwd() / 'notes_copy.md'
with destination.open('x', encoding='utf-8') as file:
    file.write(source.read_text(encoding='utf-8'))

# Crerate test directory
test_dir = Path.cwd() / 'test'
test_dir.mkdir(exist_ok=True)
input("Press Enter to delete the test directory...")
# Delete the directory
test_dir.rmdir()