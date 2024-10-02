from random import choice
from time import sleep, strftime, gmtime
from pandas import  read_csv
class FlashCard:
    TITLE= ("Ariel", 10, "italic")
    TEXT = ("Ariel", 20, "bold")
    def __init__(self, window, timer, canvas):
        self.window = window
        self.timer = timer
        self.canvas = canvas
        self.data_dict = {}
        self.flash_cards()
        
    def flash_cards(self):
        data = read_csv("./data/french_words.csv")
        self.data_dict = {row.French:row.English for row in data.iterrows()}
    def time_countdown(self, new_time = 10):
        display_time = gmtime(new_time)
        time = strftime("%S", display_time)
        self.timer.config(text = f"{time}")
        if new_time > 0:
            if new_time == 10:
                self.display_front_card()
            self.window.after(1000,  self.time_countdown,new_time - 1)
    def display_front_card(self):
        #card
        #self.canvas.create_text(400, 150, text=f"{self.data_dict[0]}", font=self.FONT)
        keys = [key for key in self.data_dict.keys()]
        self.current_word = choice(keys)
        self.canvas.create_text(400, 150, text=f"FRENCH", font=self.TITLE)
        self.canvas.create_text(400, 253, text=f"{self.current_word}", font=self.TEXT)
        
        
    