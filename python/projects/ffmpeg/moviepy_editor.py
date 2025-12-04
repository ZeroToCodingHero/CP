from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load the video files
clip1 = VideoFileClip("D:/01-eo/Coding/CP-1/python/projects/ffmpeg/video_files\A Man Called Intrepid (1979) - pt1.mp4")
clip2 = VideoFileClip("D:/01-eo/Coding/CP-1/python/projects/ffmpeg/video_files\A Man Called Intrepid (1979) - pt2.mp4")
clip3 = VideoFileClip("D:/01-eo/Coding/CP-1/python/projects/ffmpeg/video_files\A Man Called Intrepid (1979) - pt3.mp4")  
clip4 = VideoFileClip("D:/01-eo/Coding/CP-1/python/projects/ffmpeg/video_files\A Man Called Intrepid (1979) - pt4.mp4") 
clip5 = VideoFileClip("D:/01-eo/Coding/CP-1/python/projects/ffmpeg/video_files\A Man Called Intrepid (1979) - pt5.mp4")
clip6 = VideoFileClip("D:/01-eo/Coding/CP-1/python/projects/ffmpeg/video_files\A Man Called Intrepid (1979) - pt6.mp4")

# Concatenate the clips
final_clip = concatenate_videoclips([clip1, clip2, clip3, clip4, clip5, clip6], method="compose")

# Write the output to a new file
final_clip.write_videofile("output.mp4", fps=24, remove_temp=True)
# Close the clips to release resources
clip1.close()
clip2.close()
final_clip.close()  
