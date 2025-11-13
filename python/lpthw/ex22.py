# ex01 A Good First Program
print("Hello World!")

# ex02 Comments and Pound Characters
# a comment

# ex03 Numbers and Math
( "+, -, /, *, %, <, >, <=, >= ")

# ex04 Variables and Names
cars = 100

# ex05 More Variables and Printing
my_name = 'Zed A. Shaw'
print(f"Let's talk about {my_name}.")

# ex06 Strings and Text
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

# ex07 More Printing
end1 = "C"
end2 = "h"
end3 = "e"
print(end1 + end2 + end3, end= ' ')

# ex08 Printing, Printing
formatter = "{} {} {} {}" 
print(formatter.format(1, 2, 3, 4))
print(formatter.format(True, False, False, False))

# ex09 Printing, Printing, Printing
months = "\nJan\nFeb\nMar"
print("""
There's something going on here.
""")

# ex10 What Was That?
tabby_cat = "\tI'm tabbed in."
backslash_cat = 'I\'m \\ a \\ cat.'

# ex11 Asking Questions
print("How old are you", end=' ')
age = (input())

# ex12 Prompting People
age = input("How old are you? ")
print(f"So you're {age} old")

# ex13 Parameters, Unpacking, Variables
from sys import argv
script, frist, second, third = argv

# ex14 Prompting and Passing
prompt = '> '
likes = input(prompt)

# ex15 Reading Files
txt = open(filename)
print(txt.read())

# ex16 Reading and Writing Files
target = open(filename, 'w')
target.truncate()
target.write(f"{line1}\n{line2}\n{line3}\n")
target.close()

# ex17 More Files
from os.path import exists
print(f"Does the output file exist? {exists(to_file)}")

# ex18 Names, Variables, Code, Functions
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
print_two("Zed","Shaw")

# ex19 Functions and Variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# ex20 Functions and Files
def print_a_line(line_count, f):
    print(line_count, f.readline())
current_line += 1

# ex21 Functions Can Return Something
def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b
age = add(30, 5)
