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


def choose_game_mode() -> int:
    print_logo()
    print("1.) Player 1 vs Player 2")
    print("2.) Player 1 vs Computer")
    print(" ")
    user_input = input("Please select your game mode [1 or 2]: ")

    if user_input != "1" and user_input != "2":
        choose_game_mode()

    return int(user_input)


def print_game_board(game: dict[int, int], player_one_symbol: str):
    clear_terminal()
    print_logo()

    player_two_symbol = "O" if player_one_symbol == "X" else "X"
    print(f"Player 1: {player_one_symbol} | Player 2: {player_two_symbol}")
    print()

    cells = []
    for position in range(1, 10):
        if game[position] == 0:
            cells.append(str(position))
        elif game[position] == 1:
            cells.append(f"\033[34m{player_one_symbol}\033[0m")
        else:
            cells.append(f"\033[31m{player_two_symbol}\033[0m")

    border = "+---+---+---+"
    for row in (0, 3, 6):
        print(border)
        print(f"| {cells[row]} | {cells[row + 1]} | {cells[row + 2]} |")
    print(border)


def print_player_one_select() -> str:
    clear_terminal()
    print_logo()
    choice = input("Player 1, choose your symbol [X or O]: ").strip().upper()
    if choice not in ("X", "O"):
        print("Please enter X or O.")
        return print_player_one_select()
    return choice


def choose_field(game: dict[int, int], player: int, symbol: str) -> int:
    while True:
        user_input = input(
            f"Player {player} ({symbol}), choose a field [1-9]: "
        ).strip()

        try:
            field = int(user_input)
        except ValueError:
            print("Please enter a number from 1 to 9.")
            continue

        if field not in game:
            print("Please enter a number from 1 to 9.")
        elif game[field] != 0:
            print("This field is already taken. Choose another one.")
        else:
            return field


def has_player_won(game: dict[int, int], player: int) -> bool:
    winning_lines = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7),
    )
    return any(all(game[field] == player for field in line) for line in winning_lines)


def run_player_vs_player_game():
    game_board = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    player_one_symbol = print_player_one_select()
    player_two_symbol = "O" if player_one_symbol == "X" else "X"
    current_player = 1

    while True:
        print_game_board(game_board, player_one_symbol)
        symbol = player_one_symbol if current_player == 1 else player_two_symbol
        field = choose_field(game_board, current_player, symbol)
        game_board[field] = current_player

        if has_player_won(game_board, current_player):
            print_game_board(game_board, player_one_symbol)
            print(f"\033[32mPlayer {current_player} ({symbol}) wins!\033[0m")
            return

        if all(value != 0 for value in game_board.values()):
            print_game_board(game_board, player_one_symbol)
            print("It's a draw!")
            return

        current_player = 2 if current_player == 1 else 1


def run_player_vs_computer():
    clear_terminal()
    print_logo()
    print("Sorry! Not ready yet")
    input(" ")
    runGame()


def runGame():
    clear_terminal()

    game_mode = choose_game_mode()

    if game_mode == 1:
        run_player_vs_player_game()
    else:
        run_player_vs_computer()


# Tic-tac-toe game
if __name__ == "__main__":
    runGame()
