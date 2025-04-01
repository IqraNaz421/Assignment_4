def count_even(lst):
    # Populate the list by prompting the user for integers
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":  # If user presses enter without input, stop the loop
            break
        
        # Try to convert the input to an integer and add to the list if valid
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("That's not a valid integer. Please try again.")

    # Count and print the number of even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"The number of even numbers is: {even_count}")

# Example of how to call the function
numbers = []
count_even(numbers)
