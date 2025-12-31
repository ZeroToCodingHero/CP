import os
import re
import piexif
from datetime import datetime

# Directory containing your photos
directory = "//tank/photo/2023" # Change to your folder path, e.g., r"C:\Users\YourName\Pictures"

def extract_datetime_from_filename(filename):
    """
    Extract date and time from filename like '2023-03-15-14h49m28.jpg'
    Returns string in EXIF format: 'YYYY:MM:DD HH:MM:SS'
    """
    # Remove extension and get base name
    basename = os.path.splitext(filename)[0]
    
    # Regex to match: YYYY-MM-DD-HHhMMmSS
    pattern = r"(\d{4})-(\d{2})-(\d{2})-(\d{2})h(\d{2})m(\d{2})"
    match = re.match(pattern, basename)
    
    if not match:
        return None
    
    year, month, day, hour, minute, second = match.groups()
    
    try:
        dt = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
        return dt.strftime("%Y:%m:%d %H:%M:%S")
    except ValueError:
        return None

def update_exif_date_taken(file_path):
    """Update EXIF DateTimeOriginal and other date fields from filename."""
    if not file_path.lower().endswith((".jpg", ".jpeg")):
        return False
    
    filename = os.path.basename(file_path)
    new_date_str = extract_datetime_from_filename(filename)
    
    if not new_date_str:
        print(f"Skipping (no valid date/time found): {filename}")
        return False
    
    try:
        # Load existing EXIF data
        exif_dict = piexif.load(file_path)
        
        # Update the three main date fields (encode strings as bytes)
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = new_date_str.encode()
        exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = new_date_str.encode()
        exif_dict["0th"][piexif.ImageIFD.DateTime] = new_date_str.encode()
        
        # Save back to the file
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, file_path)
        
        print(f"Updated: {filename} → {new_date_str}")
        return True
        
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return False

# Batch process all JPEG files in the directory
print("Starting batch update of EXIF 'Date Taken' from filenames...\n")

count = 0
for filename in sorted(os.listdir(directory)):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        if update_exif_date_taken(file_path):
            count += 1

print(f"\nDone! Processed files in: {directory}")
print(f"Total files updated: {count}")

