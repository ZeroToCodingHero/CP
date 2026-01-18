import os
import re
from datetime import datetime
from PIL import Image
import piexif

def batch_rename_and_update_exif(root_dir, update_exif=True, dry_run=False):
    """
    Rename photos to YYYY-MM-DD-HHhMMmSS.jpg based on date in filename
    and optionally update EXIF DateTimeOriginal.

    Parameters:
        root_dir: Directory to process (including subdirectories)
        update_exif: If True, also update EXIF date
        dry_run: If True, only print what would happen (no changes)
    """
    # Regex to capture date and optional time from filename
    # Supports: 20231231, 2023-12-31, 2023_12_31, and time parts like _123456 or -12h34m56
    pattern = re.compile(
        r'(\d{4})[-_]?(\d{2})[-_]?(\d{2})'  # YYYY MM DD (with optional - or _)
        r'[-_]?(\d{2})?h?(\d{2})?m?(\d{2})?s?'  # optional HH h MM m SS s
    )

    renamed_count = 0
    skipped_count = 0

    for subdir, _, files in os.walk(root_dir):
        for filename in files:
            if not filename.lower().endswith(('.jpg', '.jpeg')):
                continue

            filepath = os.path.join(subdir, filename)

            match = pattern.search(filename)
            if not match:
                print(f"Skipped (no date found): {filename}")
                skipped_count += 1
                continue

            year, month, day = match.group(1), match.group(2), match.group(3)
            hour = match.group(4) or '00'
            minute = match.group(5) or '00'
            second = match.group(6) or '00'

            new_name = f"{year}-{month}-{day}-{hour}h{minute}m{second}s.jpg"
            new_filepath = os.path.join(subdir, new_name)

            # Avoid overwriting if file already exists
            counter = 1
            original_new = new_filepath
            while os.path.exists(new_filepath):
                name_part = f"{year}-{month}-{day}-{hour}h{minute}m{second}s_{counter}.jpg"
                new_filepath = os.path.join(subdir, name_part)
                counter += 1

            if dry_run:
                print(f"Would rename: {filename} → {os.path.basename(new_filepath)}")
            else:
                try:
                    os.rename(filepath, new_filepath)
                    print(f"Renamed: {filename} → {os.path.basename(new_filepath)}")
                    
                    # Optional: Update EXIF
                    if update_exif:
                        exif_date = f"{year}:{month}:{day} {hour}:{minute}:{second}"
                        try:
                            exif_dict = piexif.load(new_filepath)
                        except:
                            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

                        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = exif_date.encode()
                        exif_dict["0th"][piexif.ImageIFD.DateTime] = exif_date.encode()

                        exif_bytes = piexif.dump(exif_dict)
                        piexif.insert(exif_bytes, new_filepath)

                    renamed_count += 1
                except Exception as e:
                    print(f"Error processing {filename}: {e}")

    print("\nSummary:")
    print(f"Renamed: {renamed_count} files")
    print(f"Skipped: {skipped_count} files")

# ==================== USAGE ====================
root_directory = "//tank/photo/2023/2023-01-15"  # CHANGE THIS!

# Dry run first (recommended) - see what will happen without changing anything
batch_rename_and_update_exif(root_directory, update_exif=True, dry_run=True)

# When you're happy with the preview, run for real:
# batch_rename_and_update_exif(root_directory, update_exif=True, dry_run=False)