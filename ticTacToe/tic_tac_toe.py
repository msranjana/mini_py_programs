import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("300x350")
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Tic-Tac-Toe", font=("Arial", 16, "bold"))
        title.pack(pady=10)
        
        # Game board
        frame = tk.Frame(self.root)
        frame.pack(pady=10)
        
        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 20), width=4, height=2,
                          command=lambda i=i: self.make_move(i))
            btn.grid(row=i//3, column=i%3, padx=2, pady=2)
            self.buttons.append(btn)
        
        # Current player label
        self.player_label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", 
                                   font=("Arial", 12))
        self.player_label.pack(pady=10)
        
        # Reset button
        reset_btn = tk.Button(self.root, text="Reset Game", font=("Arial", 12),
                            command=self.reset_game)
        reset_btn.pack(pady=5)
    
    def make_move(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state="disabled")
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_all_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.player_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        winning_combinations = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # columns
            [0,4,8], [2,4,6]            # diagonals
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] 
                and self.board[combo[0]] != ""):
                return True
        return False
    
    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.player_label.config(text=f"Player {self.current_player}'s turn")
        for btn in self.buttons:
            btn.config(text="", state="normal")
    
    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
        self.root.mainloop()
        self.root.destroy()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()