from pandas import read_csv
from tkinter import PhotoImage
from random import choice
class FlashCard():
    TITLE_FONT = ("Serif", 40, "bold")
    CONTENT_FONT = ("Serif", 24, "normal")
    def __init__(self, window, canvas ):
        self.window = window
        self.canvas = canvas
        self.cards = {}
        self.english = None
        self.french = None
        self.get_data()
    def get_data(self):
        data = read_csv("./data/french_words.csv")
        self.cards = {row.French : row.English for index, row in data.iterrows()}
    def display_front_card(self):
        self.french = choice(list(self.cards.keys()))
        self.create_card(file="./images/card_front.png", location=(400, 100), text="FRENCH", text_content=self.french)
    def display_back_card(self):
        self.english = self.cards[self.french]
        self.create_card(file= "./images/card_back.png",location=(400, 100),text="ENGLISH", text_content=self.english )
    def create_card(self, file,location, text, text_content):
        self.canvas.delete("all")
        self.image = PhotoImage(file=file, master=self.canvas)
        x_cor, y_cor = location
        image_adjust = 180
        second_text_adjust= 100
        self.canvas.create_image(x_cor, y_cor + image_adjust, image= self.image)
        self.canvas.create_text(x_cor, y_cor, text=text, font=self.TITLE_FONT )
        self.canvas.create_text(x_cor, y_cor + second_text_adjust, text= text_content, font=self.CONTENT_FONT)
