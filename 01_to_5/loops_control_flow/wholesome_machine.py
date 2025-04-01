affirmation = "I am capable of doing anything I put my mind to."
while True:
    user_input= input("Enter these words: " + affirmation +  "\n" )
    if user_input == affirmation:
        print("You got correct word")
        break
    else:
        print("Try again")
