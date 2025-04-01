import random

# A dictionary with words and their clues
words_and_clues = {
    'python': 'A popular programming language',
    'elephant': 'A large animal with big ears',
    'guitar': 'A musical instrument with strings',
    'apple': 'A common fruit that keeps doctors away',
    'mountain': 'A large natural elevation of the earth\'s surface'
}

def get_random_word():
    # Randomly select a word from the dictionary
    word = random.choice(list(words_and_clues.keys()))
    return word

def play_game():
    word = get_random_word()
    clue = words_and_clues[word]  # Get the clue for the word
    word_length = len(word)
    guessed_letters = []  # Store the letters that have been guessed by the player
    tries = 6  # Number of guesses the player has

    print("Welcome to 'Guess the Word'!")
    print(f"Clue: {clue}")
    print(f"The word has {word_length} letters.")

    while tries > 0:
        # Show the current state of the word
        current_word_state = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Current word:", current_word_state)

        guess = input("Guess a letter or the entire word: ").lower()

        # Check if the guess is valid
        if len(guess) == 1:  # Player guessed a single letter
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
                print(f"Good guess! '{guess}' is in the word.")
            else:
                tries -= 1
                print(f"Wrong guess! You have {tries} tries left.")
        elif len(guess) == len(word) and guess.isalpha():  # Player guessed the whole word
            if guess == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
            else:
                tries -= 1
                print(f"Wrong guess! You have {tries} tries left.")
        else:
            print("Invalid input. Please enter a valid letter or word.")

        # Check if the player has guessed all letters
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break

    if tries == 0:
        print(f"Sorry, you're out of tries. The word was: {word}")

# Start the game
play_game()
