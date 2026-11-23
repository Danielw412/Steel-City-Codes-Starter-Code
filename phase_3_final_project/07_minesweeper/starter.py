"""Starter code for the Minesweeper project."""

import random


HIDDEN = "#"
FLAG = "F"
MINE = "*"
EMPTY = "."

# TODO: Add medium and hard difficulties with bigger boards and more mines.
difficulties = {
    "easy": {"size": 5, "mines": 4},
}


def choose_difficulty():
    """Ask the user for a difficulty and return it."""
    # TODO: Keep asking until the user types a difficulty in the dictionary.
    choice = input("Choose a difficulty (easy, medium, hard): ").strip().lower()
    return "easy"


def make_answer_board(size, mine_count):
    """Return a 2D list that stores MINE or the number of touching mines."""
    answer = []

    for _ in range(size):
        answer.append([0] * size)

    # TODO: Place mine_count mines in random squares.
    # TODO: For every other square, count the mines in the 8 squares around it.
    return answer


def print_board(view):
    """Print what the player can see, with row and column numbers."""
    # TODO: Print column numbers across the top.
    # TODO: Print a row number at the start of each row.
    for row in view:
        print(" ".join(row))


def reveal(answer, view, row, column):
    """Show the square at row, column on the player's view."""
    # TODO: Copy the number from answer into view.
    # TODO: If the square touches 0 mines, reveal its neighbors too.
    #       Calling reveal() from inside reveal() is called recursion.
    print("TODO: reveal row", row + 1, "column", column + 1)


def play_game():
    """Play one game of Minesweeper."""
    difficulty = choose_difficulty()
    size = difficulties[difficulty]["size"]
    mine_count = difficulties[difficulty]["mines"]

    answer = make_answer_board(size, mine_count)
    view = [[HIDDEN] * size for _ in range(size)]

    # TODO: Add the main game loop.
    print_board(view)
    action = input("Type r to reveal, f to flag, or q to quit: ").strip().lower()

    # TODO: Ask for a row and a column, and check that they are on the board.
    # TODO: If the action is f, place or remove a flag.
    # TODO: If the square is a mine, show all mines and end the game.
    # TODO: End the game with a win when every safe square is revealed.
    if action == "r":
        reveal(answer, view, 0, 0)


def main():
    print("Minesweeper")

    # TODO: Add a replay loop that asks "Play again? (yes/no)".
    play_game()


if __name__ == "__main__":
    main()
