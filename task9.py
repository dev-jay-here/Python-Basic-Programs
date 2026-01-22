# ---------------------------------------------
# Rock-Paper-Scissors Game
# Author: [Your Name]
# Description:
# A simple Python game where the user plays against the computer.
# ---------------------------------------------

import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices:
        print("❌ Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing! Goodbye!")
        break
