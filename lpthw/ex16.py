from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("if you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
# Empties the file.cls
locals()
target = open(filename, 'w')  # 'w' opens in write mode vs 'r' read only mode

print("Truncating the file. Goodbye!")
# target.truncate()

print("Now i'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1}\n{line2}\n{line3}\n")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

txt = open(filename)

print(txt.read())

txt.close()
