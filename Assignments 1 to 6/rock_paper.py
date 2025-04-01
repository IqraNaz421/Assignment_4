import random

# List of valid moves
moves = ['rock', 'paper', 'scissors']

def play_game():
    # Get player's choice
    player_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()

    # Check if the player's input is valid
    if player_choice not in moves:
        print("Invalid input, please try again.")
        return
    
    # Get computer's choice randomly
    computer_choice = random.choice(moves)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

# Start the game
play_game()
