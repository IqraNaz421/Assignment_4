def leap():
    user=int(input("Enter a year to ckeck if its leap or not: "))
    if user % 4 == 0:
        if user % 100==0:
            if user % 400==0:
                print("It is a leap year")

            else:
                print("Its is not leap year")
        else:
            print("Its is not leap year")
    else:
        print("Its is not leap year")
leap()