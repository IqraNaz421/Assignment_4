minimium_height:int=50
def height():
    user=float(input("Enter you height? "))
    if user >= minimium_height:
        print("You can ride")
    else:
        print("You can not ride")
height()