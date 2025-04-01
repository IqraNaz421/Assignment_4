import random

# Program to guess the number
def guess_my_number():
    # Randomly choose a number between 0 and 99
    number_to_guess = random.randint(0, 99)
    
    # Prompt the user to enter a guess
    guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
    
    # Keep asking for guesses until the user guesses correctly
    while guess != number_to_guess:
        if guess < number_to_guess:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        # Ask for a new guess
        guess = int(input("Enter a new number: "))
    
    # If the guess is correct, print the congratulations message
    print(f"Congrats! The number was: {number_to_guess}")

# Call the function to start the game
guess_my_number()
