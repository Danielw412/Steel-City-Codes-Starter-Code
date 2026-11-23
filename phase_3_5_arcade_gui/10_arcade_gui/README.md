Phase 3.5 · Project 10 of 10 · Previous: [Adventure Map](../../phase_3_final_project/09_adventure_map/) · Next: [Course overview](../../README.md)

# Arcade GUI

## Project Description

This project is optional. Build an arcade: a window that collects the projects your class made and launches them. The arcade has a welcome page, a page with one button per project, and a page for each project with its instructions, the name of the student who made it, and a Launch button. This project uses tkinter, which comes with Python.

## Student Requirements

- Open a window with a welcome page.
- Add a page that lists the class projects as buttons.
- Clicking a project shows a page with:
  - the project's name
  - the creator's name
  - instructions for playing
  - a Launch button
- The Launch button runs that project's Python file. Terminal projects run in the terminal you started the arcade from.
- Add Back buttons so the user can move between pages.
- Store the project information in a list of dictionaries.
- Use a class for the arcade window.
- Show a message instead of crashing if a project's file is missing.

## Concepts Practiced

- dictionaries
- lists
- classes and methods
- importing modules (`tkinter`, `subprocess`, `sys`, `pathlib`)
- functions
- event-driven programming
- file paths

## Optional Add-Ons

- Move the list of projects into its own file, such as `arcade_projects.py`, and import it.
- Hide the arcade window while a project runs, then bring it back.
- Add colors, a logo, or a different font.
- Add a page that lists everyone in the class.
- Group the projects by phase.

## Suggested Starter-Code TODOs

- Add a dictionary for every project your class finished, with the real creator names.
- Add a short welcome message.
- Make one button per project on the menu page.
- Show the creator and instructions on the project page.
- Add a Launch button and Back buttons.
- Finish `launch()` so it checks that the file exists, then runs it with `subprocess.run()` and `sys.executable`.

## Expected Behavior Example

```text
Window: "Welcome to the Arcade!"  [See the projects]
Click: See the projects
Window: Projects  [Magic 8 Ball] [Rock Paper Scissors] [Chatbot] ...
Click: Magic 8 Ball
Window: Magic 8 Ball / Made by Jordan / Ask a yes-or-no question...  [Launch] [Back]
Click: Launch
Terminal:
Welcome to Magic 8 Ball!
Ask a yes/no question, or type quit to stop.
Question:
```

## Manual Test Cases

1. Input: start the arcade
   Expected: A window opens on the welcome page.

2. Input: click the button that shows the projects
   Expected: One button appears for every project in the list.

3. Input: click a project button
   Expected: The project page shows the name, creator, and instructions.

4. Input: click Launch on a terminal project
   Expected: The project runs in the terminal. When it ends, the arcade still works.

5. Input: click Back on a project page
   Expected: The project list appears again.

6. Input: click Launch for a project whose file path is wrong
   Expected: The arcade shows an error message and does not crash.
