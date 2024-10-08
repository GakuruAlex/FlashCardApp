from random import choice
from time import strftime, gmtime
from pandas import  read_csv


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
        self.countdown_id = None
    def get_scorecard(self):
        from score_board import ScoreBoard
        return  ScoreBoard( window=self.window, timer=self.timer, canvas=self.canvas, back_image=self.back_image, front_image=self.front_image)
    def flash_cards(self):
        data = read_csv("./data/french_words.csv")
        self.data_dict = {row.French:row.English for index,row in data.iterrows()}
    def start_countdown(self, new_time = 10):
        if self.countdown_id:
            print("Countdown is not none")
            self.cancel_countdown()
        self.time_countdown(new_time)

    def time_countdown(self, new_time):
        display_time = gmtime(new_time)
        time = strftime("%S", display_time)
        self.timer.config(text=f"{time}")
        print(f"Countdown id in time_countdown: {self.countdown_id}")

        if new_time > 0 and len(self.data_dict) > 0:
            self.countdown_id = self.window.after(1000, self.time_countdown, new_time - 1)
            if new_time == 10:
                self.clear_content()
                self.display_front_card()
        elif new_time == 0:
            self.display_back_card()
            self.window.after(5000, self.time_countdown, 10)
            print(f"Countdown id when time is 0 is {self.countdown_id}")
            if len(self.data_dict)  == 0:
                self.cancel_countdown()
                scoreboard= self.get_scorecard()
                scoreboard.save_name_and_score()
            

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
        
    def cancel_countdown(self):
        print(f"Canceling previous countdown with id {self.countdown_id}")
        if self.countdown_id:
            self.window.after_cancel(self.countdown_id)
        self.timer.config(text="00")
