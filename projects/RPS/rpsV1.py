from getpass import getpass as input  # hide user input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print("Select your move (R, P, or S)")
print()

player1_score = 0
player2_score = 0
available_choices = ["R", "P", "S"]

while True:
    # Get and validate Player 1's move
    player1Move = input("Player 1 > ").upper().strip()
    if player1Move not in available_choices:
        print("Invalid input for Player 1! Choose R, P, or S.")
        continue

    # Get and validate Player 2's move
    player2Move = input("Player 2 > ").upper().strip()
    if player2Move not in available_choices:
        print("Invalid input for Player 2! Choose R, P, or S.")
        continue

    print()

    # Check for a tie
    if player1Move == player2Move:
        print("It's a tie!")

    # Check win conditions for Player 1
    elif (player1Move == "R" and player2Move == "S") or \
         (player1Move == "P" and player2Move == "R") or \
         (player1Move == "S" and player2Move == "P"):
        print(f"Player 1 wins! {player1Move} beats {player2Move}")
        player1_score += 1

    # Check win conditions for Player 2
    else:
        print(f"Player 2 wins! {player2Move} beats {player1Move}")
        player2_score += 1

    # Display scores
    print(f"Player 1 has {player1_score} wins.")
    print(f"Player 2 has {player2_score} wins.")
    print()

    # Check for game end
    if player1_score == 3:
        print("Player 1 is the champion! Thanks for playing!")
        break
    elif player2_score == 3:
        print("Player 2 is the champion! Thanks for playing!")
        break