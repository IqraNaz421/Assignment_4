def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        # Noun sentence template
        print(f"After a long day, I can't wait to relax with my {word}.")
    elif part_of_speech == 1:
        # Verb sentence template
        print(f"Every morning, I wake up and feel the urge to {word}!")
    elif part_of_speech == 2:
        # Adjective sentence template
        print(f"The movie was so {word}, I couldn't stop smiling the entire time!")
    else:
        print("Invalid part of speech. Please type 0 for noun, 1 for verb, or 2 for adjective.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

# Run the program
main()
