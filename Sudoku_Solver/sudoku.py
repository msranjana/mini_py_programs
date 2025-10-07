import streamlit as st
import numpy as np

# Sudoku Solver Functions
def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row//3), 3 * (col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Streamlit UI
st.title("Sudoku Solver 🧩")
st.write("Edit the numbers if you want and click Solve!")

# Sample pre-filled Sudoku puzzle (0 = empty)
sample_board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])

# Create a 9x9 grid for user input
board = np.zeros((9,9), dtype=int)
cols = st.columns(9)
for i in range(9):
    for j in range(9):
        with cols[j]:
            val = st.number_input(f"{i},{j}", min_value=0, max_value=9, value=int(sample_board[i][j]), key=f"{i}-{j}")
            board[i][j] = val

if st.button("Solve Sudoku"):
    board_copy = board.copy()
    if solve_sudoku(board_copy):
        st.success("Sudoku Solved ✅")
        st.table(board_copy)
    else:
        st.error("No solution exists for this board.")

if st.button("Clear Board"):
    st.experimental_rerun()
