import random

def play_high_low():
    rounds = 5  # Number of rounds to play
    score = 0  # Player's score
    
    for round_num in range(1, rounds + 1):
        # Generate random numbers for the player and the computer
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Round {round_num}")
        print(f"Your number: {player_number}")
        
        # Ask the player to guess whether their number is higher or lower
        guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").lower()

        # Check the player's guess
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print("Correct guess!")
            score += 1
        else:
            print("Incorrect guess!")
        
        print(f"The computer's number was: {computer_number}\n")
    
    # Display the final score
    print(f"Game over! Your final score is: {score} out of {rounds}")

# Start the game
play_high_low()
