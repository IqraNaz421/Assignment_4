import random
number_in_dice:int=6
num1_dice:int=random.randint(1, number_in_dice)
num2_dice:int=random.randint(1,number_in_dice)
total_number=num1_dice+num2_dice
print(num1_dice)
print(num2_dice)
print(f"The total number of this 2 dices is ", total_number)