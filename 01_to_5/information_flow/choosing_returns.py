adult_age=True
non_adult_age=False
def checking_age():
    user=int(input("How old are you? "))
    if user >= 18:
        print(adult_age)
    else:
        print(non_adult_age)
checking_age()