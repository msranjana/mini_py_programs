import tkinter as tk
import random

# Step 1: Define the options
options = ["Rock", "Paper", "Scissors"]

# Step 2: Initialize scores
user_score = 0
computer_score = 0

# Function to handle the game logic
def play(user_choice):
    global user_score, computer_score
    
    # Generate computer's choice
    computer_choice = random.choice(options)
    result_text = f"Computer chose: {computer_choice}\n"
    
    # Determine the winner
    if user_choice == computer_choice:
        result_text += "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_text += "You Win!"
        user_score += 1
    else:
        result_text += "You Lose!"
        computer_score += 1
    
    # Update labels
    result_label.config(text=result_text)
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

# Step 3: Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Step 4: Add UI components
# Title Label
title_label = tk.Label(window, text="Rock, Paper, Scissors", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="Make your choice!", font=("Arial", 14))
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(window, text="Score -> You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

# Buttons for user choices
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Exit Button
exit_button = tk.Button(window, text="Exit", font=("Arial", 12), command=window.quit)
exit_button.pack(pady=10)

# Step 5: Run the main event loop
window.mainloop()
