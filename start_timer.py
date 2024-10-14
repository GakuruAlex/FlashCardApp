from time import strftime,gmtime
from tkinter import Label, Canvas
from flash_card import FlashCard
class Timer():
    def __init__(self, window, canvas):
        self.BACKGROUND = "white"
        self.seconds = 10
        self.top_canvas = None
        self.window = window
        self.canvas = canvas
        self.TIMER_FONT = ("Serif", 20, "bold")
        self.flashcard = FlashCard(self.window, self.canvas)

    def timer_ui(self,):
        self.top_canvas = Canvas(self.window, width= 200, height= 100,bg=self.BACKGROUND)
        self.top_canvas.grid(row= 0, column= 2, pady= 5)
        self.text_id =self.top_canvas.create_text(100,50, text="00", font= self.TIMER_FONT)
    def start_timer(self):
        self.flashcard.display_front_card()
        self.run_timer(self.seconds)
    def run_timer(self, seconds):
        time = strftime("%S", gmtime(seconds))
        self.top_canvas.itemconfig(self.text_id,text=f"{time}")
        if seconds > 0:
            self.timer_id = self.window.after(1000, self.run_timer, seconds - 1)
        elif seconds == 0:
            self.flashcard.display_back_card()
            self.window.after(4000, self.check_for_cards)
    def check_for_cards(self):
        if len(self.flashcard.cards) > self.flashcard.counter:
                self.start_timer()
    def cancel_current(self):
        self.window.after_cancel(self.timer_id)
