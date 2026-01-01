import os
import re
from datetime import datetime

# Directory containing the photos (change this to your folder)
directory = "//tank/photo/2023/2023-01-15"  # Current directory, or e.g., r"C:\Photos"

# Supported image extensions (add more if needed)
extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp")

# List of common date/time patterns to try parsing from the filename base
parse_patterns = [
    "%Y%m%d_%H%M%S",      # 20240101_123045
    "%Y-%m-%d %H-%M-%S",  # 2024-01-01 12-00-00
    "%Y.%m.%d %H.%M.%S",  # 2024.01.01 12.00.00
    "%Y-%m-%d_%H%M%S",    # 2024-01-01_120000
    "%Y%m%d_%H%M",        # 20240101_1230 (seconds 00)
    "%Y-%m-%d %H.%M.%S",  # 2024-01-01 12.00.00
    "%Y.%m.%d_%H%M%S",    # 2024.01.01_120000
    "%d %B %Y %I%p",      # 5 January 2023 3pm (limited word support)
    "%Y%m%d",             # 20240101 (time 00h00m00s)
    "%Y-%m-%d",           # 2024-01-01 (time 00h00m00s)
    
]

# Additional regex for specific cases like WhatsApp or prefixed
extra_regex_patterns = [
    (r"IMG[_-]?(\d{8})[_-]WA\d+", r"\1"),  # IMG-20240101-WA0001 -> 20240101
    (r"(\d{8})[_-](\d{6})", r"\1_\2"),     # Direct capture for YYYYMMDD_HHMMSS
]

def extract_date_str(base_name):
    """Try to extract a parseable date string from the base filename."""
    # First, try extra regex to normalize
    for pattern, repl in extra_regex_patterns:
        normalized = re.sub(pattern, repl, base_name, flags=re.IGNORECASE)
        if normalized != base_name:
            return normalized
    
    # Search for potential date strings in the name
    potential_dates = re.findall(r"\d{8}[-_ .\d]*\d{4,6}", base_name)  # Find sequences like 20240101_123045
    for pd in potential_dates:
        cleaned = re.sub(r"[^\d]", "", pd)  # Remove separators
        if len(cleaned) >= 8:
            return cleaned[:8] + ( "_" + cleaned[8:14] if len(cleaned) >= 14 else "")
    
    return base_name  # Fallback: try parsing the whole base

def parse_date_from_filename(filename):
    """Parse date/time from filename, return formatted string or None."""
    base_name = os.path.splitext(filename)[0]
    
    date_str = extract_date_str(base_name)
    
    for pattern in parse_patterns:
        try:
            if pattern == "%d %B %Y %I%p":
                # Limited: try direct match
                dt = datetime.strptime(date_str, pattern)
            else:
                dt = datetime.strptime(date_str[:len(pattern.replace("%", "")) * 2], pattern)  # Rough length match
            return dt.strftime("%Y-%m-%d-%Hh%Mm%Ss")
        except ValueError:
            continue
    
    return None

# Dry run flag (set to False to actually rename)
dry_run = True

os.chdir(directory)
print(f"Processing directory: {os.getcwd()}\n")

for filename in os.listdir("."):
    if not filename.lower().endswith(extensions):
        continue
    
    new_base = parse_date_from_filename(filename)
    if new_base is None:
        print(f"Skipped (no date found): {filename}")
        continue
    
    _, ext = os.path.splitext(filename)
    new_filename = new_base + ext.lower()
    
    if new_filename == filename.lower():
        print(f"No change needed: {filename}")
        continue
    
    # Handle duplicates
    counter = 1
    orig_new = new_filename
    while os.path.exists(new_filename):
        new_filename = f"{new_base}-{counter}{ext.lower()}"
        counter += 1
    
    print(f"{filename} -> {new_filename}")
    
    if not dry_run:
        os.rename(filename, new_filename)

print("\nDone." + (" (dry run)" if dry_run else ""))
# This script renames image files in the specified directory based on date/time information
# extracted from their filenames. It supports various common date/time formats and handles 
# potential duplicates by appending a counter. Set `dry_run` to False to perform actual renaming.
