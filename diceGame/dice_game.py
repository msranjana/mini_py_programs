import random

def roll():
    #Simulates rolling a die with a value between 1 and 6.
    return random.randint(1, 6)

def get_player_names(players):
    #Prompts users to input their names based on the number of players.
    player_names = []
    for i in range(1, players + 1):
        name = input(f"Enter the name for Player {i}: ")
        player_names.append(name)
    return player_names

def print_scores(player_names, player_scores):
    #Displays the current scores of all players.
    print("\nCurrent Scores:")
    for name, score in zip(player_names, player_scores):
        print(f"{name}: {score}")
    print()

def get_target_score():
    #Prompts the user to input the target score for the game.
    while True:
        target = input("Enter the target score to win (e.g. 50): ")
        if target.isdigit() and int(target) > 0:
            return int(target)
        print("Invalid input, please enter a positive number.")

def play_turn(player_name, current_score, max_rolls=3):
    #Handles the logic for a single player's turn with automatic rolling up to a set limit.
    print(f"\n{player_name}'s turn! Your current score is: {current_score}")
    turn_score = 0

    for roll_num in range(1, max_rolls + 1):
        roll_value = roll()
        print(f"{player_name} rolled a {roll_value} on roll {roll_num}!")

        if roll_value == 1:
            print("Oh no! You rolled a 1! You lose all points for this turn.")
            turn_score = 0
            break
        else:
            turn_score += roll_value
            print(f"Your score this turn is: {turn_score}")

        # If the player has rolled the maximum number of times, end the turn automatically
        if roll_num == max_rolls:
            print(f"{player_name}'s turn ends automatically after {max_rolls} rolls.")
            break

    return turn_score

def main_game():
    print("Welcome to the Dice Rolling Game!")

    # Get the number of players
    while True:
        players = input("Enter the number of players (2 - 4): ")
        if players.isdigit() and 2 <= int(players) <= 4:
            players = int(players)
            break
        print("Invalid input, must be between 2 and 4 players.")

    # Get player names and target score
    player_names = get_player_names(players)
    target_score = get_target_score()

    # Initialize player scores
    player_scores = [0 for _ in range(players)]

    # Main game loop
    while max(player_scores) < target_score:
        for player_idx, player_name in enumerate(player_names):
            print_scores(player_names, player_scores)

            turn_score = play_turn(player_name, player_scores[player_idx])
            player_scores[player_idx] += turn_score

            if player_scores[player_idx] >= target_score:
                break

    # Announce the winner
    winning_score = max(player_scores)
    winner = player_names[player_scores.index(winning_score)]
    print(f"\n{winner} is the winner with a score of {winning_score}!")

def play_again():
    """Asks the players if they want to play again."""
    while True:
        again = input("Do you want to play again? (y/n): ").lower()
        if again in ["y", "n"]:
            return again == "y"
        print("Invalid input, please type 'y' or 'n'.")

# Start the game loop
while True:
    main_game()
    if not play_again():
        print("Thanks for playing! Goodbye!")
        break
