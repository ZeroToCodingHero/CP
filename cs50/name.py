import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# or
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])

# or
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# https://docs.python.org/3/library/sys.html
# pypi.org pypi.org/project/cowsay
