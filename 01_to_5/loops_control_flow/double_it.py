# Ask the user to enter a number
num = int(input("Enter a number: "))

# Start with the user's number
curr_value = num

# Keep doubling the number until it is 100 or greater
while curr_value < 100:
    print(curr_value, end=" ")
    curr_value = curr_value * 2

# Print the final value when it's >= 100
print(curr_value)
