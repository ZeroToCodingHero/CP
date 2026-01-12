import os
import re
from pathlib import Path
from datetime import datetime

# ----------------------------- CONFIGURATION -----------------------------
directory = "//tank/photo/2023/2023-01-15"  # Change to your folder
recursive = True          # Now safer to enable
dry_run = True            # Set to False to actually rename
use_metadata = True       # Highly recommended

# Supported extensions
IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".heic", ".heif", ".tif", ".tiff", ".webp", ".bmp", ".gif"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv", ".m4v", ".3gp", ".wmv", ".m2ts"}
SUPPORTED_EXTS = IMAGE_EXTS.union(VIDEO_EXTS)

# Optional: install with: pip install pillow exifread hachoir
try:
    from PIL import Image
    from PIL.ExifTags import TAGS as PIL_TAGS
except ImportError:
    Image = None
    PIL_TAGS = None

try:
    import exifread
except ImportError:
    exifread = None

try:
    from hachoir.metadata import extractMetadata
    from hachoir.parser import createParser
except ImportError:
    extractMetadata = createParser = None

# ----------------------------- HELPERS -----------------------------
def get_media_creation_date(file_path):
    """Best effort to extract creation date from metadata."""
    if not use_metadata:
        return None, "disabled"

    str_path = str(file_path)

    # 1. Pillow (good for JPEG, HEIC, some MOV)
    if Image and PIL_TAGS:
        try:
            with Image.open(str_path) as img:
                exif = img.getexif()
                if exif:
                    for tag_name in ["DateTimeOriginal", "DateTime", "CreateDate", "MediaCreateDate"]:
                        tag_id = {v: k for k, v in PIL_TAGS.items()}.get(tag_name)
                        if tag_id and tag_id in exif:
                            value = exif[tag_id]
                            if isinstance(value, str):
                                value = value.strip()
                                if ":" in value[:10]:
                                    value = value.replace(":", "-", 2)
                                try:
                                    return datetime.strptime(value[:19], "%Y-%m-%d %H:%M:%S"), "PIL EXIF"
                                except ValueError:
                                    continue
                # Some videos have it in info
                if "datetime_original" in img.info:
                    dt_str = img.info["datetime_original"]
                    dt_str = dt_str.replace(":", "-", 2) if ":" in dt_str[:10] else dt_str
                    return datetime.strptime(dt_str[:19], "%Y-%m-%d %H:%M:%S"), "PIL info"
        except Exception:
            pass

    # 2. exifread (better for some formats)
    if exifread:
        try:
            with open(str_path, 'rb') as f:
                tags = exifread.process_file(f, details=False)
                for tag in ["EXIF DateTimeOriginal", "Image DateTime", "EXIF CreateDate"]:
                    if tag in tags:
                        value = str(tags[tag])
                        value = value.replace(":", "-", 2) if ":" in value[:10] else value
                        return datetime.strptime(value[:19], "%Y-%m-%d %H:%M:%S"), "exifread"
        except Exception:
            pass

    # 3. hachoir (excellent for video files: MP4, MOV, AVI, etc.)
    if extractMetadata and createParser:
        try:
            parser = createParser(str_path)
            if parser:
                metadata = extractMetadata(parser)
                if metadata:
                    for line in metadata:
                        if line.startswith("Creation date:") or line.startswith("Date created:"):
                            dt_str = line.split(":", 1)[1].strip()
                            for fmt in [
                                "%Y-%m-%d %H:%M:%S",
                                "%Y-%m-%d %H:%M:%S%z",
                                "%Y-%m-%dT%H:%M:%S",
                            ]:
                                try:
                                    if "%z" in fmt:
                                        dt = datetime.strptime(dt_str, fmt)
                                    else:
                                        dt = datetime.strptime(dt_str[:19], fmt)
                                    return dt, "hachoir"
                                except ValueError:
                                    continue
        except Exception:
            pass

    return None, None

