import os
import datetime
from pathlib import Path

gallery_dir = Path(r'\\192.168.1.253\gallery-dl\pixiv\32324489 user_fsxa3285')

# print(os.listdir(gallery_dir))

start_time = datetime.datetime.now()
for file in os.scandir(gallery_dir):
    if file.is_file():
        print(file.name)
end_time = datetime.datetime.now()
print(f"Time taken: {end_time - start_time}")

start_time = datetime.datetime.now()
for file in gallery_dir.iterdir():
    if file.is_file():
        print(file.name)
end_time = datetime.datetime.now()
print(f"Time taken: {end_time - start_time}")