# guess number game:

import random
import sys

def guess_number(name = "PlayerOne"):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        player_choice = input(f"\n{name}, Guess a number I`m thinking of..1,2 or 3 ")
        print(player_choice)
        if player_choice not in [1,2,3]:
            print("That's not a valid range of numbers," f"{name} enter..1,2 or 3")
            return play_guess_number()

        computer_choice = random.choice('1,2,3')
        print(f"\n{name} you chose {player_choice}.")
        print(f" I was thinking  about...{computer_choice}")

        player_choice = int(player_choice)
        computer_choice = int(computer_choice)


