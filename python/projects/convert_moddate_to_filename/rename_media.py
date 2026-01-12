import os
import re
import sys
import argparse
from pathlib import Path

# Try to import tkinter for folder selection dialog (built-in with Python)
try:
    import tkinter as tk
    from tkinter import filedialog
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False


def select_folder_graphically():
    """Open a graphical folder picker dialog."""
    if not TKINTER_AVAILABLE:
        print("Graphical folder selection not available (tkinter missing).")
        return None
    
    # Import here to satisfy type checker after TKINTER_AVAILABLE check
    import tkinter as tk
    from tkinter import filedialog as fd
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.update()    # Ensure it processes the withdraw
    folder = fd.askdirectory(title="Select folder containing photos/videos")
    root.destroy()
    
    if folder and os.path.isdir(folder):
        return folder
    return None


def batch_rename_media(root_dir, execute=False):
    pattern = re.compile(r'^(\d{4}-\d{2}-\d{2})-(\d{2})h(\d{2})m(\d{2})s(\.[a-zA-Z0-9]+)$')
    
    media_extensions = {
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.heic', '.heif', '.webp',
        '.arw', '.cr2', '.nef', '.orf', '.rw2',
        '.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v', '.mpg', '.mpeg', '.wmv', '.flv', '.3gp', '.m2ts'
    }
    
    renamed = skipped = errors = 0
    root_path = Path(root_dir)

    print(f"Scanning: {root_path.resolve()}\n")

    for file_path in root_path.rglob('*'):  # Recursively find all files
        if not file_path.is_file():
            continue
        
        filename = file_path.name
        match = pattern.match(filename)
        if not match:
            continue

        date_part, hour, minute, second, ext = match.groups()
        ext = ext.lower()
        if ext not in media_extensions:
            continue

        new_name = f"{date_part}_{hour}-{minute}-{second}{ext}"
        if filename == new_name:
            continue

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
        description="Rename photos & videos: YYYY-MM-DD-HHhMMmSS.ext → YYYY-MM-DD_HH-MM-SS.ext",
        epilog="Tip: Drag and drop a folder onto this script, or double-click it to pick a folder."
    )
    parser.add_argument("directory", nargs="?", help="Folder to process (optional)")
    parser.add_argument("--execute", action="store_true", help="Actually rename files (otherwise dry-run only)")

    args = parser.parse_args()

    # Determine the folder
    folder = None

    if args.directory:
        folder = args.directory
    elif len(sys.argv) == 1 and (TKINTER_AVAILABLE or "darwin" in sys.platform or "win" in sys.platform):
        # No arguments → likely double-clicked or dragged → offer graphical picker
        print("No folder provided. Opening folder selector...\n")
        folder = select_folder_graphically()

    if not folder or not os.path.isdir(folder):
        if folder:
            print(f"Error: '{folder}' is not a valid folder.")
        else:
            print("No valid folder selected.")
        print("\nUsage examples:")
        print("   python rename_media.py /path/to/folder")
        print("   python rename_media.py /path/to/folder --execute")
        print("   Or drag a folder onto this script file.")
        sys.exit(1)

    print("Photo & Video Renamer")
    print("Converts: 2025-12-31-14h30m00s.jpg → 2025-12-31_14-30-00.jpg\n")

    if args.execute:
        print("WARNING: This will permanently rename files!\n")
        confirm = input("Type 'YES' to proceed with actual renaming: ")
        if confirm != "YES":
            print("Cancelled. (Dry-run is safe by default.)")
            sys.exit(0)
        batch_rename_media(folder, execute=True)
    else:
        print("DRY-RUN MODE: Showing what would be renamed (safe)\n")
        batch_rename_media(folder, execute=False)
        print("\nTo actually rename files, run again with --execute")