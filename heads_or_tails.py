
import random

user_score = 0
computer_score = 0

choices = ["heads", "tails"]


while True:
    user_choice = input(f"Choose: 'h' for {choices[0]} or 't' for {choices[1]}")
    print(f"player choice: '{user_choice}'")

    if user_choice not in ["h", "t"]:
        print('Wrong choice...do you mean heads or tails?')
        continue

    print("3...")
    print("2...")
    print("1...")
    print("throw!")
    print('\n')

    computer_choice = random.choice(choices)
    print(f"Computer choice: {computer_choice}")
    if user_choice == 'h':
        user_choice = 'heads'

    else:
        user_choice = 'tails'


    if user_choice == computer_choice:
        print('It\'s a tie! 🤝')
    elif(user_choice == 'heads' and computer_choice == 'tails') or  \
        (user_choice == 'tails' and computer_choice == 'heads'):
        user_score += 1
        print(f"You won:  🎉 {user_score} ")
    else:
        computer_score += 1
        print(f"Python won this round! 🐍: {computer_score}")

    print(f'Your score: {user_score}, Python score: {computer_score}')

    play_again = input("Would you like play again? [y/n] ")
    if play_again.lower() != 'y':
        break
