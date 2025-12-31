import subprocess
import glob

file_paths = glob.glob("//tank/photo/2007" + "/*.JPG")

# Build command: exiftool -overwrite_original -TAG=value file1 file2 ...
cmd = ["exiftool", "-overwrite_original"]

# Add common tags
cmd += [
    "-XMP:Description=Batch corrected on 2025-12-31",
    "-EXIF:Artist=Your Name",
    "-XMP:Subject=new year,celebration,2025",
]

cmd += file_paths  # Append all files at the end

subprocess.run(cmd, check=True)
print("Batch processing complete!")
# This script uses exiftool to batch update EXIF metadata for all JPEG files in the 'photos' directory.