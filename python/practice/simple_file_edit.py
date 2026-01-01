import os
import re
from datetime import datetime

# Optional: Pillow library for reading EXIF metadata from images
# If not installed, EXIF parsing will be skipped (install with: pip install pillow)
try:
    from PIL import Image
except ImportError:
    Image = None
    print("PIL not found. EXIF parsing skipped. Install with 'pip install pillow' for best results.")

def get_timestamp(file_path):
    """
    Attempts to extract the original photo/video timestamp.
    Priority:
        1. EXIF metadata (most accurate, when available)
        2. Date patterns in the filename
    Returns a datetime object if successful, otherwise None (file will be skipped)
    """
    filename = os.path.basename(file_path).lower()  # Get just the filename, lowercase for easier matching

    # ==================== 1. EXIF METADATA PARSING ====================
    if Image:  # Only attempt if Pillow is available
        try:
            with Image.open(file_path) as img:  # Open image without loading full data into memory
                exif = img.getexif()  # Get EXIF data dictionary
                if exif:
                    # Common EXIF tags for date:
                    # 36867 = DateTimeOriginal (preferred)
                    # 36868 = DateTimeDigitized
                    # 306   = DateTime (fallback, when file was modified in camera)
                    date_str = exif.get(36867) or exif.get(36868) or exif.get(306)
                    if date_str:
                        # Clean string: remove timezone info (+00:00 or Z), trim whitespace
                        date_str = date_str.split('+')[0].split('Z')[0].strip()
                        # EXIF uses colons in date: '2025:12:31 23:59:59' → replace first two with spaces
                        date_str = date_str.replace(':', ' ', 2)
                        return datetime.strptime(date_str, '%Y %m %d %H %M %S')
        except Exception:
            # Many file types (e.g. PNG, some videos) don't have EXIF or cause errors → silently ignore
            pass

    # ==================== 2. FILENAME PATTERN PARSING ====================
    # Remove common prefixes that don't contain date info (e.g., "IMG_", "Screenshot_")
    clean_name = re.sub(r'^(img|vid|photo|picture|pxl|screenshot|snapchat|fb.?img)[- _]*', '', filename)
    # Remove common suffixes like WhatsApp's "-WA0001"
    clean_name = re.sub(r'[- _](wa|burst)\d*$', '', clean_name)

    # Pattern 1: Most common phone format → YYYYMMDD[HHMMSS]
    # Examples: IMG_20251231_235959.jpg, 20251231.jpg
    match = re.search(r'(\d{8})(\d{6})?', clean_name)
    if match:
        date_part = match.group(1)           # YYYYMMDD
        time_part = match.group(2) or '000000'  # HHMMSS or default midnight
        try:
            return datetime.strptime(date_part + time_part, '%Y%m%d%H%M%S')
        except ValueError:
            pass  # Invalid date → continue to next pattern

    # Pattern 2: Explicit date with separators → YYYY-MM-DD [HH-MM-SS]
    # Handles -, _, ., space as separators
    match = re.search(r'(\d{4})[-_\. ]?(\d{2})[-_\. ]?(\d{2})[-_\. ]?(\d{2})?[-_\. ]?(\d{2})?[-_\. ]?(\d{2})?', clean_name)
    if match:
        y, m, d = match.group(1), match.group(2), match.group(3)
        h = match.group(4) or '00'   # Default to 00 if time missing
        mi = match.group(5) or '00'
        s = match.group(6) or '00'
        try:
            return datetime(int(y), int(m), int(d), int(h), int(mi), int(s))
        except ValueError:
            pass

    # Pattern 3: 13-digit Unix timestamp in milliseconds
    # Common in Snapchat, Facebook downloads, etc.
    match = re.search(r'(\d{13})', filename)
    if match:
        try:
            timestamp_ms = int(match.group(1))
            return datetime.fromtimestamp(timestamp_ms / 1000.0)
        except (ValueError, OSError):
            pass

    # Pattern 4: Ambiguous US/EU formats → MMDDYYYY or DDMMYYYY with optional time
    match = re.search(r'(\d{2})(\d{2})(\d{4})(\d{6})?', clean_name)
    if match:
        a, b, y = int(match.group(1)), int(match.group(2)), int(match.group(3))
        time_part = match.group(4) or '000000'
        h, mi, s = int(time_part[:2]), int(time_part[2:4]), int(time_part[4:])
        # Try MM/DD/YYYY first
        try:
            return datetime(y, a, b, h, mi, s)
        except ValueError:
            pass
        # Then try DD/MM/YYYY
        try:
            return datetime(y, b, a, h, mi, s)
        except ValueError:
            pass

    # If no pattern matched → return None (file will not be renamed)
    return None

