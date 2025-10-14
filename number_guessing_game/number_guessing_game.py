import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1–100): "))
            attempts += 1
            if guess < number:
                print("Too low! Try again.\n")
            elif guess > number:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == "__main__":
    number_guessing_game()
