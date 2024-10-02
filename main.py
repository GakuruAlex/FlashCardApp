from tkinter import Tk, Button, Label, PhotoImage, Canvas
from flash_card import FlashCard
class Main:
    BACKGROUND_COLOR = "#B1DDC6"
    WINDOW_WIDTH = 900
    WINDOW_HEIGHT = 626
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 526
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
        front_image = PhotoImage(file="./images/card_front.png")
        back_image = PhotoImage(file="./images/card_back.png")
       
        #countdown
        flashcard = FlashCard(window=window, timer=timer, canvas=canvas,back_image=back_image, front_image=front_image)
        begin=Button(window, text="Begin", command=flashcard.time_countdown)
        begin.grid(row = 0, column=0)

        #buttons
        #right button and image
        right_image = PhotoImage(file="./images/right.png")
        right = Button(window, image=right_image, highlightthickness=0 )
        right.grid(row=2, column=0)
        #wrong button and image
        wrong_image = PhotoImage(file="./images/wrong.png")
        wrong = Button(window, image=wrong_image, highlightthickness= 0)
        wrong.grid(row=2, column=1)
        window.mainloop()
    def main(self):
        self.ui()

if __name__ == "__main__":
    main = Main()
    main.main()
