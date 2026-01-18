import os
import piexif
from PIL import Image
from datetime import datetime

def update_datetime_original(image_path, new_datetime_str):
    # Load EXIF data
    exif_dict = piexif.load(image_path)
    # Update DateTimeOriginal
    exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_datetime_str
    # Update DateTimeDigitized
    exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_datetime_str
    # Update DateTime in the 0th IFD
    exif_dict['0th'][piexif.ImageIFD.DateTime] = new_datetime_str
    # Save the updated EXIF data back to the image
    exif_bytes = piexif.dump(exif_dict)
    image = Image.open(image_path)
    image.save(image_path, exif=exif_bytes)

# Specify the folder containing images and the new date/time
folder_path = "//tank/photo/1994" # Path to the folder with images
new_time = "1994-00-00-00h-00m-00s"  # Format: YYYY:MM:DD HH:MM:SS

# Loop through all JPEG files in the folder and update their EXIF data
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg')):
        image_path = os.path.join(folder_path, filename)
        update_datetime_original(image_path, new_time)
        print(f"Updated: {filename}")
print("All images updated.")



  