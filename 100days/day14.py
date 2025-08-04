from getpass import getpass as input # hide user input

print("*** Rock🪨, Paper📄, Scissors✂️***")
player1 = input("player1, please enter 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ")
player2 = input("player2, please enter 'R' for Rock, 'P' for Paper, or 'S' for Scissors: ")

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
else:
    print("Invalid input!")
    exit() # exit the program if the input is invalid
