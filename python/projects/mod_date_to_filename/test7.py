import os
import re
import sys
import argparse
from pathlib import Path

# =============================================
#       USER CONFIGURATION SECTION
# =============================================
# Change these values if you want different behavior

# Input filename pattern (default matches your original: YYYY-MM-DD-HHhMMmSS.ext)
INPUT_PATTERN = r'^(\d{4}-\d{2}-\d{2})-(\d{2})h(\d{2})m(\d{2})s(\.[a-zA-Z0-9]+)$'

# Output filename format
# Available parts: {date}, {hour}, {minute}, {second}, {ext}
# Example: "{date}_{hour}-{minute}-{second}{ext}"  →  2025-12-31_14-30-00.jpg
OUTPUT_FORMAT = "{date}_{hour}-{minute}-{second}{ext}"

# File extensions to process (add or remove as needed)
MEDIA_EXTENSIONS = {
    # Photos
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif',
    '.heic', '.heif', '.webp', '.arw', '.cr2', '.nef', '.orf', '.rw2',
    # Videos
    '.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v', '.mpg', '.mpeg',
    '.wmv', '.flv', '.3gp', '.m2ts'
}

# Confirmation prompt text (you can make it stricter or friendlier)
CONFIRM_PROMPT = "Do you want to permanently rename these files? (y/n): "

# What to accept as "yes" (case-insensitive)
YES_RESPONSES = {"y", "yes"}

# =============================================
#       END OF USER CONFIGURATION
# =============================================

# Compile the regex once for speed
pattern = re.compile(INPUT_PATTERN)


# Optional: Graphical folder picker
try:
    import tkinter as tk
    from tkinter import filedialog
    TKINTER_AVAILABLE = True
except ImportError:
    tk = None
    filedialog = None
    TKINTER_AVAILABLE = False


def select_folder_graphically():
    if not TKINTER_AVAILABLE or tk is None or filedialog is None:
        return None
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select folder with photos and videos")
    root.destroy()
    return folder if folder else None


def batch_rename_media(root_dir, execute=False):
    root_path = Path(root_dir)
    renamed = skipped = errors = 0

    print(f"Scanning: {root_path.resolve()}\n")

    for file_path in root_path.rglob('*'):
        if not file_path.is_file():
            continue

        match = pattern.match(file_path.name)
        if not match:
            continue

        date_part, hour, minute, second, ext = match.groups()
        ext = ext.lower()
        if ext not in MEDIA_EXTENSIONS:
            continue

        new_name = OUTPUT_FORMAT.format(
            date=date_part,
            hour=hour,
            minute=minute,
            second=second,
            ext=ext
        )

        if file_path.name == new_name:
            continue  # Already correct

        new_path = file_path.with_name(new_name)

        if new_path.exists():
            print(f"SKIP: {new_path.name} already exists")
            skipped += 1
            continue

        if execute:
            try:
                file_path.rename(new_path)
                print(f"→ {new_path.name}")
                renamed += 1
            except Exception as e:
                print(f"ERROR {file_path.name}: {e}")
                errors += 1
        else:
            print(f"→ {new_path.name}")
            renamed += 1

    print("\n" + "="*40)
    mode = "EXECUTED" if execute else "DRY-RUN"
    print(f"{mode} SUMMARY:")
    print(f"  Renamed:   {renamed}")
    print(f"  Skipped:   {skipped}")
    if errors:
        print(f"  Errors:    {errors}")
    print("="*40)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rename photos & videos from custom timestamp format",
        epilog="Drag a folder onto this script or double-click it to select a folder."
    )
    parser.add_argument("directory", nargs="?", help="Folder to process")
    parser.add_argument("--execute", action="store_true", help="Actually rename files")

    args = parser.parse_args()

    folder = args.directory or select_folder_graphically()

    if not folder or not os.path.isdir(folder):
        print("Error: No valid folder selected or provided.")
        print("\nTip: Drag a folder onto this script, or run:")
        print("   python rename_media.py \"path/to/folder\"")
        sys.exit(1)

    print("Custom Media Renamer")
    print("Easy to configure — just edit the settings at the top of the script!\n")

    if args.execute:
        print("WARNING: Files will be permanently renamed!\n")
        response = input(CONFIRM_PROMPT).strip().lower()
        if response not in YES_RESPONSES:
            print("Cancelled — no files were changed.")
            sys.exit(0)
        print()
        batch_rename_media(folder, execute=True)
    else:
        print("DRY-RUN: Showing what would be renamed (safe preview)\n")
        batch_rename_media(folder, execute=False)
        print("\nTo actually rename, run again with --execute")
