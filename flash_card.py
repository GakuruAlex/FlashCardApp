from ui import UI
from pandas import read_csv, DataFrame
from tkinter import PhotoImage, Text

class FlashCard(UI):
    TITLE_FONT = ("Serif", 20, "italic")
    CONTENT_FONT = ("Serif", 24, "normal")
    def __init__(self):
        super().__init__()
        self.cards = {}
        self.english = None
        self.french = None
        self.get_data()
    def get_data(self):
        data = DataFrame(read_csv("./data/french_words.csv"))
        self.cards = {row.French : row.English for index, row in data.iterrows()}
        print(f"Data {self.cards}")
    def display_front_card(self):
         self.front_image = PhotoImage(file="./images/card_front.png")
         self.canvas.create_image(400, 263, image=self.front_image, parent=self.canvas)
         self.front = Text(parent=self.canvas,str=f"French", font=self.TITLE_FONT)
         self.front.grid(row=1, column=2)