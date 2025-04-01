def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        'apple': 2.5,
        'durian': 10.0,
        'jackfruit': 5.0,
        'kiwi': 3.0,
        'rambutan': 4.0,
        'mango': 3.5
    }
    
    total_cost = 0

    # Loop through the dictionary and prompt the user for the quantity of each fruit
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price

    # Print the total cost
    print(f"\nYour total is ${total_cost}")


main()
