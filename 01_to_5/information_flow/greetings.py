def greeting(name: str):  # Define greeting function
    print(f"Hello {name}")  # Print a greeting message using the name

def main():
    name = input("What is your name? ")  # Ask for the user's name
    greeting(name)  # Pass the name to the greeting function

main()  # Call the main function
