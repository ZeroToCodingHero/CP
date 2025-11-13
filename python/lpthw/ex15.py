# Import argv from the sys module
from sys import argv

# Get argv command line arguments (when running the file) & assigning to 2 VAR
script, filename = argv

# Open the file (ex15_sample.txt) & assign to a VAR
txt = open(filename)

# Print out the filename & print out the content of the opened file using, read()
print(f"Here's your file {filename}:")
print(txt.read())

# Close txt file
txt.close()

# Print out instructions & ask for user input()
print("Type the filename again:")
file_again = input("> ")  # ex15_sample.txt

# Open the file (ex15_sample.txt) & assign to a VAR
txt_again = open(file_again)

# Print out the filename & print out the content of the opened file using, read()
print(txt_again.read())

# Close file
txt_again.close()
