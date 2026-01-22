# ---------------------------------------------
# Number Guessing Game
# Author: [Your Name]
# Description:
# The computer randomly selects a number between 1 and 100.
# The user must guess it, receiving hints until correct.
# ---------------------------------------------

import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.\n")
        elif guess > secret_number:
            print("📈 Too high! Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed it right in {attempts} attempts!")
            break

    except ValueError:
        print("❌ Please enter a valid number!\n")
