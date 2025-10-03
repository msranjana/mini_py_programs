def start_game():
    name = input("Hey, type your name: ")
    print("Hello " + name + ", welcome to my game!")

    should_we_play = input("Do you want to play? (yes/no) ").lower()
    
    if should_we_play in ["y", "yes"]:
        play_game()
    else:
        print("We are NOT playing...")

def play_game():
    print("We are gonna play!")

    direction = input("Do you want to go left or right? (left/right) ").lower()
    
    if direction == "left":
        print("You went left and fell off a cliff. Game over, try again.")
    elif direction == "right":
        choice = input("Okay, you now see a bridge. Do you want to swim under it or cross it? (swim/cross) ").lower()
        if choice == "swim":
            print("You got eaten by an alligator. You die, the end!")
        elif choice == "cross":
            print("You found the gold and won!")
        else:
            print("Sorry, not a valid reply. You die!")
    else:
        print("Invalid choice! You die!")

start_game()
