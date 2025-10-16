import random

def scramble_word(word):
    """Returns a scrambled version of the given word."""
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def play_game():
    print("🎮 Welcome to the Word Scramble Game! 🎯")
    words = ["apple", "banana", "orange", "grape", "cherry", "mango", "strawberry"]
    word = random.choice(words)
    scrambled = scramble_word(word)
    print(f"\nScrambled word: {scrambled}")

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower()
        if guess == word:
            print("✅ Correct! You guessed it right!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"❌ Wrong! Try again. Attempts left: {attempts}")
            else:
                print(f"😞 Out of attempts! The correct word was '{word}'.")
                break

if __name__ == "__main__":
    play_game()
