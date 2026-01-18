import os
import re
import piexif
from datetime import datetime

# Directory containing the photos (change this to your folder path)
directory = ""  # Current directory, or specify like r"C:\path\to\photos"

# Common filename patterns that contain dates (e.g., "2025-12-31.jpg", "IMG_20251231_123456.jpg", "Photo20251231.jpg")
# Add or modify patterns as needed for your files
date_patterns = [
    r"(\d{4})-(\d{2})-(\d{2})-(\d{2}h)(\d{2}m)(\d{2})",  # YYYY-MM-DD-HHhMMmSS
    r"(\d{4}-\d{2}-\d{2})",                  # YYYY-MM-DD
    r"(\d{8})",                              # YYYYMMDD (will assume 00:00:00)
    r"(\d{4}\d{2}\d{2})",                     # YYYYMMDD no separators
    r"(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})",  # YYYY-MM-DD_HH-MM-SS
    r"IMG[_-]?(\d{8})[_-]?\d*",              # IMG_YYYYMMDD or similar (WhatsApp style)
    r"PXL[_-]?(\d{8})[_-]?\d*",              # Google Pixel style
    r"Photo[_-]?(\d{8})[_-]?\d*",            # PhotoYYYYMMDD style
    r"(\d{4}-\d{2}-\d{2}-\d{2}h\d{2}m\d{2}s)"  # YYYY-MM-DD-HHhMMmSS

]

def extract_date_from_filename(filename):
    """Extract date (and time if available) from filename using regex patterns."""
    name = os.path.splitext(filename)[0]  # Remove extension
    for pattern in date_patterns:
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

def update_exif_date_taken(file_path):
    """Update the EXIF DateTimeOriginal, DateTimeDigitized, and DateTime with date from filename."""
    if not file_path.lower().endswith((".jpg", ".jpeg")):
        return

    new_date_str = extract_date_from_filename(os.path.basename(file_path))
    if not new_date_str:
        print(f"No date found in filename: {file_path}")
        return

    try:
        exif_dict = piexif.load(file_path)

        # Update the three main date tags
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = new_date_str
        exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = new_date_str
        exif_dict["0th"][piexif.ImageIFD.DateTime] = new_date_str

        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, file_path)
        print(f"Updated EXIF date for: {file_path} -> {new_date_str}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Batch process all JPEG files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        update_exif_date_taken(file_path)

print("Batch update complete!")