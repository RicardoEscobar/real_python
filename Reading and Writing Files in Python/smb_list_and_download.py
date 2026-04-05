"""Connect to an SMB share, list a directory, and download one file.

Usage example:
python smb_list_and_download.py --username user_fsxa3285 --server-ip 192.168.1.253 --share gallery-dl --remote-dir /pixiv/32324489

You can also set SMB_PASSWORD as an environment variable to avoid prompts.
"""

from __future__ import annotations

import argparse
import getpass
import os
from pathlib import Path

from smb.SMBConnection import SMBConnection


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List and download from an SMB share")
    parser.add_argument("--username", required=True, help="SMB username")
    parser.add_argument("--password", default=None, help="SMB password (optional)")
    parser.add_argument("--server-ip", required=True, help="SMB server IP, e.g. 192.168.1.253")
    parser.add_argument("--server-name", default=None, help="SMB server name/host (optional)")
    parser.add_argument("--share", required=True, help="Share name, e.g. gallery-dl")
    parser.add_argument("--remote-dir", required=True, help="Path inside share, e.g. /pixiv/32324489")
    parser.add_argument("--client-name", default="python-client", help="Local client name")
    parser.add_argument(
        "--download-dir",
        default="downloads",
        help="Local folder where one sample file is downloaded",
    )
    return parser.parse_args()


def get_password(cli_password: str | None) -> str:
    if cli_password:
        return cli_password

    env_password = os.getenv("SMB_PASSWORD")
    if env_password:
        return env_password

    return getpass.getpass("SMB password: ")


def main() -> int:
    args = parse_args()
    password = get_password(args.password)

    server_name = args.server_name or args.server_ip

    conn = SMBConnection(
        args.username,
        password,
        args.client_name,
        server_name,
        use_ntlm_v2=True,
        is_direct_tcp=True,
    )

    connected = conn.connect(args.server_ip, 445, timeout=10)
    if not connected:
        print("Failed to connect to SMB server.")
        return 1

    try:
        entries = [
            entry
            for entry in conn.listPath(args.share, args.remote_dir)
            if entry.filename not in {".", ".."}
        ]

        if not entries:
            print("No files found in the remote directory.")
            return 0

        print(f"Found {len(entries)} entries in {args.remote_dir}:")
        for entry in entries:
            kind = "DIR " if entry.isDirectory else "FILE"
            print(f"{kind:4} {entry.filename} ({entry.file_size} bytes)")

        # Download the first regular file as a connectivity test.
        first_file = next((e for e in entries if not e.isDirectory), None)
        if first_file is None:
            print("No regular file to download in this directory.")
            return 0

        download_dir = Path(args.download_dir)
        download_dir.mkdir(parents=True, exist_ok=True)

        local_path = download_dir / first_file.filename
        remote_file = f"{args.remote_dir.rstrip('/')}/{first_file.filename}"

        with local_path.open("wb") as handle:
            conn.retrieveFile(args.share, remote_file, handle)

        print(f"Downloaded: {remote_file}")
        print(f"Saved to: {local_path.resolve()}")
        return 0
    finally:
        conn.close()


if __name__ == "__main__":
    raise SystemExit(main())
