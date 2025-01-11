from sys import exit 

def red_room():
    print(f"You are now trapped in a room with a zombie.")
    print("Do you want to fight the zombie 'y'")
    print("Do you want to run 'n'")
          
    choice = input("> ")

    if "y" in choice:
        print("You Winner")
    elif "n" in choice:
        print("You Lose")
    else:
        exit("Invaild Choice")

def blue_room():
    print(f"You are now trapped in a room with a bear.")
    print("Do you want to fight the bear 'y'")
    print("Do you want to run 'n'")
    
    choice = input("> ")

    if "y" in choice:
        print("You Winner")
    elif "n" in choice:
        print("You Lose")
    else:
        exit("Invaild Choice")

def green_room():
    print(f"You are now trapped in a room with The Muffin Man.")
    print("Do you want to fight the The Muffin Man 'y'")
    print("Do you want to run 'n'")
    
    choice = input("> ")

    if "y" in choice:
        print("You Winner")
    elif "n" in choice:
        print("You Lose")
    else:
        exit("Invaild Choice")
 
def start():
    print("Welcome to Ecsape Room! What's your name ?", end= ' ')
    name = (input()).title().strip()
    print(f"Welcome {name} now let's get started")

    print("You have a choice of three doors.")
    print("The Red, Blue or Green door! all have a different adventure")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "red":
        red_room()
    elif choice == "blue":
        blue_room()
    elif choice == "green":
        green_room()
    else:
        exit("Invaild Choice")


start() 


# def play_again():
#     play_again = input("play again? (y/n): ")
#     if play_again.lower() != "y":
#         exit