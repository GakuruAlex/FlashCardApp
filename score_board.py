from json import load, dump, JSONDecodeError
from tkinter import simpledialog, messagebox
from flash_card import FlashCard
class ScoreBoard(FlashCard):
    def __init__(self, window, timer, canvas, back_image,front_image):
        super().__init__( window, timer, canvas, back_image,front_image)
        self.data = {}
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
            else:
                self.scores = self.get_scores()
        return name
    def increase_score(self):
        self.score += 1
        self.run_all_cards()
    def got_wrong(self):
        self.run_all_cards()
    def save_name_and_score(self):
        self.scores.append(self.score)
        try:
            with open("scoreboard.json", "w") as scoreboard:
                dump({self.name: self.scores}, scoreboard, indent=4)
        except JSONDecodeError as e:
            messagebox.showerror(title="JSON Decode Error", message=f"{e}")