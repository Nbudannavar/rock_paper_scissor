#ask the user to make a Choice    
# if choice is not valid  
# print an error   
# let the computer to make a choice  
# print choices(emojis)  
#  determine the winner  
#  ask the user if they want to continue  
# if not  
# terminate

import random

# Emoji mapping for fun visuals
emoji_map = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌️"
}

# Valid choices
choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")

while True:
    # Ask user for their choice
    user_choice = input("Make your choice (rock, paper, scissors): ").lower()

    # Validate choice
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Let the computer choose
    computer_choice = random.choice(choices)

    # Show both choices with emojis
    print(f"\nYou chose {user_choice} {emoji_map[user_choice]}")
    print(f"Computer chose {computer_choice} {emoji_map[computer_choice]}\n")

    # Determine the winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! 👋")
        break
