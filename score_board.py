from json import load, dump
from tkinter import simpledialog
class ScoreBoard:
    def __init__(self, window):
        self.window = window
        self.name = self.get_name()
        self.score = self.get_score()
    def get_score(self):
        try:
            with open("./scoreboard.json", "r") as scoreboard:
                data = load(scoreboard)
                return data[self.name]
        except FileNotFoundError:
            return 0
    def get_name(self):
        name = simpledialog.askstring(title="Name",prompt="Enter your Name", parent=self.window)
        return name
    