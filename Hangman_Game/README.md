# Hangman Game

## Problem Statement
Implement the classic Hangman game where the computer selects a random word, and the player tries to guess it by suggesting letters. The player has a limited number of incorrect guesses before the game ends.

## Example

```
Welcome to Hangman!
I am thinking of a word. It has 5 letters.

_ _ _ _ _

You have 6 lives left.
Guessed letters: 

Enter a letter: a
Good guess!

_ A _ _ _

You have 6 lives left.
Guessed letters: A

Enter a letter: e
Sorry, 'e' is not in the word.

_ A _ _ _

You have 5 lives left.
Guessed letters: A, E

Enter a letter: p
Good guess!

P A P _ _

You have 5 lives left.
Guessed letters: A, E, P

Enter a letter: l
Good guess!

P A P L _

You have 5 lives left.
Guessed letters: A, E, P, L

Enter a letter: y
Good guess!

P A P L Y

Congratulations! You guessed the word: PAPLY
```

## Constraints
- The word to be guessed should be chosen randomly from a predefined list.
- The player should have a limited number of incorrect guesses (e.g., 6 lives).
- The game should display the current state of the word (e.g., `_ _ _ _ _`).
- The game should keep track of guessed letters.
- Input should be case-insensitive.

## Complexity Analysis

### Time Complexity
- **Word Selection**: `O(1)` if the word list is small and pre-defined. If it's loaded from a file, it depends on file I/O.
- **Guessing Loop**: In the worst case, the player might guess every letter of the alphabet. Each guess involves checking if the letter is in the word, updating the displayed word, and updating lives. This is `O(L * W)` where `L` is the number of unique letters in the alphabet and `W` is the length of the word. However, since `L` is constant (26), it's effectively `O(W)` per guess.

### Space Complexity
- The space complexity is `O(W + L)` where `W` is the length of the word and `L` is the number of guessed letters. This is because we store the secret word, the displayed word, and the list of guessed letters. Given the typical constraints of Hangman, this is very small and can be considered `O(1)` for practical purposes.