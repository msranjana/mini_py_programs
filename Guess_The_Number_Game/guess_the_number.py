import random

def guess_the_number():
    """
    Implements a simple "Guess the Number" game.

    The computer generates a random number within a specified range (1 to 100),
    and the user has to guess it. The game provides feedback to the user
    ("Too high", "Too low") until they guess the correct number.
    """
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} tries.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()