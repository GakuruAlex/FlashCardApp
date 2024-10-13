from flash_card import FlashCard

from time import strftime
from tkinter import Label, Canvas
class Timer(FlashCard):
    def __init__(self, ):
        super().__init__()
        self.BACKGROUND = "white"
        self.seconds = 10
        self.top_canvas = None
        self.ui()
        self.display_front_card()
        self.timer()
        self.start()

    def timer(self,):
        self.top_canvas = Canvas(self.window, width= 200, height= 100,bg=self.BACKGROUND)
        self.top_canvas.grid(row= 0, column= 2, pady= 10)
    