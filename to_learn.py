from pandas import DataFrame
from start_timer import Timer
from tkinter import Button, PhotoImage
class ToLearn:
    def __init__(self, window, canvas, main_class):
        self.window = window
        self.canvas = canvas
        self.main_class = main_class
        self.timer = Timer(window=self.window, canvas=self.canvas, main_class=self.main_class)
        self.words_to_learn = {}
        self.right = "right"
        self.wrong= "wrong"
        self.got_right()
        self.got_wrong()

    def add_words_to_learn(self)->None:
        """_Update the words to learn dictionary with the current french english pair _
        """
        self.words_to_learn.update(self.timer.words_combo)
        if self.timer.check_if_to_save:
            self.save_words_to_learn()
    def save_words_to_learn(self,)->None:
        """_Create a data frame of the words to learn dict and save to words to learn csv_
        """
        learn ={"French": self.words_to_learn.keys(), "English": self.words_to_learn.values()}
        data = DataFrame(learn)
        data.to_csv("./data/words_to_learn.csv", index=False)

    def create_button(self, file: str, run, row: int, col: int ,name: str)-> None:
        """_Create a button given some parameters_

        Args:
            file (_str_): _Path to image_
            run (_callback_): _Command to run when button is clicked_
            row (_int_): _Where to place on the grid_
            col (_int_): _Where to place on the grid_
            name (_str_): _name to identify button_
        """
        image = PhotoImage(file=file, master=self.window)
        button =Button(self.window,image=image, command=run)
        button.grid(row=row, column=col, )
        button.image = image

        setattr(self, name, button)
    def right_button(self):
        pass
    def got_wrong(self)-> None:
        """_Button with wrong icon _
        """
        self.create_button(name=self.wrong,file="./images/wrong.png", run= self.add_words_to_learn, row=2, col=0)
    def got_right(self)-> None:
        """_Button with right icon_
        """
        self.create_button(name=self.right,file="./images/right.png", run = self.right_button , row= 2, col= 1)