from random import choice
from time import strftime, gmtime
from pandas import  read_csv
from score_board import ScoreBoard
from time import sleep
class FlashCard:
    TITLE= ("Ariel", 10, "italic")
    TEXT = ("Ariel", 20, "bold")
    def __init__(self, window, timer, canvas, back_image,front_image):
        self.window = window
        self.timer = timer
        self.canvas = canvas
        self.front_image = front_image
        self.back_image = back_image
        self.data_dict = {}
        self.flash_cards()
        self.countdown = None
    def flash_cards(self):
        data = read_csv("./data/french_words.csv")
        self.data_dict = {row.French:row.English for index,row in data.iterrows()}
    def start_countdown(self):
        if self.countdown is not None:
            self.window.after_cancel(self.countdown)
        else:
            #Prompt user for name
            ScoreBoard(window=self.window)
        self.time_countdown(10)
        
    def time_countdown(self, new_time):
        display_time = gmtime(new_time)
        time = strftime("%S", display_time)
        self.timer.config(text = f"{time}")

        if new_time > 0:
            if new_time == 10:
                self.clear_content()
                self.display_front_card()
            self.countdown =self.window.after(1000,  self.time_countdown,new_time - 1)
        elif new_time == 0:
            self.display_back_card()
            
    def display_front_card(self):
        #front card
        self.canvas.create_image(400, 280, image=self.front_image)
        keys = [key for key in self.data_dict.keys()]
        self.french_word = choice(keys)
        self.canvas.create_text(400, 150, text=f"FRENCH", font=self.TITLE)
        self.canvas.create_text(400, 253, text=f"{self.french_word}", font=self.TEXT)
    def display_back_card(self):
        self.canvas.create_image(400, 280, image=self.back_image)
        self.english_word = self.data_dict[self.french_word]
        self.canvas.create_text(400, 150, text=f"ENGLISH", font=self.TITLE)
        self.canvas.create_text(400, 253, text=f"{self.english_word}", font=self.TEXT)
        del self.data_dict[self.french_word]

    def clear_content(self):
        self.canvas.delete("all")
    def run_all_cards(self):
        if len(self.data_dict) > 0:
            self.start_countdown()


