import os

# List of MP4 files to join
files = ["python\projects\ffmpeg\video_files\A Man Called Intrepid (1979) - pt1.mp4", "python\projects\ffmpeg\video_files\A Man Called Intrepid (1979) - pt2.mp44"]

# Create a text file with file paths
with open("file_list.txt", "w") as f:
    for file in files:
        f.write(f"file '{file}'\n")

# Run ffmpeg command to concatenate
os.system("ffmpeg -f concat -safe 0 -i file_list.txt -c copy output.mp4")

# Clean up the temporary file
os.remove("file_list.txt")
