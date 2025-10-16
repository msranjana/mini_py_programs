import random
import time

class WordJumble:
    def __init__(self):
        self.words = [
            'python', 'programming', 'computer', 'keyboard', 'internet',
            'algorithm', 'function', 'variable', 'string', 'integer'
        ]
        self.score = 0
        self.high_score = self.load_high_score()

    def load_high_score(self):
        try:
            with open('highscore.txt', 'r') as f:
                return int(f.read())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        with open('highscore.txt', 'w') as f:
            f.write(str(self.high_score))

    def jumble_word(self, word):
        jumbled = list(word)
        random.shuffle(jumbled)
        return ''.join(jumbled)

    def play(self):
        print("\n=== Welcome to Word Jumble! ===")
        print("Unscramble the letters to form a meaningful word.")
        print("Type 'quit' to exit the game.\n")
        
        while True:
            word = random.choice(self.words)
            jumbled = self.jumble_word(word)
            
            print(f"Score: {self.score}")
            print(f"High Score: {self.high_score}")
            print("\nThe jumbled word is:", jumbled)
            
            guess = input("\nYour guess: ").lower()
            
            if guess == 'quit':
                print(f"\nThanks for playing! Your final score: {self.score}")
                if self.score > self.high_score:
                    print("New high score!")
                    self.high_score = self.score
                    self.save_high_score()
                break
                
            if guess == word:
                self.score += 1
                print("\nCorrect! Well done! 🎉")
                time.sleep(1)
            else:
                print(f"\nWrong! The word was: {word}")
                print("Game Over!")
                print(f"Final Score: {self.score}")
                
                if self.score > self.high_score:
                    print("🎉 New High Score! 🎉")
                    self.high_score = self.score
                    self.save_high_score()
                
                play_again = input("\nPlay again? (yes/no): ").lower()
                if play_again != 'yes':
                    break
                self.score = 0

if __name__ == "__main__":
    game = WordJumble()
    game.play()
