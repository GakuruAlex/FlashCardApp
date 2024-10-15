from time import strftime,gmtime
from tkinter import  Canvas, Button
from flash_card import FlashCard
class Timer():
    def __init__(self, window, canvas, main_class):
        self.BACKGROUND = "white"
        self.seconds = 5
        self.window = window
        self.canvas = canvas
        self.words_combo = {}
        self.main_class = main_class
        self.top_canvas = None
        self.timer_id = None
        self.TIMER_FONT = ("Serif", 10, "bold")
        self.flashcard = FlashCard(self.window, self.canvas, main_class= self.main_class)
       

    def timer_ui(self,):
        button = Button(self.window, text="start", command=self.start_timer)
        button.grid(row=0, column=0,)
        self.top_canvas = Canvas(self.window, width= 50, height= 20,bg=self.BACKGROUND)
        self.top_canvas.grid(row= 0, column= 2,)
        self.text_id =self.top_canvas.create_text(25,10, text="00", font= self.TIMER_FONT)
    def start_timer(self):
        if self.flashcard.check_for_cards():
            self.words_combo =self.flashcard.get_card()
            self.flashcard.display_front_card()
            self.run_timer(self.seconds)
    def run_timer(self, seconds: int):
        time = strftime("%S", gmtime(seconds))
        self.top_canvas.itemconfig(self.text_id,text=f"{time}")
        if seconds > 0:
                self.timer_id = self.window.after(1000, self.run_timer, seconds - 1)
        else:
                self.flashcard.display_back_card()
                if self.flashcard.check_for_cards():
                    self.window.after(4000,self.start_timer)
    def cancel_current(self):
        self.window.after_cancel(self.timer_id)
        self.canvas.delete("all")
        self.start_timer()
    def check_if_to_save(self):
        return self.flashcard.counter == self.flashcard.length

