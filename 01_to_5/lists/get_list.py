def get_values():
    # Initialize an empty list
    lst = []

    # Continuously ask the user for input
    while True:
        value = input("Enter a value (or press Enter to stop): ")
        
        # If the user presses Enter without typing anything, stop the loop
        if value == "":
            break
        
        # Otherwise, add the value to the list
        lst.append(value)
    
    # Print the list after the loop ends
    print("Final list:", lst)

# Call the function to start the process
get_values()
