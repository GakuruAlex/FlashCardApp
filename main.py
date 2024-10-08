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
        self.right_image = None
        self.wrong_image = None
    def ui(self):
        # main window
        window = Tk()
       
        

        window.title("Flash Card App")
        window.config(background=self.BACKGROUND_COLOR, height=self.WINDOW_HEIGHT,width=self.WINDOW_WIDTH , padx=50, pady= 20)
        #timer
        timer = Label(window, text="00",)
        timer.grid(row=0, column=1,)
        #canvas for the cards
        canvas = Canvas(window, width=self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT, bg=self.BACKGROUND_COLOR)
        canvas .grid(row=1, column=0, columnspan=2, )
        #background front 
        self.front_image = PhotoImage(file="./images/card_front.png")
        self.back_image = PhotoImage(file="./images/card_back.png")
       
        #countdown
        flashcard = FlashCard(window=window, timer=timer, canvas=canvas,back_image=self.back_image, front_image=self.front_image)
        begin=Button(window, text="Begin", command=flashcard.run_all_cards)
        begin.grid(row = 0, column=0)
        
        #buttons
        #right button and image
        scorecard = flashcard.get_scorecard()
        self.right_image = PhotoImage(file="./images/right.png")
        right = Button(window, image=self.right_image, highlightthickness=0 , command=scorecard.increase_score)
        right.grid(row=2, column=0)
        #wrong button and image
        self.wrong_image = PhotoImage(file="./images/wrong.png")
        wrong = Button(window, image=self.wrong_image, highlightthickness= 0, command=scorecard.got_wrong)
        wrong.grid(row=2, column=1)
        window.mainloop()
    def main(self):
        self.ui()

if __name__ == "__main__":
    main = Main()
    main.main()
