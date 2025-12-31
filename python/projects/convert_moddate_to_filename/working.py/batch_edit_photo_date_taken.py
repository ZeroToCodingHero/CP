from exif import Image
import os

# Directory containing your images
input_dir = "//tank/photo/2002"  # Replace with your directory
output_dir = "//tank/photo/2002" # Directory to save modified images
os.makedirs(output_dir, exist_ok=True)

# New date in EXIF format: 'YYYY:MM:DD HH:MM:SS'
new_date = '2002:01:01 12:00:00'

# Process each JPEG file
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        with open(input_path, 'rb') as img_file:
            img = Image(img_file)
        
        if img.has_exif:
            # Update the date taken field
            img.datetime_original = new_date
            # Optionally update related fields
            img.datetime = new_date
            img.datetime_digitized = new_date
        
        # Save the modified image
        with open(output_path, 'wb') as out_file:
            out_file.write(img.get_file())
        
        print(f"Updated {filename}")
        
# Note: Ensure you have the 'exif' library installed. You can install it via pip:
# pip install exif  
# Also, make sure to back up your images before running this script, as it modifies EXIF data.
