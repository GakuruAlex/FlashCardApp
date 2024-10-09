from pandas import read_csv, DataFrame
from tkinter import PhotoImage
from random import choice

class FlashCard():
    TITLE_FONT = ("Serif", 40, "bold")
    CONTENT_FONT = ("Serif", 24, "normal")
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.cards = {}
        self.english = None
        self.french = None
        self.get_data()
        self.display_front_card()
    def get_data(self):
        data = DataFrame(read_csv("/home/aleyg/projects/Python/100DaysOfCode/DayThirty/FlashCardApp/data/french_words.csv"))
        self.cards = {row.French : row.English for index, row in data.iterrows()}
    def display_front_card(self):
        self.french = choice(list(self.cards.keys()))
        self.front_image = PhotoImage(file="/home/aleyg/projects/Python/100DaysOfCode/DayThirty/FlashCardApp/images/card_front.png", master=self.canvas)
        self.canvas.create_image(400, 280, image=self.front_image)
        self.canvas.create_text(400, 100, text=f"FRENCH", font=self.TITLE_FONT)
        self.canvas.create_text(400, 200, text=f"{self.french}", font=self.CONTENT_FONT)