def get_file_creation_date(file_path):
    """Fallback: filesystem birth/creation time."""
    try:
        timestamp = file_path.stat().st_birthtime  # macOS preferred
    except AttributeError:
        timestamp = file_path.stat().st_ctime      # Windows fallback
    return datetime.fromtimestamp(timestamp), "filesystem"

def parse_date_from_filename(stem):
    """Extended patterns for common phone/camera naming."""
    text = stem.upper()

    patterns = [
        (r"(\d{8}[_T]?\d{6})", "%Y%m%d%H%M%S"),
        (r"(\d{8}[_]\d{6})", "%Y%m%d_%H%M%S"),
        (r"(\d{4}-\d{2}-\d{2}[_ ]\d{2}[_.-]?\d{2}[_.-]?\d{2})", "%Y-%m-%d %H:%M:%S"),
        (r"(\d{4}\d{2}\d{2}[_T]?\d{6})", "%Y%m%d%H%M%S"),
        (r"IMG[_-](\d{8})[_-]?\d+", "%Y%m%d"),
        (r"PXL[_-](\d{8})[_-]?\d+", "%Y%m%d"),
        (r"VID[_-](\d{8})[_-]?\d+", "%Y%m%d"),
        (r"VIDEO[_-](\d{8})", "%Y%m%d"),
        (r"(\d{4}-\d{2}-\d{2})", "%Y-%m-%d"),
        (r"(\d{4}\d{2}\d{2})", "%Y%m%d"),
        (r"VID-(\d{8})-WA\d+", "%Y%m%d"),           # WhatsApp
        (r"IMG-(\d{8})-WA\d+", "%Y%m%d"),
        (r"SNAPCHAT-\d+-(\d{8})", "%Y%m%d"),
        (r"MOV_\d+_(\d{8})", "%Y%m%d"),
    ]

    for regex, fmt in patterns:
        match = re.search(regex, text)
        if match:
            date_str = re.sub(r"[^\d]", "", match.group(1))
            try:
                if len(date_str) == 8:
                    return datetime.strptime(date_str, "%Y%m%d"), "filename"
                elif len(date_str) == 14:
                    return datetime.strptime(date_str, "%Y%m%d%H%M%S"), "filename"
            except ValueError:
                continue
    return None, None

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
        print("No supported media files found.")
        return

    print(f"Found {len(files)} file(s). {'(DRY RUN)' if dry_run else '(RENAMING)'}\n")

    renamed = no_change = errors = 0

    for file_path in sorted(files):
        dt = source = None

        # Priority 1: Metadata
        dt, source = get_media_creation_date(file_path)
        if dt:
            source = f"metadata ({source})"

        # Priority 2: Filename
        if not dt:
            dt, source = parse_date_from_filename(file_path.stem)
            if dt:
                source = "filename"

        # Priority 3: Filesystem
        if not dt:
            dt, source = get_file_creation_date(file_path)

        new_name = generate_new_name(dt, file_path.suffix)
        new_path = file_path.with_name(new_name)

        # Conflict resolution
        counter = 1
        original_new = new_path
        while new_path.exists() and new_path != file_path:
            new_name = generate_new_name(dt, "") + f"-{counter}" + file_path.suffix.lower()
            new_path = file_path.with_name(new_name)
            counter += 1

        # Skip if name is effectively the same (case-insensitive)
        if file_path.name.lower() == new_path.name.lower():
            print(f"✓ No change: {file_path.name}  ({source})")
            no_change += 1
            continue

        action = " => " if dry_run else " -> "
        file_type = "Photo" if file_path.suffix.lower() in IMAGE_EXTS else "Video"
        print(f"{file_type}: {file_path.name} {action} {new_path.name}  ({source})")

        if not dry_run:
            try:
                file_path.rename(new_path)
                renamed += 1
            except Exception as e:
                print(f"✗ Error renaming {file_path.name}: {e}")
                errors += 1

    print("\n" + "="*60)
    print(f"Summary: Renamed: {renamed} | No change: {no_change} | Errors: {errors}")
    if dry_run:
        print("This was a dry run. Set dry_run = False to apply changes.")

if __name__ == "__main__":
    main()