import random

# Function to start the game
def computer_guess():
    print("Welcome to the Computer Guessing Game!")
    print("Please think of a number between 1 and 100 and I'll try to guess it.")
    
    # Initialize the range of possible numbers
    low = 1
    high = 100
    attempts = 0
    
    while True:
        # Let the computer make a guess in the current range
        guess = random.randint(low, high)
        attempts += 1
        
        # Get user feedback on the guess
        print(f"Computer's guess: {guess}")
        feedback = input("Is the guess too low (L), too high (H), or correct (C)? ").lower()
        
        # Check if the user provided valid feedback
        if feedback not in ['l', 'h', 'c']:
            print("Please enter L for too low, H for too high, or C for correct.")
            continue
        
        # Adjust the range based on the user's feedback
        if feedback == 'l':
            low = guess + 1  # The guess was too low, so we increase the lower bound
        elif feedback == 'h':
            high = guess - 1  # The guess was too high, so we decrease the upper bound
        elif feedback == 'c':
            print(f"Yay! The computer guessed your number {guess} correctly in {attempts} attempts.")
            break  # Exit the loop once the correct guess is made

# Start the game
computer_guess()
