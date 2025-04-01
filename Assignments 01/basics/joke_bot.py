jokee = "Why did the banana go to the doctor? Because it wasn’t peeling well!"

def joke():
    user = input("What do you want to read: ")
    if user.lower() == "joke":
        print(jokee)
    else:
        print("Sorry, I only tell jokes.")

joke()
