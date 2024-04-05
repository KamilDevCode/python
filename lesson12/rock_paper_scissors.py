import random
import sys

choices = ['rock 🪨', 'paper 📄', 'scissors ✂️']

def rps():
    game_count = 0
    player_wins = 0
    computer_wins = 0
    
    def play_rock_paper_scissors():
        nonlocal game_count
       
        def get_player_choice():
            
            player_input = input("Please choose one of the following:\n1: rock,\n2: paper,\n3: scissors:\n\n")
            player = int(player_input)
            if player not in range(1, 4):
                print("Invalid choice. Please choose a number between 1 and 3.")
                return get_player_choice()
            return player
        
        def check_winner(player, computer):
            nonlocal player_wins
            nonlocal computer_wins
            nonlocal game_count
            computer = random.choice(choices)
            
            if player == choices.index(computer) + 1:
                print("It's a tie! 🤝")
            else:
                if (player == 1 and choices.index(computer) == 2) or (player == 2 and choices.index(computer) == 0) or (player == 3 and choices.index(computer) == 1):
                    player_wins += 1
                    game_count += 1
                    print("You won this round! 🎉")
                else:
                    computer_wins += 1
                    game_count += 1
                    print("Python won this round! 🐍")
                    print(f"You chose: {choices[player-1]} and Python chose: {computer}. Player wins: {player_wins}, Computer wins: {computer_wins}, Game count: {game_count}")
                
            return player == choices.index(computer) + 1
        
        player = get_player_choice()
        check_winner(player, random.choice(choices))
        
        play_again_input = input("\nWould you like to play again?\nY for Yes or Q to Quit\n\n")
        if play_again_input.lower() == "y":
            play_rock_paper_scissors()
        else:
            print("\n🎉 🎉")
            print("Ok, thanks for playing!")
            sys.exit("Bye! 👋")
    
    play_rock_paper_scissors()
    
rps()
