from tkinter import Tk, Canvas, PhotoImage
from flash_card import FlashCard
class UI:
    def __init__(self):
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.WINDOW_WIDTH = 900
        self.WINDOW_HEIGHT = 626
        self.CANVAS_WIDTH = 800
        self.CANVAS_HEIGHT = 526
        self.front_image = None
        self.back_image = None

    def ui(self):
        # main window
        self.window = Tk()
        self.window.title("Flash Card App")
        self.window.config(background=self.BACKGROUND_COLOR, height=self.WINDOW_HEIGHT,width=self.WINDOW_WIDTH , padx=50, pady= 20)
        #canvas for the cards
        self.canvas = Canvas(width=self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT, bg=self.BACKGROUND_COLOR)
        self.canvas.grid(row=0, column=0, columnspan=2, pady=20)

        flashcard = FlashCard(window=self.window, canvas = self.canvas)
        self.window.mainloop()



