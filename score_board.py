from json import load, dump, JSONDecodeError
from tkinter import simpledialog, messagebox
class ScoreBoard:
    def __init__(self, window):
        self.window = window
        self.name = self.get_name()
        self.scores = []
        self.score = 0
    def get_scores(self):
        try:
            with open("./scoreboard.json", "r") as scoreboard:
                self.data = load(scoreboard)
                return self.data[self.name]
        except FileNotFoundError as missing_file:
            messagebox.showerror(title="File not Found!", message=f"{missing_file} not found")
    def get_name(self):
        name = simpledialog.askstring(title="Name",prompt="Enter your Name", parent=self.window)
        if name in self.data:
            answer = messagebox.askyesno(title="Name Exists", message="Name already exists do you want to change it ?")
            if answer == "yes":
                self.get_name()
            return name
    def save_name_and_score(self):
        self.scores.append(self.score)
        try:
            with open("scoreboard.json", "w") as scoreboard:
                dump({self.name: self.scores}, scoreboard, indent=4)
        except JSONDecodeError as e:
            messagebox.ERROR(e)