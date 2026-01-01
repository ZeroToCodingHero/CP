import os
import re
from pathlib import Path
from datetime import datetime

# ----------------------------- CONFIGURATION -----------------------------
# Directory to process
directory = "//tank/photo/2023/2023-01-15"  # Change to your folder, e.g., r"C:\Users\You\Videos"

# Process subfolders recursively?
recursive = False

# Supported file extensions
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".tif", ".tiff", ".webp", ".bmp", ".gif"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".m4v", ".3gp", ".wmv"}

# Combine
SUPPORTED_EXTS = IMAGE_EXTS.union(VIDEO_EXTS)

# Dry run? (True = preview only)
dry_run = True

# Prefer EXIF/media metadata? (Highly recommended)
use_metadata = True

# Try to import Pillow for metadata extraction
TAGS = {}
Image = None
try:
    from PIL import Image
    from PIL.ExifTags import TAGS
except ImportError:
    if use_metadata:
        print("Pillow not installed. Run: pip install pillow")
        print("Falling back to filename + file creation time only.")
    use_metadata = False

# ----------------------------- HELPERS -----------------------------
def get_media_creation_date(file_path):
    """Extract creation date from image/video metadata (most accurate)."""
    if not use_metadata:
        return None

    try:
        if Image is None:
            return None
        with Image.open(file_path) as img:
            exif_data = img.getexif()
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id, tag_id)
                    if tag in ("DateTimeOriginal", "DateTime", "CreateDate", "MediaCreateDate"):
                        if isinstance(value, str) and ":" in value[:10]:  # YYYY:MM:DD format
                            cleaned = value.replace(":", "-", 2)  # Fix YYYY:MM:DD -> YYYY-MM-DD
                            return datetime.strptime(cleaned[:19], "%Y-%m-%d %H:%M:%S")
            # Fallback: some videos store it in other ways
            if hasattr(img, "info") and "datetime_original" in img.info:
                return datetime.strptime(img.info["datetime_original"], "%Y:%m:%d %H:%M:%S")
            if hasattr(img, "info") and "creation_time" in img.info:
                # Handle various formats
                dt_str = img.info["creation_time"]
                for fmt in ["%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%SZ", "%Y:%m:%d %H:%M:%S"]:
                    try:
                        if ":" in dt_str[:10]:
                            dt_str = dt_str.replace(":", "-", 2)
                        return datetime.strptime(dt_str[:19], fmt.replace("T", " ").replace("Z", ""))
                    except ValueError:
                        continue
    except Exception:
        pass  # Many video formats don't support full EXIF via Pillow
    return None

def get_file_creation_date(file_path):
    """Fallback: use file system creation time (often close on phones)."""
    try:
        timestamp = file_path.stat().st_birthtime  # macOS / some Linux
    except AttributeError:
        timestamp = file_path.stat().st_ctime  # Windows / fallback (creation or change)
    return datetime.fromtimestamp(timestamp)

def parse_date_from_filename(stem):
    """Parse date from common filename patterns (photos & videos)."""
    text = stem.upper()

    patterns = [
        (r"(\d{8}[_T]?\d{6})", "%Y%m%d%H%M%S"),
        (r"(\d{8}[_]\d{6})", "%Y%m%d_%H%M%S"),
        (r"(\d{4}-\d{2}-\d{2}[_ ]\d{2}[_.-]?\d{2}[_.-]?\d{2})", "%Y-%m-%d %H:%M:%S"),
        (r"(\d{4}\d{2}\d{2}[_]\d{6})", "%Y%m%d_%H%M%S"),
        (r"VID[_-](\d{8})", "%Y%m%d"),
        (r"VIDEO[_-](\d{8})", "%Y%m%d"),
        (r"(\d{4}-\d{2}-\d{2})", "%Y-%m-%d"),
        (r"(\d{4}\d{2}\d{2})", "%Y%m%d"),
        # WhatsApp videos
        (r"VID-(\d{8})-WA\d+", "%Y%m%d"),
    ]

    for regex, fmt in patterns:
        match = re.search(regex, text)
        if match:
            date_str = match.group(1)
            date_str = re.sub(r"[^\d]", "", date_str)  # Clean
            try:
                if len(date_str) == 8:
                    dt = datetime.strptime(date_str, "%Y%m%d")
                elif len(date_str) == 14:
                    dt = datetime.strptime(date_str, "%Y%m%d%H%M%S")
                elif len(date_str) == 12:
                    dt = datetime.strptime(date_str, "%Y%m%d%H%M")
                else:
                    continue
                return dt
            except ValueError:
                continue
    return None

def generate_new_name(dt, extension):
    return dt.strftime("%Y-%m-%d-%Hh%Mm%Ss") + extension.lower()

# ----------------------------- MAIN -----------------------------
def main():
    path = Path(directory)
    if not path.is_dir():
        print(f"Directory not found: {directory}")
        return

    glob_method = path.rglob if recursive else path.glob
    files = [f for f in glob_method("*") if f.is_file() and f.suffix.lower() in SUPPORTED_EXTS]

    if not files:
        print("No supported photo or video files found.")
        return

    print(f"Found {len(files)} file(s). {'(Dry run)' if dry_run else '(Renaming)'}\n")

    renamed = skipped = 0

    for file_path in sorted(files):
        dt = None
        source = ""

        # 1. Try embedded media metadata (best)
        dt = get_media_creation_date(file_path)
        if dt:
            source = "metadata"

        # 2. Try filename
        if not dt:
            dt = parse_date_from_filename(file_path.stem)
            if dt:
                source = "filename"

        # 3. Last resort: file creation time
        if not dt:
            dt = get_file_creation_date(file_path)
            source = "file system"

        new_base = generate_new_name(dt, file_path.suffix)
        new_path = file_path.with_name(new_base)

        # Handle name conflicts
        counter = 1
        orig_new_path = new_path
        while new_path.exists() and new_path != file_path:
            new_name = generate_new_name(dt, "") + f"-{counter}" + file_path.suffix.lower()
            new_path = file_path.with_name(new_name)
            counter += 1

        if new_path.name.lower() == file_path.name.lower():
            print(f"No change: {file_path.name}")
            continue

        action = " => " if dry_run else " -> "
        file_type = "Photo" if file_path.suffix.lower() in IMAGE_EXTS else "Video"
        print(f"{file_type}: {file_path.name} {action} {new_path.name}  ({source})")

        if not dry_run:
            try:
                file_path.rename(new_path)
                renamed += 1
            except Exception as e:
                print(f"Error renaming {file_path.name}: {e}")
                skipped += 1
        else:
            if source == "file system":
                skipped += 1  # Optional: count potential inaccuracies

    print("\n" + "="*60)
    print(f"Done! Renamed: {renamed} | Skipped/No change: {len(files) - renamed}")
    if dry_run:
        print("This was a dry run. Set dry_run = False to apply changes.")

if __name__ == "__main__":
    main()