"""This script arechives a given directory into a TAR file."""
import tarfile
from pathlib import Path


# Esta es una funcion decoradora que mide el tiempo de ejecucion de la funcion que se le pasa como argumento
def timeit(func):
    """Decorator to measure the execution time of a function."""
    import time

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")
        return result

    return wrapper


@timeit
def archive_directory(source_dir: Path, archive_path: Path):
    """Archive the source directory into a TAR file."""
    with tarfile.open(archive_path, "w") as tar:
        tar.add(source_dir, arcname=source_dir.name)

if __name__ == "__main__":
    source_directory = Path(r"\\192.168.1.253\gallery-dl\pixiv\32324489 user_fsxa3285")
    archive_file = Path("32324489 user_fsxa3285.tar")
    archive_directory(source_directory, archive_file)
    print(f"Archived {source_directory} to {archive_file}")
    # Extract the archive to current directory:
    # with tarfile.open(archive_file, "r") as tar:
    #     tar.extractall()
    # print(f"Extracted {archive_file} to current directory/")
