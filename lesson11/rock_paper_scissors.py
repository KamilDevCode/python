import random
import sys

choices = ['rock 🪨', 'paper 📄', 'scissors ✂️']


def play_rock_paper_scissors(game_count = 0):
    
    def get_player_choice():
        
            player_input = input("Please choose one of the following:\n1: rock,\n2: paper,\n3: scissors:\n\n")
            player = int(player_input)
            if player not in range(1,4):
                print("Invalid choice. Please choose a number between 1 and 3.")
                return get_player_choice()
            return player
    
    def check_winner(player, computer):
        computer = random.choice(choices)
        if player == choices.index(computer) + 1:
            print("It's a tie! 🤝")
        else:
            print(f"You chose: {choices[player-1]} and Python chose: {computer} and you {['lost', 'won', 'tied'][player == computer or player != choices.index(computer) or player - choices.index(computer) or choices.index(computer) - player]} to Python 🐍")
            
        return player == choices.index(computer) + 1
    
    player = get_player_choice()
    if check_winner(player, random.choice(choices)):
        game_count += 1
        print("Game count:", game_count)
    
    play_again_input = input("\nWould you like to play again?\nY for Yes or Q to Quit\n\n")
    if play_again_input.lower() == "y":
        play_rock_paper_scissors(game_count)
    else:
        print("\n🎉 🎉")
        print("Ok, thanks for playing!")
        sys.exit("Bye! 👋")
play_rock_paper_scissors()
