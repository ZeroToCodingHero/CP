from PIL import Image
import os

# Folder with your original images
input_folder = "D:\sort_folders\sort_folders\png"        # CHANGE THIS
output_folder = "D:\sort_folders\converted"     # CHANGE THIS

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported extensions (add more if needed)
extensions = ('.png', '.bmp', '.tiff', '.webp', '.gif', '.ico', '.jpg', '.jpeg', '.jfif', '.heic', '.avif', '.raw', '.cr2', '.nef', '.orf', '.sr2')

for filename in os.listdir(input_folder):
    filepath = os.path.join(input_folder, filename)
    
    # Skip if it's not a file or already JPEG (optional)
    if not os.path.isfile(filepath):
        continue
    if filename.lower().endswith(('.jpg', '.jpeg')):
        print(f"Skipping (already JPEG): {filename}")
        continue
    
    if filename.lower().endswith(extensions):
        try:
            img = Image.open(filepath)
            
            # Convert RGBA (PNG with transparency) to RGB (JPEG doesn't support transparency)
            if img.mode in ("RGBA", "P", "LA"):
                # White background for transparent images
                background = Image.new("RGB", img.size, (255, 255, 255))
                if img.mode == "P":
                    img = img.convert("RGBA")
                background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
                img = background
            else:
                img = img.convert("RGB")
            
            # Save as JPEG
            new_filename = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, new_filename)
            
            img.save(output_path, "JPEG", quality=95)  # 95 = very good quality
            print(f"Converted: {filename} → {new_filename}")
            
        except Exception as e:
            print(f"Error converting {filename}: {e}")

print("Batch conversion complete!")