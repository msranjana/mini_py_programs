import random

def hangman():
    """
    Implements the classic Hangman game.

    The computer selects a random word, and the player tries to guess it
    by suggesting letters. The player has a limited number of incorrect guesses
    before the game ends.
    """
    words = ["python", "hangman", "programming", "computer", "developer", "challenge", "keyboard", "monitor"]
    secret_word = random.choice(words).upper()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"I am thinking of a word. It has {len(secret_word)} letters.")

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(f"\n{display_word}")

        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

        print(f"You have {max_incorrect_guesses - incorrect_guesses} lives left.")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        guess = input("Enter a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
        elif guess in secret_word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            guessed_letters.append(guess)
            incorrect_guesses += 1

    else:
        print(f"\nYou ran out of lives! The word was: {secret_word}")

if __name__ == "__main__":
    hangman()