"""This script connects to a SMB folder and lists the files in it."""
import os
from pathlib import Path
import subprocess
import sys
from turtle import width

from PIL import Image


samba_dir = Path(r'\\192.168.1.253\gallery-dl\pixiv\32324489 user_fsxa3285')


def file_generator(samba_dir: Path):
    files = sorted(samba_dir.iterdir(), key=lambda path: path.stat().st_mtime, reverse=True)
    for file in files:
        yield file


def open_in_default_viewer(file: Path):
    """Open a file with the operating system default app."""
    if os.name == 'nt':
        os.startfile(file)  # type: ignore[attr-defined]
    elif sys.platform == 'darwin':
        subprocess.run(['open', str(file)], check=False)
    else:
        subprocess.run(['xdg-open', str(file)], check=False)

def get_binary_data_line(file: Path, lines: int = 10):
    with file.open('rb') as f:
        for _ in range(lines):
            line = f.readline()
            if not line:
                break
            print(line)
            input()

def mirror_img(path: Path) -> bytes:
    """Mirror the image horizontally and return the binary data."""
    with Image.open(path) as img:
        mirrored = img.transpose(Image.FLIP_LEFT_RIGHT)
        width, height = mirrored.size
        return mirrored.tobytes(), width, height
    
def show_image_bytes(image_bytes: bytes, width: int, height: int):
    """Open the image from bytes data and display it."""
    # Convert the bytes back to an image
    image = Image.frombytes('RGB', (width, height), image_bytes)
    image.show()
    

if __name__ == "__main__":
    # Open a JPEG file in binary mode
    for file in file_generator(samba_dir):
        # Only process JPEG files
        if file.suffix.lower() in ['.jpg', '.jpeg']:
            # Mirror the image and display it
            image_bytes, width, height = mirror_img(file)
            show_image_bytes(image_bytes, width, height)
            input("Press Enter to continue to the next image...")
