# continue starts the while loop again
# break stops the while loop
# exit stops the program
# pass does nothing
# return returns a value from a function
# yield returns a value from a function and pauses the function

from getpass import getpass as input # hide user input
from emoji import emojize

counter = 1
while True: 
        print("*** Rock🪨, Paper📄, Scissors✂️***") 
        player1 = input("player1, please enter 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ").lower().replace(" ", "")
        player2 = input("player2, please enter 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ").lower().replace(" ", "")

        if player1 == player2:
                print("It's a tie!")
        elif player1 == "R" and player2 == "P":
                print("Player2 wins! 📄 beats 🪨")
        elif player1 == "P" and player2 == "S":
                print("Player2 wins! ✂️ beats 📄")
        elif player1 == "S" and player2 == "R":
                print("Player2 wins! 🪨 beats ✂️")
        elif player2 == "R" and player1 == "P":
                print("Player1 wins! 📄 beats 🪨")
        elif player2 == "P" and player1 == "S":
                print("Player1 wins! ✂️ beats 📄")
        elif player2 == "S" and player1 == "R":
                print("Player1 wins! 🪨 beats ✂️")
                counter += 1
                
                continue
        else:
                print("Invalid input!")
                continue
        exit() # exit the program if the input is invalid
