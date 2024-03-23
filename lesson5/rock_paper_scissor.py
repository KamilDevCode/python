# #  user input 
import sys
import random

# Ask the player to choose rock, paper, or scissors
player = input("Please choose one of the following: \n1: rock, \n2: paper, \n3: scissors: \n\n")

# Convert the player's choice to an integer
player = int(player)

# Check the player's choice and print it
if player == 1:
    print("You chose rock")
elif player == 2:
    print("You chose paper")
elif player == 3:
    print("You chose scissors")
else:
    # Exit the program if the player's choice is invalid
    sys.exit("Invalid choice. Please choose a number between 1 and 3.")

