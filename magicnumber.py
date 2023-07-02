import platform, os, random

# Create game variables
min = 1
max = 10

# Clear terminal
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

# Print game intro
print("-"*50, "MAGIC NUMBER GAME", "-"*50)
print(f"I have a number between {min} and {max}. Can you guess it?")



# Game Loop
while True:
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    max_tries = 3
    magic_number = random.randint(min, max)
    print(f"You can try {max_tries} times.")

    player_guess = input("What is your guess?")
    while str(magic_number) != player_guess:
        max_tries -= 1
        if max_tries == 0:
            break

        print(f"Wrong guess. You can try {max_tries} more times.")
        player_guess = input("What is your guess?")

    # Check final result
    if str(magic_number) == player_guess:
        print("You win!")
    else:
        print(f"You lost. My number was {magic_number}")

    # Ask player if he/she wants to play again.
    player_choice = input("Do you want to play again? (y/n)")
    if player_choice.lower() != "y":
        print("Ok... maybe next time... ")
        exit()