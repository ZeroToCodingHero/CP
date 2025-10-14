input1 = input("first word ? ").lower()
input2 = input("second word ? ").lower()

input_list = [input1, input2]
input_list.sort()

if input1 == input2:
    print("You gave the same word twice.")
else:
    print(f"{input_list[-1]} come alphabetically last.")

user_input1 = input("1st letter")
user_input2 = input("2nd letter")
user_input3 = input("3rd letter")

list = [user_input1, user_input2, user_input3]
list.sort()

print(list)