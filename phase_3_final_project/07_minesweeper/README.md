Phase 3 · Project 07 of 10 · Previous: [Hangman](../../phase_2_core_projects/06_hangman/) · Next: [Connect 4](../08_connect_4/)

# Minesweeper

## Project Description

Create a command-line Minesweeper game. Mines are hidden on a grid. The player reveals squares one at a time, and each revealed square shows how many mines touch it. The player wins by revealing every safe square without hitting a mine.

## Student Requirements

- Let the user choose a difficulty, such as easy, medium, or hard. Harder levels use a bigger board, more mines, or both.
- Hide mines in random squares.
- Print the board with row and column numbers.
- Let the user reveal a square by typing its row and column.
- Show the number of touching mines on each revealed square.
- When the user reveals a square that touches 0 mines, open all the squares around it automatically, and keep going until the open area reaches numbered squares. Use recursion: a `reveal()` function that calls itself.
- Let the user place and remove flags on squares they think hide mines.
- End the game when the user reveals a mine, and show where all the mines were.
- Announce a win when every safe square is revealed.
- Ask if the user wants to play again.
- Validate input so wrong rows, columns, or commands do not crash the program.
- Use terminal input and printed output.

## Concepts Practiced

- input/output
- loops
- conditionals
- functions
- 2D lists
- dictionaries
- random choices
- recursion
- optional object-oriented programming

## Optional Command-Line Add-Ons

- Make the first square the user reveals always safe.
- Track wins and losses across games.
- Use classes for the squares, the board, or the game.
- Build a version with a window and mouse clicks using Pygame. This needs `pip install pygame`, so check with your instructor first.

## Suggested Starter-Code TODOs

- Add medium and hard difficulties.
- Place random mines on the answer board.
- Count the mines touching every square.
- Print row and column numbers around the board.
- Ask for a row and column, and check that they are on the board.
- Add flags.
- Finish `reveal()`, then make it open empty areas with recursion.
- Detect wins and losses.
- Add a replay loop.

## Expected Behavior Example

```text
Minesweeper
Choose a difficulty (easy, medium, hard): easy

    1  2  3  4  5  6
 1  #  #  #  #  #  #
 2  #  #  #  #  #  #
 3  #  #  #  #  #  #

Move (r row col, f row col, or q): r 1 1

    1  2  3  4  5  6
 1  .  .  1  #  #  #
 2  .  .  2  #  #  #
 3  1  1  3  #  #  #

Move (r row col, f row col, or q): f 1 4
```

## Manual Test Cases

1. Input: `easy`, then reveal a square
   Expected: The square shows a number, or a blank if no mines touch it.

2. Input: `banana` as the difficulty
   Expected: The program asks for a difficulty again.

3. Input: a row or column outside the board, such as `0` or `99`
   Expected: The program says the square is not on the board and asks again.

4. Input: flag a hidden square, then flag it again
   Expected: The flag appears, then disappears.

5. Input: reveal a square that hides a mine
   Expected: The program shows all the mines, says the game is over, and asks to play again.

6. Input: reveal every safe square
   Expected: The program announces a win.

7. Input: reveal a square that touches 0 mines
   Expected: The empty area around it opens up until it reaches numbered squares.

8. Input: `no` when asked to play again
   Expected: The program ends with a goodbye message.
