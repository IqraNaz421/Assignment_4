
def in_stocke():
    user=input("Write a fruite name to check the stock (first letter should be capital): ")
    if user == "Apple":
        print("There are 23 apple in stock")
    elif user == "Banana":
        print("There are 3 banana in stock")
    elif user == "Orange":
        print("There are 56 oranges in stock")
    elif user == "Pear":
        print("There are 45 pears in stock")
    else:
        print("There is no fruite in stock")
in_stocke()