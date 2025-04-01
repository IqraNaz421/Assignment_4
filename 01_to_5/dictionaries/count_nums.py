numbers = {}

while True:
    user_input = input("Enter a number (or 'done' to stop): ")
    if user_input == 'done':
        break
    number = int(user_input)
    
    if number in numbers:
        numbers[number] += 1
    else:
        numbers[number] = 1

for number, count in numbers.items():
    print(f"{number} appears {count} times.")
