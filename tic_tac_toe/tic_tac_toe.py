import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.winner = None

    def print_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                return True
            elif " " not in self.board:
                self.winner = "Tie"
                return True
            self.current_player = "O" if self.current_player == "X" else "X"
            return True
        return False

    def check_winner(self):
        # Check rows, columns and diagonals
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for combo in win_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " "):
                return True
        return False

def play_game():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered from 1-9, left to right, top to bottom")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 \n")

    while not game.winner:
        game.print_board()
        try:
            if game.current_player == "X":
                position = int(input(f"Player {game.current_player}, enter position (1-9): ")) - 1
                if position < 0 or position > 8:
                    print("Please enter a number between 1 and 9")
                    continue
            else:
                # Simple AI: choose random available position
                available_positions = [i for i, spot in enumerate(game.board) if spot == " "]
                position = random.choice(available_positions)
                print(f"Computer (O) chooses position {position + 1}")
            
            if not game.make_move(position):
                if game.current_player == "X":
                    print("Position already taken. Try again.")
                continue
                
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    game.print_board()
    if game.winner == "Tie":
        print("It's a tie!")
    else:
        if game.winner == "X":
            print("Congratulations! You won!")
        else:
            print("Computer wins! Better luck next time!")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
