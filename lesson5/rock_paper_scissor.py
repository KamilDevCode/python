# #  user input 
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
playagain = True

while playagain:
    

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
        
        
        
    # Generate a random choice for the computer (1 for rock, 2 for paper, 3 for scissors)
    computerchoice = random.randint(1, 3)

    # Print the computer's choice
    print("Computer chose:", computerchoice)

    # Compare the player's choice and the computer's choice to determine the winner
    if player == computerchoice:
        print("It's a tie! 🤝")
    elif (player == 1 and computerchoice == 3) or \
        (player == 2 and computerchoice == 1) or \
        (player == 3 and computerchoice == 2):
        print("You win! 🎉 🎉 ")
    else:
        print("Python wins!" "🐍" )

    playagain = input("\nWould you like to play again? \nY for Yes or \n Q to Quit \n\n")

    if playagain.lower() =="y":
        continue
    else:
        print("\n🎉 🎉 ")
        print("Ok, thanks for playing!")
        playagain = False
        
