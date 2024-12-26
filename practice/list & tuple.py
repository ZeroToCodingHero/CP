# list  use [ ]
# Lists are used to store multiple items in a single variable
# List is a collection which is ordered and changeable. Allows duplicate members.

# tuple use ( )
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

this_list = ["apple", "banana", "cherry"]
print(this_list[1])
# To determine how many items a list has
print(len(this_list))

# To change the value 
this_list[1] = "blackcurrant"
print(this_list)

# The insert() method inserts an item at the specified index
this_list.insert(2, "watermelon")
print(this_list)

# To append elements from another list to the current list
tropical = ["mango", "pineapple", "papaya"]
this_list.extend(tropical)
print(this_list)

