from sys import argv
from pathlib import Path
import os

script = argv
prompt = '> '
directory_path = 'Z:\movies' # which directory to search
directory_list =  os.listdir('Z:\movies')
python_files = 'D:/01-eo/Coding/python/CP/projects/movielist' # where to save your file
number_of_folders = len(directory_list) 

# writing to a txt file 
file_path = os.path.join(python_files, 'movielist.txt')
with open(file_path, 'w') as file:
    items = os.listdir(directory_path)
    for item in items:
        file.write(item + '\n')

print()
print("\tWelcome to my JellyFin library,",end=' ')
print(f"You have {number_of_folders} movies to choice from." )
print()
print("\tHere are the available movies")

# viewing what folders are in the directory
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