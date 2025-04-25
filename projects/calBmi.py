# def = function = A block of reusable code
                 # place () after the function name to invoke it
user_name = input("What is your name? ")
user_age = input("What is your age? ")
user_weight = float(input("What is your weight in lbs? "))
user_height = float(input("What is your height in inches? "))

           # parameters
def calBmi (name, age, weight):
    print(f"hello, {name}!")
    print(f"You are {age} years old!")
    print(f"Your weight is {weight}!")

      # arguments
calBmi(user_name, user_age, user_weight)

bmi = user_weight / (user_height**2) * 703
print(f"your bmi is {bmi}")
