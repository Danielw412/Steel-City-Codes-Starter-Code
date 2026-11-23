"""Starter code for the Arcade GUI project.

The arcade is a tkinter window that launches the projects your class made.
"""

import subprocess
import sys
import tkinter as tk
from pathlib import Path


# This file is in phase_3_5_arcade_gui/10_arcade_gui, so the top folder of the
# repository is two folders above this one.
REPO_FOLDER = Path(__file__).resolve().parent.parent.parent

# TODO: Add one dictionary for each project your class finished.
# TODO: Put the creator's real name in each one.
projects = [
    {
        "name": "Magic 8 Ball",
        "creator": "TODO: your name",
        "script": "phase_1_warm_up/01_magic_8_ball/starter.py",
        "instructions": "Ask a yes-or-no question. Type quit to stop.",
    },
]


class ArcadeApp:
    """The arcade window and its pages."""

    def __init__(self, root):
        self.root = root
        self.root.title("Arcade")
        self.root.geometry("500x500")

        # Every page is drawn inside this frame.
        self.page = tk.Frame(self.root, padx=20, pady=20)
        self.page.pack(fill="both", expand=True)

        self.show_welcome_page()

    def clear_page(self):
        """Remove everything from the current page."""
        for widget in self.page.winfo_children():
            widget.destroy()

    def show_welcome_page(self):
        """Show the first page the player sees."""
        self.clear_page()

        tk.Label(self.page, text="Welcome to the Arcade!", font=("Arial", 24)).pack(pady=20)
        # TODO: Add a short message that explains the arcade.
        tk.Button(self.page, text="See the projects", command=self.show_menu_page).pack(pady=10)

    def show_menu_page(self):
        """Show one button for every project."""
        self.clear_page()

        tk.Label(self.page, text="Projects", font=("Arial", 24)).pack(pady=10)

        # TODO: Loop through projects and make one button for each.
        #       Each button should call self.show_project_page(project).
        #       Hint: command=lambda project=project: self.show_project_page(project)
        # TODO: Add a button that goes back to the welcome page.

    def show_project_page(self, project):
        """Show one project's name, creator, instructions, and Launch button."""
        self.clear_page()

        tk.Label(self.page, text=project["name"], font=("Arial", 24)).pack(pady=10)
        # TODO: Show "Made by" and the creator's name.
        # TODO: Show the instructions.
        # TODO: Add a Launch button that calls self.launch(project).
        # TODO: Add a button that goes back to the menu page.

    def launch(self, project):
        """Run the project's Python file in the terminal."""
        script = REPO_FOLDER / project["script"]

        # TODO: Show a message if the file does not exist.
        # TODO: Run the file with the same Python that runs the arcade:
        #       subprocess.run([sys.executable, str(script)], cwd=str(script.parent))
        print("TODO: launch", script)


def main():
    root = tk.Tk()
    ArcadeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
