import random


DONE_LIKELIHOOD = 0.3

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    for i in range(10):
        if done():
            print("I'm done.")
            return
        print(i)

def main():
    chaotic_counting()

main()
