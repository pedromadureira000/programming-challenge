import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Your code goes here!
            # 1. Check if the guess is correct
            # 2. If not correct, give hints (too high or too low)
            # 3. If correct, break the loop

        except ValueError:
            print("Please enter a valid number!")

    # Your code goes here!
    # Display a message based on the number of attempts

if __name__ == "__main__":
    guess_number()
