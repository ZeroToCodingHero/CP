# import argv from sys module
from sys import argv

# assign commandline arguments to variables
script, input_file = argv

# define a print all funtion which prints the content of the file
def print_all(f):
    print(f.read())

# rewind our file to the original position
def rewind(f):
    f.seek(0)

# print out a line number, followed by a line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open a file and assign it to a bariable
current_file = open(input_file)

print("First let's print the whole file:\n")

# print out the content of file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# rewind the file to the first position
rewind(current_file)

print("Let's print three lines:")

# set current line, prints each line of the file with the line number
current_line = 1
print_a_line(current_line, current_file)

# increase the current line number by 1
# set current line, prints each line of the file with the line number
current_line = current_line + 1
print_a_line(current_line, current_file)

# increase the current line number by 1
# set current line, prints each line of the file with the line number
current_line += 1 # short hand
print_a_line(current_line, current_file)
