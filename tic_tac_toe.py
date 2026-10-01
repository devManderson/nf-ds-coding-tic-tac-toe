import os
import subprocess
from pathlib import Path


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
    clear_terminal()
    print_logo()

    symbols = {1: "X", 2: "O"}
    cells = [
        str(position) if game[position] == 0 else symbols[game[position]]
        for position in range(1, 10)
    ]

    border = "+---+---+---+"
    for row in (0, 3, 6):
        print(border)
        print(f"| {cells[row]} | {cells[row + 1]} | {cells[row + 2]} |")
    print(border)


def print_player_one_select():
    pass


def run_player_vs_player_game():
    game_board = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    user_input = print_player_one_select()
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
