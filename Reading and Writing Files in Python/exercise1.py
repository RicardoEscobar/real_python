import os


def join_and_read(*parts):
    """Join path parts and return the file's content."""
    content = None
    path = os.path.join(*parts)

    # Open the file and get the contents
    with open(path) as file:
        return file.read()


try:
    print(join_and_read("data", "greeting.txt"))
except Exception as e:
    print(e)
