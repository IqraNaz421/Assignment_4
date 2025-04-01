import random
guess_number=random.randint(0,99)

while True:
   user=int(input("Guess a number: "))
   if (user < guess_number):
      print("You guess is too low")
   elif user > guess_number:
      print("Your guess is too high")
   else:
      print("Congo you got correct number")
