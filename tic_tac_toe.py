# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)

import os
import subprocess
from pathlib import Path


# Function for ... (displaying the board?)
def blabla():
    pass


# Function for... (choosing a player?)
def blablabla():
    pass


# ... write as many functions as you need


def clear_terminal():
    if os.name == "nt":
        subprocess.run("cls", shell=True, check=False)
    else:
        subprocess.run(["clear"], check=False)


def print_logo():
    logo_path = Path(__file__).resolve().parent / "assets" / "game_logo.md"
    print(logo_path.read_text(encoding="utf-8"))
    print(" ")


def choose_game_mode(user_input_was_wrong: bool = False) -> int:
    print_logo()
    print("1.) Player 1 vs Player 2")
    print("2.) Player 1 vs Computer")
    print(" ")
    user_input = input("Please select your game mode [1 or 2]: ")

    if user_input != "1" and user_input != "2":
        choose_game_mode()

    return int(user_input)


def print_game_board(game: dict[int, int]):
    symbols = {1: "X", 2: "O"}
    cells = [str(position) if game[position] == 0 else symbols[game[position]]
             for position in range(1, 10)]

    for row in (0, 3, 6):
        print(f" {cells[row]} | {cells[row + 1]} | {cells[row + 2]} ")
        if row < 6:
            print("---+---+---")


def run_player_vs_player_game():
    game_board = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    print_game_board(game_board)


def run_player_vs_computer():
    clear_terminal()
    print_logo()
    print("Sorry! Not ready yet")
    input(" ")
    runGame()


def runGame():
    # Start a new round of Tic-tac-toe
    clear_terminal()

    game_mode = choose_game_mode()

    if game_mode == 1:
        run_player_vs_player_game()
    else:
        run_player_vs_computer()


# Tic-tac-toe game
if __name__ == "__main__":
    runGame()
