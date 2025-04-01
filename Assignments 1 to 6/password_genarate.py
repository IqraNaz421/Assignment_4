import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters that can be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the pool and create the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Main function to collect user input and generate passwords
def main():
    try:
        # Get number of passwords and length of each password from user input
        num_passwords = int(input("How many passwords would you like to generate? "))
        length = int(input("What is the desired length of each password? "))

        # Check if the input values are positive
        if num_passwords <= 0 or length <= 0:
            print("Please enter positive values for both the number of passwords and the length.")
            return

        # Generate the passwords
        print("\nGenerated Passwords:")
        for _ in range(num_passwords):
            password = generate_password(length)
            print(password)

    except ValueError:
        print("Invalid input. Please enter valid integers.")

# Run the program
main()
