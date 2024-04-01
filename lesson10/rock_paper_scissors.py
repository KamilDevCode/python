# #  user input 
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# Rock, paper, scissors wih recursive function:

def rock_paper_scissor():
    player_input = input("Please choose one of the following: \n1: rock, \n2: paper, \n3: scissors: \n\n")
    player = int(player_input)
    
    if player not in [1, 2, 3]:
        sys.exit("Invalid choice. Please choose a number between 1 and 3.")

    computer = random.randint(1, 3)

    if player == computer:
        print("It's a tie! 🤝")
    elif (player == RPS.ROCK.value and computer == RPS.SCISSORS.value):
        print(f"You chose: Rock 🪨 and Python chose: Scissors ✂️")
        print("You win! 🎉 🎉 ")
    elif (player == RPS.PAPER.value and computer == RPS.ROCK.value):
        print(f"You chose: Paper 📄 and Python chose: Rock 🪨")
        print("You win! 🎉 🎉 ")
    elif (player == RPS.SCISSORS.value and computer == RPS.PAPER.value):
        print(f"You chose: Scissors ✂️ and Python chose: Paper 📄")
        print("You win! 🎉 🎉 ")
    else:
        print("Python wins! 🐍")

    play_again_input = input("\nWould you like to play again? \nY for Yes or \nQ to Quit\n\n")
    if play_again_input.lower() == "y":
        rock_paper_scissor()
    else:
        print("\n🎉 🎉 ")
        print("Ok, thanks for playing!")

rock_paper_scissor()
