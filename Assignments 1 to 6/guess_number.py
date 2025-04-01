import random
random_number=random.randint(1,10)

while True:
    user=int(input("Guess a number: "))
    if user < random_number:
        print("Your guess is too low")
    elif user > random_number:
        print("Your guess is too high")
    else:
        print("You guess correct number")
    


    