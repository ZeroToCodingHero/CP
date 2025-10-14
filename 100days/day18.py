num = 69
counter = 0

while True:
    user_input = int(input("Guess a number between 1 & 100? "))
    if user_input == 69:
        print("Winner")
        counter += 1
        print(f"Winner, with {counter} of attempts")
        break
    if user_input >= 1 and user_input < 69:
        print("Too low")
        counter +=1
    elif user_input > 69 and user_input <= 100:
        print("Too high")
        counter +=1
    else:
        print("You broke the progam")
        exit()

    

