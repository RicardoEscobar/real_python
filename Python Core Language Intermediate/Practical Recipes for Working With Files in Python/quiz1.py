import os


def count_directories(root):
    """Return the number of subdirectories under root."""
    count = 0
    for root, dirs, files in os.walk(root):
        count += len(dirs)
    return count

if __name__ == "__main__":
    print(count_directories("."))
