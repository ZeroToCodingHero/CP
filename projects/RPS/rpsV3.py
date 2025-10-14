from getpass import getpass as input
import tkinter # ? 

print("***Rock🪨 Paper📄 Scissors✂️***")

while True:
    player1 = input("player1, please enter 'R' for Rock 🪨  'P' for Paper 📄 or 'S' Scissors ✂️ > ").upper().strip()
    player2 = input("player2, please enter 'R' for Rock 🪨  'P' for Paper 📄 or 'S' Scissors ✂️ > ").upper().strip()
    if player1 == player2:
        print("It's a tie!")
    elif player1 == 'R' and player2 == 'P':
        print("Player2 wins! 📄  beats 🪨")
    elif player1 == 'P' and player2 == 'S':
        print("player2 wins! ✂️  beats 📄")
    elif player1 == 'S' and player2 == 'R':
        print("player2 wins! 🪨  beats ✂️")
    elif player2 == "R" and player1 == "P":
        print("Player1 wins! 📄  beats 🪨")
    elif player2 == "P" and player1 == "S":
        print("Player1 wins! ✂️  beats 📄")
    elif player2 == "S" and player1 == "R":
        print("Player1 wins! 🪨  beats ✂️")
    else:
        print("Invaild choice!")

    play_again = input("play again? (y/n): ")
    if play_again.lower() != "y":
        print("Goodbye")
        break
