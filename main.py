import os
import subprocess
import sys

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR_ENABLED = True
except ImportError:
    COLOR_ENABLED = False

# --- MANUAL PROGRAM REGISTRY ---
PROGRAMS = {
    "Color Game": "colorGame/color-game.py",
    "Contact System": "contactSystem/contact_system.py",
    "Dice Game": "diceGame/dice_game.py",
    "Mini Quiz": "miniQuiz/minigame.py",
    "Pattern Game": "patternGame/pattern.py",
    "Rock Paper Scissor": "rockPaperScissor/rock-paper-scissor.py",
    "Star Pyramid": "starPyramid/star-pyramid.py",
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_title():
    if COLOR_ENABLED:
        print(Fore.CYAN + "=" * 45)
        print(Fore.YELLOW + "   🎮 Mini Python Programs Launcher 🎮   ")
        print(Fore.CYAN + "=" * 45 + Style.RESET_ALL)
    else:
        print("=" * 45)
        print("   Mini Python Programs Launcher   ")
        print("=" * 45)

def list_programs():
    print_title()
    for i, name in enumerate(PROGRAMS.keys(), 1):
        print(f"{i}. {name}")
    print(f"{len(PROGRAMS)+1}. Exit\n")

def run_program(choice):
    name = list(PROGRAMS.keys())[choice - 1]
    path = PROGRAMS[name]
    print(f"\nLaunching {name}...\n")

    # Run the selected program as a subprocess
    try:
        subprocess.run([sys.executable, path], check=False)
    except Exception as e:
        print(f"Error running {name}: {e}")

    input("\nPress Enter to return to the menu...")

def main():
    while True:
        clear_screen()
        list_programs()
        try:
            choice = int(input("Enter your choice: "))
            if choice == len(PROGRAMS) + 1:
                print("\nGoodbye! 👋")
                break
            elif 1 <= choice <= len(PROGRAMS):
                run_program(choice)
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Please enter a valid number.")
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
