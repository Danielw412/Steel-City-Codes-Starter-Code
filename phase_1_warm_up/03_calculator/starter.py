"""Starter code for the Calculator project.

This project opens a window using tkinter, which comes with Python.
"""

import tkinter as tk


# The calculator needs to remember these between button clicks.
state = {
    "first_number": None,
    "operator": None,
}

# TODO: Add the rest of the buttons: 4-9, 0, the decimal point, -, *, /, and =.
button_rows = [
    ["1", "2", "3", "+"],
]


def calculate(first, operator, second):
    """Return the answer for first, operator, second."""
    # TODO: Return first + second when the operator is "+".
    # TODO: Handle -, *, and / too.
    # TODO: Do not crash when dividing by zero. Show a message instead.
    return 0


def press_digit(display, digit):
    """Add a digit or decimal point to the number on the display."""
    # TODO: Do not allow two decimal points in one number.
    display.set(display.get() + digit)


def press_operator(display, operator):
    """Remember the first number and the operator."""
    # TODO: Save float(display.get()) in state["first_number"].
    # TODO: Save the operator in state["operator"].
    # TODO: Clear the display so the user can type the second number.
    print("TODO: remember", operator)


def press_equals(display):
    """Calculate the answer and show it on the display."""
    # TODO: Read the second number from the display.
    # TODO: Call calculate() and show the answer with display.set().
    print("TODO: calculate the answer")


def press_button(display, label):
    """Decide what to do for the button that was clicked."""
    if label in ["+", "-", "*", "/"]:
        press_operator(display, label)
    elif label == "=":
        press_equals(display)
    else:
        press_digit(display, label)


def build_window():
    """Create the window, the display, and the buttons."""
    window = tk.Tk()
    window.title("Calculator")

    display = tk.StringVar(value="")

    screen = tk.Label(window, textvariable=display, anchor="e", font=("Arial", 24), width=12)
    screen.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

    for row_index, row in enumerate(button_rows):
        for column_index, label in enumerate(row):
            button = tk.Button(
                window,
                text=label,
                width=5,
                height=2,
                command=lambda label=label: press_button(display, label),
            )
            button.grid(row=row_index + 1, column=column_index, padx=4, pady=4)

    # TODO: Add a Clear button that resets the display and the state.

    return window


def main():
    window = build_window()
    window.mainloop()


if __name__ == "__main__":
    main()
