import os
import zipfile


def zip_directory(src_dir, archive_path):
    """Write every file in src_dir into a new ZIP at archive_path."""
    with zipfile.ZipFile(archive_path, 'w') as archive:
        for file in os.listdir(src_dir):
            full_path = os.path.join(src_dir, file)

            if os.path.isfile(full_path):
                archive.write(full_path, arcname=file)


if __name__ == '__main__':
    zip_directory('borrame1', 'data.zip')
    with zipfile.ZipFile('data.zip') as archive:
        print(archive.namelist())
    os.remove('data.zip')