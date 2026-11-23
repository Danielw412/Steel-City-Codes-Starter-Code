# Steel City Codes Starter Projects

Beginner Python starter projects for the Steel City Codes **Project-based (Python and Java)** course. Students in grades 4 to 8 build these projects in class with help from high-school volunteer instructors.

Each project folder contains:

- `README.md` with the project description, requirements, concepts, add-ons, an example, and manual tests
- `starter.py` with incomplete starter code and TODO comments for students to finish

Everything uses plain Python 3. Nothing extra needs to be installed.

## Course Phases

**Phase 0: Conceptual review.** The course starts with a review of Python basics in the class slides. There is no code for Phase 0 in this repository.

### Phase 1: Warm-Up (the class picks 2 of 3)

| # | Project | What it practices | Folder |
|---|---|---|---|
| 01 | Magic 8 Ball | `input()`, `print()`, loops, lists, random choices | [phase_1_warm_up/01_magic_8_ball](phase_1_warm_up/01_magic_8_ball/) |
| 02 | Rock Paper Scissors | strings, conditionals, loops, input validation | [phase_1_warm_up/02_rock_paper_scissors](phase_1_warm_up/02_rock_paper_scissors/) |
| 03 | Calculator (window) | functions, decimal numbers, tkinter buttons and events | [phase_1_warm_up/03_calculator](phase_1_warm_up/03_calculator/) |

### Phase 2: Core Projects (Chatbot first, then Tic-Tac-Toe or Hangman)

| # | Project | What it practices | Folder |
|---|---|---|---|
| 04 | Chatbot | strings, `.lower()`, keyword checks, loops | [phase_2_core_projects/04_chatbot](phase_2_core_projects/04_chatbot/) |
| 05 | Tic-Tac-Toe | functions, 2D lists, win checks, input validation | [phase_2_core_projects/05_tic_tac_toe](phase_2_core_projects/05_tic_tac_toe/) |
| 06 | Hangman | strings, lists, random choices, tracking guesses | [phase_2_core_projects/06_hangman](phase_2_core_projects/06_hangman/) |

### Phase 3: Final Project (the class picks 1 of 3)

| # | Project | What it practices | Folder |
|---|---|---|---|
| 07 | Minesweeper | 2D lists, dictionaries, recursion, random mines | [phase_3_final_project/07_minesweeper](phase_3_final_project/07_minesweeper/) |
| 08 | Connect 4 | 2D lists, four-in-a-row checks, a computer player | [phase_3_final_project/08_connect_4](phase_3_final_project/08_connect_4/) |
| 09 | Adventure Map | grids or rooms, dictionaries, game loops, optional classes | [phase_3_final_project/09_adventure_map](phase_3_final_project/09_adventure_map/) |

### Phase 3.5: Arcade GUI (optional)

| # | Project | What it practices | Folder |
|---|---|---|---|
| 10 | Arcade GUI (window) | dictionaries, classes, importing, launching other programs | [phase_3_5_arcade_gui/10_arcade_gui](phase_3_5_arcade_gui/10_arcade_gui/) |

## Course Rules

- **Phase 1:** the class picks 2 of the 3 warm-up projects.
- **Phase 2:** everyone builds the Chatbot first. Then the class builds Tic-Tac-Toe or Hangman.
- **Phase 3:** the class builds one final project: Minesweeper, Connect 4, or Adventure Map.
- **Phase 3.5:** the Arcade GUI is optional. It brings the class's finished projects together in one window.
- **The whole class does the same projects in the same order.** Every student works on the same project at the same time.

Each project README starts with a line that links to the previous and next project.

## How to Run a Project

Open a terminal, go into the project's folder, and run the starter file:

```bash
cd phase_1_warm_up/01_magic_8_ball
python starter.py
```

Use `python3 starter.py` if your computer uses `python3` for Python 3.

Most projects use the terminal: they ask questions with `input()` and answer with `print()`. The Calculator and the Arcade GUI use tkinter, so they open a window instead. tkinter comes with Python on Windows and macOS. On some Linux computers it must be installed separately (for example, `sudo apt install python3-tk`).
