import os
from pathlib import Path
from datetime import datetime
import re

# ==================== CONFIGURATION ====================
# Root directory to start from (will process this folder + all subfolders)
directory = Path("")  # <-- CHANGE THIS to your target folder

# Choose your preferred output format (uncomment one)
# FORMAT = "{year}-{month}-{day}_{hour}-{minute}-{second}{ext}"          # 2023-03-15_14-49-28.jpg
# FORMAT = "{year}{month}{day}_{hour}{minute}{second}{ext}"              # 20230315_144928.jpg
# FORMAT = "IMG_{year}-{month}-{day}_{hour}-{minute}-{second}{ext}"      # IMG_2023-03-15_14-49-28.jpg
# FORMAT = "{year}-{month}-{day} {hour}h{minute}m{second}{ext}"          # 2023-03-15 14h49m28.jpg
FORMAT = "{year}-{month}-{day}-{hour}h{minute}m{second}{ext}"            # 2023-03-15-14h49m28.jpg

# Dry-run mode: True = preview only, False = actually rename
DRY_RUN = False # Change to False to perform actual renaming

# Optional: Add a prefix based on subfolder name (e.g., "Vacation/IMG_...")
# Set to True if you want the immediate subfolder name added as prefix
ADD_SUBFOLDER_PREFIX = False
# ======================================================

def extract_datetime_from_filename(filename: str):
    """Extract datetime from filename like '2023-03-15-14h49m28.jpg'"""
    stem = Path(filename).stem
    pattern = r"^(\d{4})-(\d{2})-(\d{2})-(\d{2})h(\d{2})m(\d{2})$"
    match = re.match(pattern, stem)
    if not match:
        return None
    y, mo, d, h, mi, s = match.groups()
    try:
        return datetime(int(y), int(mo), int(d), int(h), int(mi), int(s))
    except ValueError:
        return None

def generate_new_name(file_path: Path, dt: datetime) -> Path:
    """Generate new filename based on FORMAT and optional subfolder prefix"""
    replacements = {
        "{year}": dt.strftime("%Y"),
        "{month}": dt.strftime("%m"),
        "{day}": dt.strftime("%d"),
        "{hour}": dt.strftime("%H"),
        "{minute}": dt.strftime("%M"),
        "{second}": dt.strftime("%S"),
        "{ext}": file_path.suffix.lower(),
    }

    new_name = FORMAT
    for placeholder, value in replacements.items():
        new_name = new_name.replace(placeholder, value)

    # Optional: Add subfolder name as prefix
    if ADD_SUBFOLDER_PREFIX:
        # Get the immediate parent folder name (one level below root)
        relative_parent = file_path.parent.relative_to(directory)
        if len(relative_parent.parts) >= 1:
            prefix = relative_parent.parts[0] + "_"
            # Avoid double underscore if format already ends with _
            if not new_name.startswith("_"):
                new_name = prefix + new_name
            else:
                new_name = prefix[:-1] + new_name  # in case prefix ends with _

    return file_path.with_name(new_name)

# Main processing
if not directory.exists():
    print(f"Error: Directory not found: {directory}")
    exit(1)

if not directory.is_dir():
    print(f"Error: Path is not a directory: {directory}")
    exit(1)

print(f"Scanning recursively from: {directory}")
print(f"Output format: {FORMAT}")
if ADD_SUBFOLDER_PREFIX:
    print("Adding immediate subfolder name as prefix")
print(f"Dry-run mode: {DRY_RUN}\n")

renamed_count = 0
skipped_count = 0
already_good_count = 0

# Recursively find all JPEG files
jpeg_files = list(directory.rglob("*.jpg")) + list(directory.rglob("*.jpeg"))

print(f"Found {len(jpeg_files)} JPEG files to process...\n")

for file_path in sorted(jpeg_files):
    if not file_path.is_file():
        continue

    dt = extract_datetime_from_filename(file_path.name)
    if dt is None:
        print(f"Skipping (no valid timestamp): {file_path.relative_to(directory)}")
        skipped_count += 1
        continue

    new_path = generate_new_name(file_path, dt)

    # Skip if already correctly named
    if file_path == new_path:
        # Optional: uncomment next line for verbose already-correct feedback
        # print(f"Already good: {file_path.relative_to(directory)}")
        already_good_count += 1
        continue

    # Check for naming conflicts (same filename in same folder)
    if new_path.exists():
        print(f"CONFLICT: '{new_path.name}' already exists in {new_path.parent}")
        print(f"          Skipping: {file_path.relative_to(directory)}")
        skipped_count += 1
        continue

    print(f"Rename: {file_path.relative_to(directory)}")
    print(f"    →   {new_path.relative_to(directory)}")

    if not DRY_RUN:
        try:
            file_path.rename(new_path)
            renamed_count += 1
        except Exception as e:
            print(f"ERROR renaming {file_path.name}: {e}")
            skipped_count += 1
    else:
        renamed_count += 1  # count for summary in dry-run

print("\n" + "="*60)
print("Recursive batch rename complete!")
print(f"Root directory:    {directory}")
print(f"Files renamed:     {renamed_count}")
print(f"Already correct:   {already_good_count}")
print(f"Skipped/Errors:    {skipped_count}")
print(f"Dry-run:           {DRY_RUN}")
if ADD_SUBFOLDER_PREFIX:
    print("Subfolder prefix:  Enabled")
else:
    print("Subfolder prefix:  Disabled")
print("="*60)   

# End of script
"""    # Extract date and time from filename formatted as 'YYYY-MM-DD-HHhMMmSS' """
    # Example filename: '2023-03-15-14h49m28.jpg    
    