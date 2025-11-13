# define a function cheese_and_crackers with 2 parameters
# inside of the function: use aruments with print staements
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# call our function with numbers as aruments
print("We can just give the function numbers direclty:")
cheese_and_crackers(20, 30) 

#define two variables and assign the numbers
print("OR, we can uase variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# call out function with vaiables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# call out function and pass calculation as argument
print("We we even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# call out function and pass calculation (with variableas and numbers)
print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def add_two_number(number1, number2):
    print(f"{number1} + {number2} equals {number1 + number2}.")

add_two_number(1, 9)
add_two_number(2, 3)
add_two_number(1 + 2, 3 + 7)
add_two_number(5 - 2, 7 - 2)
add_two_number(2 + 3, 7 - 2)

number1 = 3
number2 = 8

add_two_number(number1, number2)
add_two_number(number1 + number2, number2 - number1)
add_two_number(number1 + 5, number2 + 2)
add_two_number(number1 - 1, number2 - 3)
add_two_number(number1 + number1 + number2, 31 + 2)
