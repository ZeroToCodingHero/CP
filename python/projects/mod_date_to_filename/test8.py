import re
from pathlib import Path
from datetime import datetime

# ----------------------------- CONFIGURATION -----------------------------
directory = r"D:/test/2023/2023-01-15"  # <<< CHANGE THIS to your folder
recursive = True                    # True = process subfolders too
dry_run = True                       # True = preview only, False = actually change metadata

# Supported files (ones that can store EXIF date taken)
supported_exts = {
    # Photos
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif',
    '.heic', '.heif', '.webp', '.arw', '.cr2', '.nef', '.orf', '.rw2',
    # Videos
    '.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v', '.mpg', '.mpeg',
    '.wmv', '.flv', '.3gp', '.m2ts'}

# Supported extensions set for quick lookup
supported_exts = set(ext.lower() for ext in supported_exts)

# ----------------------------- DATE PATTERNS -----------------------------
patterns = [
    r"(\d{4})-(\d{2})-(\d{2})-(\d{2}h)(\d{2}m)(\d{2})",  # YYYY-MM-DD-HHhMMmSS
    r"(\d{4}-\d{2}-\d{2})",                  # YYYY-MM-DD
    r"(\d{8})",                              # YYYYMMDD (will assume 00:00:00)
    r"(\d{4}\d{2}\d{2})",                     # YYYYMMDD no separators
    r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})",  # YYYY-MM-DD_HH-MM-SS
    r"IMG[_-]?(\d{8})[_-]?\d*",              # IMG_YYYYMMDD or similar (WhatsApp style)
    r"^IMG_\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$", # IMG_YYYY-MM-DD_HH-MM-SS
    r"PXL[_-]?(\d{8})[_-]?\d*",              # Google Pixel style
    r"Photo[_-]?(\d{8})[_-]?\d*",            # PhotoYYYYMMDD style
    r"(\d{4}-\d{2}-\d{2}-\d{2}h\d{2}m\d{2}s)"  # YYYY-MM-DD-HHhMMmSS
]

# ----------------------------- DATE PATTERN EXTRACTION -----------------------------
def extract_date_from_filename(filename):
    """Extract date (and time if available) from filename using regex patterns."""
    name = Path(filename).stem  # Remove extension
    for pattern in patterns:
        match = re.search(pattern, name)
        if match:
            date_str = match.group(1)
            try:
                if len(date_str) == 8 and date_str.isdigit():
                    # YYYYMMDD -> YYYY:MM:DD 00:00:00
                    return datetime.strptime(date_str, "%Y%m%d").strftime("%Y:%m:%d %H:%M:%S")
                elif "_" in date_str or "-" in date_str.replace(date_str[:10], ""):
                    # Likely includes time: YYYY-MM-DD_HH-MM-SS or similar
                    date_str = date_str.replace("_", " ")  # Normalize
                    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").strftime("%Y:%m:%d %H:%M:%S")
                else:
                    # YYYY-MM-DD
                    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y:%m:%d 00:00:00")
            except ValueError:
                continue
    return None
# ----------------------------- MAIN PROCESSING -----------------------------
def main():
    path = Path(directory)
    if recursive:
        files = path.rglob('*')
    else:
        files = path.glob('*')

    for file in files:
        if file.suffix.lower() in supported_exts:
            date_taken = extract_date_from_filename(file.name)
            if date_taken:
                if dry_run:
                    print(f"[DRY RUN] Would update '{file}' with date taken: {date_taken}")
                else:
                    # Here you would add the code to actually update the metadata
                    print(f"Updating '{file}' with date taken: {date_taken}")
            else:
                print(f"No date found in filename: {file}")
if __name__ == "__main__":
    main()

# ----------------------------- END OF SCRIPT -----------------------------    