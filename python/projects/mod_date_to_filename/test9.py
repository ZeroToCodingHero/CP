import re
from pathlib import Path
from datetime import datetime

# ----------------------------- CONFIGURATION -----------------------------
directory = r"D:/test/2023/2023-01-19"  # <<< CHANGE THIS to your folder
recursive = True                        # Process subfolders?
dry_run = False                         # False = actually write metadata

# Supported extensions (photos + videos that can store creation date)
SUPPORTED_EXTENSIONS = {
    '.jpg', '.jpeg', '.png', '.tiff', '.tif', '.heic', '.heif', '.webp',
    '.arw', '.cr2', '.nef', '.orf', '.rw2',  # RAW photos
    '.mp4', '.mov', '.avi', '.mkv', '.m4v', '.3gp'
}

# ----------------------------- COMPREHENSIVE PATTERNS -----------------------------
# Each tuple: (regex_pattern, strptime_format, example)
DATE_PATTERNS = [
    # 1. YYYY-MM-DD-HHhMMmSS or YYYY-MM-DD-HHhMMmSSs
    (r"(\d{4}-\d{2}-\d{2}-\d{2}h\d{2}m\d{2}m?\d*s?)", "%Y-%m-%d-%Hh%Mm%S"),
    
    # 2. YYYY-MM-DD_HH-MM-SS
    (r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})", "%Y-%m-%d_%H-%M-%S"),
    
    # 3. WhatsApp: IMG-YYYYMMDD-WAxxxx.jpg or IMG_YYYYMMDD_xxxx.jpg
    (r"IMG[_-]?(\d{8})", "%Y%m%d"),
    
    # 4. Full WhatsApp/Google: IMG_YYYYMMDD_HHMMSS.jpg
    (r"IMG[_-](\d{8}_\d{6})", "%Y%m%d_%H%M%S"),
    
    # 5. Google Pixel: PXL_YYYYMMDD_HHMMSS.jpg
    (r"PXL[_-]?(\d{8}_\d{6})", "%Y%m%d_%H%M%S"),
    
    # 6. YYYY-MM-DD
    (r"(\d{4}-\d{2}-\d{2})", "%Y-%m-%d"),
    
    # 7. YYYYMMDD (bare or at start)
    (r"(\d{8})", "%Y%m%d"),
    
    # 8. Screenshot style: Screenshot_YYYY-MM-DD-HH-MM-SS.png
    (r"Screenshot[_-]?(\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2})", "%Y-%m-%d-%H-%M-%S"),
]

def extract_date_from_filename(filename: str) -> str | None:
    """Return date string in 'YYYY:MM:DD HH:MM:SS' format or None."""
    stem = Path(filename).stem

    for pattern, fmt in DATE_PATTERNS:
        match = re.search(pattern, stem, re.IGNORECASE)
        if match:
            date_str = match.group(1)
            try:
                # Handle different formats
                if fmt == "%Y-%m-%d-%Hh%Mm%S":
                    date_str = date_str.replace('h', ':').replace('m', ':').replace('s', '')
                    dt = datetime.strptime(date_str, "%Y-%m-%d-%H:%M:%S")
                elif fmt == "%Y-%m-%d_%H-%M-%S":
                    dt = datetime.strptime(date_str, "%Y-%m-%d_%H-%M-%S")
                else:
                    dt = datetime.strptime(date_str, fmt)
                    if len(date_str) == 8:  # Only date → midnight
                        dt = dt.replace(hour=0, minute=0, second=0)
                return dt.strftime("%Y:%m:%d %H:%M:%S")
            except ValueError:
                continue
    return None

# ----------------------------- METADATA WRITING (OPTIONAL) -----------------------------
# Uncomment and install required library to enable actual writing

try:
    import piexif  # pip install piexif  (for JPEG/TIFF)
    def set_exif_date(filepath: Path, date_str: str):
        if filepath.suffix.lower() in {".jpg", ".jpeg", ".tiff", ".tif"}:
            exif_dict = piexif.load(str(filepath))
            exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = date_str
            exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = date_str
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, str(filepath))
except ImportError:
    def set_exif_date(filepath: Path, date_str: str):
        print(f"[WARNING] piexif not installed – cannot write EXIF to {filepath}")

# For videos and other formats, you’d need exiftool (via subprocess) or pyexiv2/hachoir

# ----------------------------- MAIN -----------------------------
def main():
    path = Path(directory)
    pattern = '**/*' if recursive else '*'
    files = [f for f in path.glob(pattern) if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS]

    updated = 0
    skipped = 0

    for file in files:
        date_taken = extract_date_from_filename(file.name)
        if date_taken:
            if dry_run:
                print(f"[DRY RUN] Would set '{file.name}' → {date_taken}")
            else:
                print(f"Updating '{file.name}' → {date_taken}")
                set_exif_date(file, date_taken)
            updated += 1
        else:
            print(f"No date pattern matched: {file.name}")
            skipped += 1

    print(f"\nDone: {updated} files would be/have been updated, {skipped} skipped.")

if __name__ == "__main__":
    main()
# ----------------------------- END OF SCRIPT -----------------------------