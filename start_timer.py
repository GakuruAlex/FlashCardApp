from time import strftime
from tkinter import Label, Canvas
from flash_card import FlashCard
class Timer():
    def __init__(self, window, canvas):
        super().__init__()
        self.BACKGROUND = "white"
        self.seconds = 10
        self.top_canvas = None
        self.window = window
        self.canvas = canvas
        flashcard = FlashCard(self.window, self.canvas)

    def timer(self,):
        self.top_canvas = Canvas(self.window, width= 200, height= 100,bg=self.BACKGROUND)
        self.top_canvas.grid(row= 0, column= 2, pady= 10)