def process_directory(root_dir, dry_run):
    """
    Recursively walks through all subdirectories and renames supported media files.
    Preserves original folder structure.
    """
    # List of supported image and video extensions (case-insensitive)
    extensions = (
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif',
        '.heic', '.heif', '.webp', '.avif',
        '.mp4', '.mov', '.avi', '.mkv', '.webm', '.3gp', '.3g2', '.m4v'
    )

    renamed_count = 0
    skipped_count = 0

    # os.walk recursively traverses all subdirectories
    for current_dir, _, files in os.walk(root_dir):
        for file in sorted(files):  # Sort for consistent processing order
            # Skip Apple edit sidecar files (they belong to a photo and shouldn't be renamed alone)
            if file.lower().endswith('.aae'):
                rel_path = os.path.relpath(os.path.join(current_dir, file), root_dir)
                print(f"Skipped sidecar: {rel_path}")
                skipped_count += 1
                continue

            # Check if file has a supported extension
            if file.lower().endswith(extensions):
                full_path = os.path.join(current_dir, file)
                rel_path = os.path.relpath(full_path, root_dir)  # Show path relative to root

                # Extract timestamp
                ts = get_timestamp(full_path)
                if ts is None:
                    print(f"Not changed (no date found): {rel_path}")
                    skipped_count += 1
                    continue

                # Build new filename: YYYY-MM-DD-HH-MM-SS + original extension
                ext = os.path.splitext(file)[1].lower()
                new_name = ts.strftime('%Y-%m-%d-%H-%M-%S') + ext
                new_path = os.path.join(current_dir, new_name)

                # Handle filename conflicts in the same folder (add _1, _2, etc.)
                counter = 1
                base = ts.strftime('%Y-%m-%d-%H-%M-%S')
                while os.path.exists(new_path):
                    new_name = f"{base}_{counter}{ext}"
                    new_path = os.path.join(current_dir, new_name)
                    counter += 1

                # Show what would happen (dry run) or actually rename
                new_rel_path = os.path.relpath(new_path, root_dir)
                if dry_run:
                    print(f"[DRY] {rel_path} → {new_rel_path}")
                else:
                    try:
                        os.rename(full_path, new_path)
                        print(f"Renamed: {rel_path} → {new_rel_path}")
                        renamed_count += 1
                    except Exception as e:
                        print(f"Error renaming {rel_path}: {e}")

    return renamed_count, skipped_count

def main():
    # Get root directory from user
    dir_path = input("Enter the root directory path (will process all subfolders): ").strip().strip('"\'')
    if not os.path.isdir(dir_path):
        print("Invalid directory. Exiting.")
        return

    # Ask for dry run mode
    dry_run_input = input("Dry run? (y/n): ").strip().lower()
    dry_run = dry_run_input == 'y'

    # Inform user about mode
    if dry_run:
        print("\n--- DRY RUN MODE (no files will be renamed) ---\n")
    else:
        print("\n--- LIVE MODE (files will be renamed) ---\n")

    # Process all files and get summary counts
    renamed, skipped = process_directory(dir_path, dry_run)

    # Final summary
    print(f"\nDone! {renamed} files renamed, {skipped} not changed or skipped.")

if __name__ == "__main__":
    main()
    