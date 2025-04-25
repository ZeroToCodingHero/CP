from sys import argv
from pathlib import Path
import os
import pandas as pd

script = argv
prompt = '> '
directory_path = 'Z:/#-q Movies'
directory_list =  os.listdir('Z:/#-q Movies')
python_files = 'D:/Coding/movielist'
number_of_folders = len(directory_list)

# writing to a txt file 
file_path = os.path.join(python_files, 'movielist.txt')
with open(file_path, 'w') as file:
    items = os.listdir(directory_path)
    for item in items:
        file.write(item + '\n')

# # writing to a csv file
# df1 = pd.read_csv("movielist.txt")
# df1.to_csv('movielist.csv', 
#                   index = None)

print()
print("\tWelcome to my Plex library,",end=' ')
print(f"You have {number_of_folders} movies to choice from." )
print()
print("\tHere are the available movies")

# viewing whats folders are in the directory
def list_of_folders(path):
    for folder in Path(path).iterdir():
        print(f"Movie List: {folder}")

list_of_folders(directory_path)

print()
print("\tHere are the folders with missing files")

# viewing which directories has no files, still need to update match missing video files
def list_empty_folders(path):
    for folder in Path(path).iterdir():
        if folder.is_dir() and not list(folder.iterdir()):
            print(f"Empty folder: {folder}")

list_empty_folders(directory_path)
print()
