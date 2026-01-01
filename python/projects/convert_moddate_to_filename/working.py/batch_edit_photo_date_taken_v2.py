import os
import piexif
from datetime import datetime

def update_exif_dates(root_dir, dry_run=True):
    """
    Traverses the given directory and its subdirectories, finds JPEG files with names
    in the format YYYY-MM-DD-HHhMMmSS.jpg (or .jpeg), parses the date/time from the filename,
    and (optionally) updates the EXIF 'DateTime', 'DateTimeOriginal', and 'DateTimeDigitized' tags.
    
    Args:
        root_dir (str): The root directory to search for photos.
        dry_run (bool): If True, only shows what would be done without modifying files.
                        If False, actually updates the EXIF data.
    
    Requires: pip install piexif
    """
    updated_count = 0
    skipped_count = 0

    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg')):
                file_path = os.path.join(subdir, file)
                base_name, ext = os.path.splitext(file)
                parts = base_name.split('-')
                
                if len(parts) != 4:
                    continue  # Skip files that don't match the expected pattern
                
                year_str, month_str, day_str, time_str = parts
                
                # Parse time part: HHhMMmSS
                if 'h' in time_str.lower() and 'm' in time_str.lower():
                    try:
                        # Case-insensitive handling
                        time_str_lower = time_str.lower()
                        hour_part = time_str_lower.split('h')[0]
                        rest = time_str_lower.split('h')[1]
                        minute_part = rest.split('m')[0]
                        second_part = rest.split('m')[1]
                        
                        hour = int(hour_part)
                        minute = int(minute_part)
                        second = int(second_part)
                        year = int(year_str)
                        month = int(month_str)
                        day = int(day_str)
                        
                        # Validate ranges
                        datetime(year, month, day, hour, minute, second)  # Will raise ValueError if invalid
                        
                        dt = datetime(year, month, day, hour, minute, second)
                        exif_date = dt.strftime("%Y:%m:%d %H:%M:%S")
                        
                        if dry_run:
                            print(f"[DRY RUN] Would update: {file_path}")
                            print(f"          → Set EXIF date to: {exif_date}")
                        else:
                            # Load and update EXIF
                            exif_dict = piexif.load(file_path)
                            
                            exif_dict['0th'][piexif.ImageIFD.DateTime] = exif_date
                            exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = exif_date
                            exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = exif_date
                            
                            exif_bytes = piexif.dump(exif_dict)
                            piexif.insert(exif_bytes, file_path)
                            
                            print(f"[UPDATED] {file_path} → {exif_date}")
                        
                        updated_count += 1
                        
                    except ValueError as ve:
                        print(f"[SKIP] Invalid date/time in filename: {file_path} ({ve})")
                        skipped_count += 1
                    except Exception as e:
                        print(f"[ERROR] Failed to process {file_path}: {e}")
                        skipped_count += 1
                else:
                    skipped_count += 1  # Doesn't match HHhMMmSS pattern
    
    # Summary
    print("\n" + "="*50)
    if dry_run:
        print(f"DRY RUN COMPLETE:")
        print(f"   Files that would be updated: {updated_count}")
        print(f"   Files skipped (invalid format): {skipped_count}")
        print("\nNo files were modified. Run with dry_run=False to apply changes.")
    else:
        print(f"UPDATE COMPLETE:")
        print(f"   Files updated: {updated_count}")
        print(f"   Files skipped: {skipped_count}")


# Example usage:
if __name__ == "__main__":
    directory = "D:\\test\\2023\\2023-01-19"  # <-- CHANGE THIS
    
    # First: Test with dry-run (safe)
    print("Running in dry-run mode...")
    update_exif_dates(directory, dry_run=True) # Change to False to actually modify files
    
    # Uncomment the line below when you're ready to actually modify files:
    # print("\nApplying changes for real...")
    # update_exif_dates(directory, dry_run=False)