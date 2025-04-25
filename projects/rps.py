import random

print("What is your name?", end=" ")
name = input().title().strip()

while True:
    user_choice = input(f"Welcome {name}, Enter a choice (rock, paper, scissors): ")
    available_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(available_choices)

    if user_choice == computer_choice:
        print("It was a tie, try again")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Won! Rock beats Scissors")
    elif user_choice == "rock" and computer_choice == "paper":
        print("You Lost! Paper beats Rock")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Won! Paper beats Rock")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("You Lost! Scissors beats Paper")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Won! Scissors beats Paper")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("You Lost! Rock beats Scissors")
    else:
        print("Invaild Choice, Please Choose Again")

    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
        break
