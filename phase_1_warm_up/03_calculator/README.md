Phase 1 · Project 03 of 10 · Previous: [Rock Paper Scissors](../02_rock_paper_scissors/) · Next: [Chatbot](../../phase_2_core_projects/04_chatbot/)

# Calculator

## Project Description

Create a calculator with a window and clickable buttons, like the calculator on a phone. This project uses tkinter, which comes with Python, so there is nothing extra to install.

## Student Requirements

- Open a window with a display at the top.
- Add buttons for the digits 0 to 9 and a decimal point.
- Support at least four operations: `+`, `-`, `*`, and `/`.
- Accept decimal numbers such as `2.5`, and show decimal answers such as `7.5`.
- Add an `=` button that shows the answer on the display.
- Add a Clear button that starts over.
- Do not crash when the user divides by zero. Show a message such as `Error` instead.

## Concepts Practiced

- functions
- conditionals
- variables
- floats and decimal numbers
- event-driven programming (code that runs when a button is clicked)
- tkinter windows, labels, and buttons
- lists and dictionaries

## Optional Add-Ons

- Show `4` instead of `4.0` when the answer is a whole number.
- Let the user chain operations, such as `2 + 3 * 4`.
- Add a backspace button.
- Add more operations, such as square root or percent.
- Let the user type with the keyboard as well as click.
- Make a command-line version first, using `input()` and `print()`, then build the window.

## Suggested Starter-Code TODOs

- Finish `calculate()` so it handles `+`, `-`, `*`, and `/`.
- Handle dividing by zero without crashing.
- Add the missing buttons to `button_rows`.
- Finish `press_operator()` so it remembers the first number and the operator.
- Finish `press_equals()` so it shows the answer.
- Stop the user from typing two decimal points in one number.
- Add a Clear button.

## Expected Behavior Example

```text
Click: 7  .  5  +  2  =
Display: 9.5

Click: 8  /  0  =
Display: Error
```

## Manual Test Cases

1. Input: click `2`, `+`, `3`, `=`
   Expected: The display shows `5`.

2. Input: click `7`, `.`, `5`, `-`, `2`, `=`
   Expected: The display shows `5.5`.

3. Input: click `6`, `*`, `4`, `=`
   Expected: The display shows `24`.

4. Input: click `9`, `/`, `2`, `=`
   Expected: The display shows `4.5`.

5. Input: click `8`, `/`, `0`, `=`
   Expected: The display shows an error message and the program does not crash.

6. Input: click `1`, `.`, `.`, `5`
   Expected: The display shows `1.5`, not `1..5`.

7. Input: click Clear after any calculation
   Expected: The display resets and a new calculation can start.
