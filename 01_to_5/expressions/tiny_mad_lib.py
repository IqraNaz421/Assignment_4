random_sentence: str = "Yesterday, I went to the park and saw a huge balloon. "

# Get user inputs
adjective: str = input("Enter an adjective: ")
noun: str = input("Enter a noun: ")
verb: str = input("Enter a verb: ")

# Print the combined sentence
print(random_sentence + "It was so " + adjective + "! Then, a " + noun + " appeared and started to " + verb + ".")
