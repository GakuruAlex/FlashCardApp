from tkinter import Tk, Button, Label, PhotoImage, Canvas
from flash_card import FlashCard

class Main:
    BACKGROUND_COLOR = "#B1DDC6"
    WINDOW_WIDTH = 900
    WINDOW_HEIGHT = 626
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 526
    def __init__(self):
        # Store image references as instance variables
        self.front_image = None
        self.back_image = None
        self.canvas = None
        self.window = None
    def ui(self):
        # main window
        self.window = Tk()

        self.window.title("Flash Card App")
        self.window.config(background=self.BACKGROUND_COLOR, height=self.WINDOW_HEIGHT,width=self.WINDOW_WIDTH , padx=50, pady= 20)
        #canvas for the cards
        canvas = Canvas(self.window, width=self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT, bg=self.BACKGROUND_COLOR)
        canvas .grid(row=1, column=0, columnspan=2, )

        self.window.mainloop()
    def main(self):
        self.ui()


