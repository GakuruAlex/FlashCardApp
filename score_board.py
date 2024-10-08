from json import load, dump, JSONDecodeError
from tkinter import simpledialog, messagebox
from flash_card import FlashCard
class ScoreBoard(FlashCard):
    def __init__(self, window, timer, canvas, back_image,front_image):
        super().__init__( window, timer, canvas, back_image,front_image)
        self.data = {}
        self.score = 0

    def get_name(self):
        self.name = simpledialog.askstring(title="Name",prompt="Enter your Name", parent=self.window)
        print(f"Name: {self.name}")
        if self.name in self.data:
            answer = messagebox.askyesno(title="Name Exists", message="Name already exists do you want to change it ?", parent= self.window)
            if answer == "yes":
                self.get_name()
            else:
                self.scores = self.get_scores()
        return self.name
    def get_scores(self):
        try:
                with open("./scoreboard.json", "r") as scoreboard:
                    try:
                        self.data = load(scoreboard)
                    except JSONDecodeError as error:
                        print(f"Error: {error}")
                        return []
                    if self.name in self.data:
                        return self.data[self.name]
                    else:
                        return []
        except FileNotFoundError as missing_file:
            print(f"Error: {missing_file}")
            return []

    def increase_score(self):
        
        self.score += 1
    def got_wrong(self):
        self.cancel_countdown()
    def save_name_and_score(self):
        self.name = self.get_name()
        self.scores = self.get_scores()
        print(f"Name: {self.name} Score: {self.score}")
        self.scores.append(self.score)
        updated_dict = {self.name: self.scores}
        try:
            print(f"Name: {self.name} Score: {self.score} Scores: {self.scores}")
            with open("scoreboard.json", "w") as scoreboard:
                if self.name in self.data:
                    self.data.update(updated_dict)
                try:
                    dump({self.name: self.scores}, scoreboard, indent=4)
                except JSONDecodeError as e:
                    messagebox.showerror(title="JSON Decode Error", message=f"{e}")
        except FileNotFoundError as missing_file:
            print(f"Missing file: {missing_file}")