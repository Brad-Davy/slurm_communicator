import shutil
import sys
import subprocess


def is_process_running(process_name):
    result = subprocess.run(
        ["pgrep", "-f", process_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.returncode == 0


def sinfo_is_present():
    sinfo_path = shutil.which("sinfo")

    if sinfo_path:
        print(f"sinfo found at: {sinfo_path}")
        return True
    else:
        print("sinfo not found on this system.")
        return False


def sacct_is_present():
    sacct_path = shutil.which("sacct")

    if sacct_path:
        print(f"sacct found at: {sacct_path}")
        return True
    else:
        print("sacct not found on this system.")
        return False
