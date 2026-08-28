import os
import shutil


def backup_file(src_path, dst_dir):
    """Copy src_path to dst_dir with metadata; return the new path."""
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    dst_path = os.path.join(dst_dir, os.path.basename(src_path))
    shutil.copy2(src_path, dst_path)
    return dst_path