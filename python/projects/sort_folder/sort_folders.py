import os
import shutil

# Define the source directory and destination directory
source_directory = '//Desktop-ats16j4/06-photos\photo frame'  # Replace with your source path
destination_directory = 'D:/01-eo\Coding\CP-1\python\projects'  # Replace with your destination path

# Ensure the destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# Walk through the source directory and its subdirectories
for root, dirs, files in os.walk(source_directory):
    for file in files:
        file_path = os.path.join(root, file)
        # Extract the file extension
        _, ext = os.path.splitext(file)
        ext = ext[1:].lower()  # Remove the dot and convert to lowercase

        # Skip if there is no extension (e.g., directories)
        if not ext:
            continue

        # Define the destination folder for this extension
        ext_folder = os.path.join(destination_directory, ext)
        os.makedirs(ext_folder, exist_ok=True)

        # Move the file to the extension-specific folder
        shutil.move(file_path, os.path.join(ext_folder, file))

print("Files have been sorted into folders by extension.")   