
import random
def guess_number(name="Player"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_guess_number():
        nonlocal game_count
        nonlocal player_wins
        nonlocal name
        nonlocal computer_wins
        player_choice = input(f"\n{name}, Guess a number I'm thinking of..1,2 or 3 ")
        player_choice = int(player_choice)
        if player_choice not in [1, 2, 3]:
            print(f"That's not a valid range of numbers, {name}. Enter 1, 2 or 3.")
            return play_guess_number()

        computer_choice = str(random.randint(1, 3))
        print(f"\n{name}, you chose {player_choice}.")
        print(f"I was thinking about...{computer_choice}")

        computer_choice = int(computer_choice)

        def check_winner(player_choice, computer_choice):
            nonlocal player_wins
            nonlocal computer_wins
            if player_choice == computer_choice:
                print("It's a tie!")
            # elif player_choice == 1 and computer_choice == 3 \
            #         or player_choice == 2 and computer_choice == 1 \
            #         or player_choice == 3 and computer_choice == 2:
            #     print(f"Congratulations {name}, you win!")
                player_wins += 1
            else:
                print("Computer wins! ")
                computer_wins += 1

        check_winner(player_choice, computer_choice)

        game_count += 1
        print(f"{game_count} games played")
        print(f"{name} wins: {player_wins}, Computer wins: {computer_wins}")

    play_guess_number()
guess_number()
