import random

print("Welcome to the Rock, Paper and Scissors Game")
user_choice = int(input("What will you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
computer_choice = random.randint(0, 2)
print(f"Computer choice: {computer_choice}")

if user_choice == computer_choice:
    print("This is a tie.")
elif user_choice == 0:  # Rock
    if computer_choice == 1:  # Paper
        print("You lose! Paper covers rock.")
    else:  # Scissors
        print("You win! Rock crushes scissors.")
elif user_choice == 1:  # Paper
    if computer_choice == 0:  # Rock
        print("You win! Paper covers rock.")
    else:  # Scissors
        print("You lose! Scissors cuts paper.")
elif user_choice == 2:  # Scissors
    if computer_choice == 0:  # Rock
        print("You lose! Rock crushes scissors.")
    else:  # Paper
        print("You win! Scissors cuts paper.")
else:
    print("Invalid input, please type 0, 1, or 2.")
