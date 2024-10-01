from tkinter import Tk, Button, Label, PhotoImage, Canvas

class Main:
    BACKGROUND_COLOR = "#B1DDC6"
    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 426
    def ui(self):
        # main window
        window = Tk()
        window.title("Flash Card App")
        window.config(background=self.BACKGROUND_COLOR, height=526, width=700, padx=50, pady= 50)
        #canvas for the cards
        canvas = Canvas(window, width=self.CANVAS_WIDTH, height = self.CANVAS_HEIGHT)
        canvas .grid(row=0, column=0, columnspan=2, pady=20)
        #buttons
        #right button and image
        right_image = PhotoImage(file="./images/right.png")
        right = Button(window, image=right_image )
        right.grid(row=1, column=0)
        #wrong button and image
        wrong_image = PhotoImage(file="./images/wrong.png")
        wrong = Button(window, image=wrong_image)
        wrong.grid(row=1, column=1)

        window.mainloop()
    def main(self):
        self.ui()

if __name__ == "__main__":
    main = Main()
    main.main()
