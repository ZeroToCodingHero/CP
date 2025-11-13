"""

"""
# for loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])

# A short hand for loop that will print all items in a list
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# newlist = [expression for item in iterable if condition == True]
newlist = [x for x in thislist if "a" in x]
print(newlist)
