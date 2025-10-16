# Mini Python Projects

Welcome to the **Mini Python Projects**! This repository features several mini-games and programs developed in Python. These projects demonstrate the use of popular libraries such as **Tkinter** for graphical user interfaces (GUIs) and **Turtle** for graphics.

### please do star the repo :)
## Games and Applications

1. [Color Game](#1-color-game)
2. [Contact Management System](#2-contact-management-system)
3. [Dice Rolling Game](#3-dice-rolling-game)
4. [Text Adventure Game](#4-text-adventure-game)
5. [Turtle Graphics](#5-turtle-graphics)
6. [Star Pyramid Generator](#6-star-pyramid-generator)
7. [Rock, Paper, Scissors Game](#7-rock-paper-scissors-game)
8. [Snake Game](#8-snake-game)
9. [Sudoku Solver](#9-sudoku-solver)
10. [Number Guessing Game](#10-number-guessing-game)
11. [Word Scramble Game](#11-word-scramble-game)
---

## 1. Color Game

### Description

Test your reflexes and concentration! The **Color Game** challenges players to type the **color of the text** displayed on the screen—not the word itself. You have 30 seconds to score as many correct answers as possible.

### Features

- Real-time score tracking
- High score storage
- Simple and engaging GUI built with Tkinter

### How to Play

1. Launch the game.
2. Press **Enter** to start.
3. Type the color of the displayed text (not the word) as fast as you can!

---

## 2. Contact Management System

### Description

Manage your personal or professional contacts efficiently with this program. You can add, search, delete, and view all contacts.

### Features

- Add contacts with details such as **name**, **age**, and **email**.
- Validate email formats automatically.
- Save and load contacts using a JSON file for persistent storage.

### How to Use

1. Run the program.
2. Follow the interactive prompts to manage your contacts.

---

## 3. Dice Rolling Game

### Description

Compete against friends in this simple but thrilling dice-rolling game. Roll the dice, avoid penalties, and be the first to reach the target score.

### Features

- Supports 2 to 4 players
- Automatic score tracking
- Rolling a **1** resets the current player's turn score

### How to Play

1. Input the number of players and their names.
2. Set a target score.
3. Take turns rolling the dice until a player reaches the target score.

---

## 4. Text Adventure Game

### Description

Dive into a world of choices with this **text-based adventure game**. Every decision you make leads to a unique outcome.

### Features

- Interactive story with multiple endings
- Player-driven choices that affect the storyline

### How to Play

1. Launch the program.
2. Follow the text prompts and make choices by typing the corresponding options.

---

## 5. Turtle Graphics

### Description

Unleash your creativity with **Turtle Graphics**, which generates vibrant spirals using Python's built-in **Turtle** library.

### Features

- Randomized colors for a dynamic visual display
- Easy to modify and expand with your own designs

### How to Run

1. Run the script.
2. Watch the colorful spiral unfold!

---

## 6. Star Pyramid Generator

### Description

Create aesthetically pleasing star pyramids based on the height you specify. This program is perfect for understanding loops and patterns in Python.

### Features

- User-defined pyramid height
- Clean and centered alignment

### How to Use

1. Run the program.
2. Enter the desired height for your pyramid.
3. Generate more pyramids or quit the program.

---

## 7. Rock Paper Scissors Game

### Description

A simple and interactive Rock, Paper, Scissors game built using Python's tkinter library. Play against the computer and keep track of your score while enjoying a fun GUI-based experience!

### Features

- User-Friendly Interface: Built with tkinter, making it easy to use for all ages.
- Score Tracking: Displays real-time scores for both the user and the computer.
- Replayable: Play as many rounds as you want, with scores updated after each game.
- Dynamic Outcome Display: Shows the computer's choice and the result of each round.

### How to Run
1. Choose one of the three options by clicking the corresponding button:
- Rock
- Paper
- Scissors
2. The computer will randomly select its choice.
3. The game will display the computer's choice and the result:
- "You Win!" if you win the round.
- "You Lose!" if the computer wins the round.
- "It's a Tie!" if both choices are the same.
4. Scores will update automatically.

---

## 8. Snake Game

### Description
Experience the classic arcade game with this Python implementation! Control a snake to eat food and grow longer while avoiding collisions with yourself. Built with Pygame for smooth graphics and responsive controls.

### Features
Smooth Movement: Responsive arrow key controls

Score Tracking: Real-time score display

Game Over Detection: Self-collision ends the game

Wrap-around Screen: Snake can move through screen boundaries

Visual Feedback: Clean grid-based graphics with colored elements

### How to Play
Use Arrow Keys to control the snake's direction:

 - ↑ Up

 - ↓ Down

 - ← Left

 - → Right

 - Eat the red food to grow longer and increase your score

 - Avoid running into your own body

 - Try to achieve the highest score possible!

## 10. Number Guessing Game

### Description
Guess the number between 1 and 100 in the fewest attempts possible! After each guess, the game tells whether your guess was too high or too low.

### Features
- Random number each round
- Tracks number of attempts
- Simple terminal-based gameplay

### How to Play
Run the script and start guessing!

## 11. Word Scramble Game

### Description
Unscramble the given word before running out of attempts! The program randomly selects a word, scrambles it, and asks the user to guess the original word.

### Features
- Random word selection
- 3 attempts to guess
- Displays the correct word if you fail

### How to Play
Run the script and type your guesses until you find the right word!


## Getting Started

### Prerequisites

Make sure you have the following:

- **Python 3.x** installed on your machine
- Required libraries (all are standard in Python):
  - **Tkinter** (for GUI)
  - **Turtle** (for graphics)
  - **JSON** (for saving data)

### Installation

1. Clone this repository or download the project files:

   ```bash
   git clone <repository-link>
   ````
2. Open a terminal or command prompt.
3. Navigate to the directory containing the scripts.

### Running the Games

 To run the launcher, use the following command:

   ````bash
  python3 main.py
   ````
Select the number corresponding with the game/program you want to use.

## 9. Sudoku Solver 

### Description

​	An interactive Sudoku solver built with Streamlit. Users can input any valid 9x9 Sudoku puzzle, and the program will find the solution using a backtracking algorithm.

### Features

- **Interactive 9x9 Grid:** Easily input or edit numbers in a user-friendly grid.
- **Automated Solving:** Employs a powerful backtracking algorithm to solve the puzzle with a single click.
- **Pre-filled Sample:** Comes with a default Sudoku puzzle for quick testing.
- **Instant Feedback:** Immediately displays a success message with the solution or an error if the puzzle is unsolvable.

### How to Play

1.  Make sure you have Python installed.
2.  Install the required libraries:
    ```bash
    pip install streamlit numpy
    ```
3.  Run the application from your terminal:
    ```bash
    streamlit run sudoku_solver.py
    ```
4.  The web app will open in your browser. Edit the grid to input your own Sudoku puzzle.
5.  Click the "Solve Sudoku" button to see the solution.

## License

This project is licensed under the [MIT License](./LICENSE).
