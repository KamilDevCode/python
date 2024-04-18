import random

user_score = 0
computer_score = 0

choices = ["heads", "tails"]
short_choices = ['h', 't']

while True:
    user_choice = input(f"Choose: '{short_choices[0]}' for {choices[0]} or '{short_choices[1]}' for {choices[1]}")
    print(f"User choice: '{user_choice}'")

    if user_choice not in short_choices:
        print('Not a valid choice!...')
        continue

    print("3...")
    print("2...")
    print("1...")
    print("Throw!")
    print('\n')

    computer_choice = random.choice(short_choices)
    print(f"Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        user_score += 1
        print(f"You won 🎉 🎉 and scored: {user_score} ")
    else:
        computer_score += 1
        print(f"Computer won 🐍: and have: {computer_score}")

    print(f'Your result: {user_score}, computer score: {computer_score}')

    play_again = input("Would you like to play again? [y/n] ")
    if play_again.lower() != 'y':
        break