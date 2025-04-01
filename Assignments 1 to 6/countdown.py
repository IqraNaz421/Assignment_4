import time

def countdown_timer(seconds):
    # While loop to count down
    while seconds > 0:
        # Print the remaining time
        print(f"Time remaining: {seconds} seconds")
        # Wait for 1 second
        time.sleep(1)
        # Decrease the time by 1 second
        seconds -= 1

    # When the timer reaches zero
    print("Time's up!")

def main():
    # Ask the user to enter the countdown time in seconds
    try:
        seconds = int(input("Enter the time in seconds for the countdown: "))
        if seconds <= 0:
            print("Please enter a positive integer for the countdown time.")
        else:
            countdown_timer(seconds)
    except ValueError:
        print("Please enter a valid integer.")

# Run the program
main()
