# Tic-Tac-Toe Game

A simple command-line implementation of the classic Tic-Tac-Toe game in Python, featuring player vs computer gameplay.

## Features

- Player vs Computer gameplay
- Simple AI opponent
- Clear board display
- Input validation
- Play multiple games in one session
- Clear instructions and position numbering

## How to Play

1. Run the game using Python 3:
   ```
   python tic_tac_toe.py
   ```

2. The board positions are numbered from 1 to 9, left to right, top to bottom:
   ```
    1 | 2 | 3 
   -----------
    4 | 5 | 6 
   -----------
    7 | 8 | 9 
   ```

3. When prompted, enter a number (1-9) to place your 'X' on the board.

4. The computer will automatically make its move as 'O'.

5. The first to get three in a row (horizontally, vertically, or diagonally) wins!

## Example Game

```
Welcome to Tic-Tac-Toe!
Positions are numbered from 1-9, left to right, top to bottom
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 


   |   |   
-----------
   |   |   
-----------
   |   |   


Player X, enter position (1-9): 5


   |   |   
-----------
   | X |   
-----------
   |   |   


Computer (O) chooses position 1


 O |   |   
-----------
   | X |   
-----------
   |   |   
```

## Requirements

- Python 3.x
- No additional packages required

## How to Run

1. Navigate to the game directory
2. Run: `python tic_tac_toe.py`
3. Follow the on-screen instructions to play!

## Game Rules

- You are 'X' and the computer is 'O'
- Take turns placing your mark on the board
- First to get three in a row wins
- If all squares are filled with no winner, it's a tie
- You can play multiple games in one session
