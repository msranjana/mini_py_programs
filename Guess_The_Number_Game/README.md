# Guess the Number Game

## Problem Statement
Implement a simple "Guess the Number" game where the computer generates a random number within a specified range, and the user has to guess it. The game should provide feedback to the user (e.g., "Too high", "Too low") until they guess the correct number.

## Example

```
Welcome to the Guess the Number Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too high! Try again.
Enter your guess: 25
Too low! Try again.
Enter your guess: 37
Too high! Try again.
Enter your guess: 30
Too low! Try again.
Enter your guess: 33
Congratulations! You guessed the number 33 in 5 tries.
```

## Constraints
- The random number should be an integer.
- The game should continue until the correct number is guessed.
- The game should provide appropriate feedback to the user.
- The number of attempts should be tracked.

## Complexity Analysis

### Time Complexity
The time complexity of the game depends on the number of guesses the user takes. In the worst-case scenario, if the user guesses linearly, it could take `O(N)` guesses, where `N` is the range of numbers. However, if the user employs a binary search strategy, the time complexity would be `O(log N)`.

### Space Complexity
The space complexity is `O(1)` as only a few variables are used to store the random number, user's guess, and the number of attempts, regardless of the range of numbers.