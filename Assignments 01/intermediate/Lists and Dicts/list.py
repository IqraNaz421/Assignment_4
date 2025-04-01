def main():
    # Create a list called fruit_list that contains the following fruits.
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list.
    print("Length of fruit list:", len(fruit_list))

    # Add 'mango' at the end of the list.
    fruit_list.append('mango')

    # Print the updated list.
    print("Updated fruit list:", fruit_list)

# Run the main function
main()


# Function to access an element in the list at a specific index
def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Index is out of range"
    return lst[index]

# Function to modify an element at a specific index
def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index is out of range"
    lst[index] = new_value
    return lst

# Function to slice the list from a start index to an end index
def slice_list(lst, start, end):
    if start < 0 or end > len(lst):
        return "Invalid indices for slicing"
    return lst[start:end]

# Game loop to interact with the user
def game():
    # Initialize the list with 5 elements (mix of numbers and strings)
    elements_list = [1, 'apple', 3.14, 'banana', 42]

    print("Welcome to the Index Game!")
    print("List to manipulate:", elements_list)

    while True:
        print("\nChoose an operation:")
        print("1: Access an element")
        print("2: Modify an element")
        print("3: Slice the list")
        print("4: Exit")

        operation = input("Enter the number corresponding to your choice: ")

        if operation == '1':  # Access an element
            index = int(input("Enter the index of the element to access: "))
            result = access_element(elements_list, index)
            print("Result:", result)
        
        elif operation == '2':  # Modify an element
            index = int(input("Enter the index of the element to modify: "))
            new_value = input("Enter the new value: ")
            result = modify_element(elements_list, index, new_value)
            print("Updated list:", result)
        
        elif operation == '3':  # Slice the list
            start = int(input("Enter the start index for slicing: "))
            end = int(input("Enter the end index for slicing: "))
            result = slice_list(elements_list, start, end)
            print("Sliced list:", result)
        
        elif operation == '4':  # Exit the game
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the game
game()

