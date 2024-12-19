from sys import argv
from os.path import exists # This import comes back with a bool if the file exists or not

script, from_file, to_file = argv # python ex17.py test.txt newfile.txt

print(f"Copying from {from_file} to (to_file)")

#we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("ready, hit RETURN to continue, CTRL-C to about.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
