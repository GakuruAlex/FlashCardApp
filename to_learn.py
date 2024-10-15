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
        self.words_to_learn.update(self.timer.words_combo)
        if self.timer.check_if_to_save:
            self.save_words_to_learn()
    def save_words_to_learn(self,)->None:
        learn ={"French": self.words_to_learn.keys(), "English": self.words_to_learn.values()}
        data = DataFrame(learn)
        data.to_csv("./data/words_to_learn.csv", index=False)

    def create_button(self, file, run, row, col ,name):
        image = PhotoImage(file=file, master=self.window)
        button =Button(self.window,image=image, command=run)
        button.grid(row=row, column=col, )
        button.image = image

        setattr(self, name, button)
    def right_button(self):
        pass
    def got_wrong(self,):
        self.create_button(name=self.wrong,file="/home/aleyg/projects/Python/100DaysOfCode/DayThirty/FlashCardApp/images/wrong.png", run= self.add_words_to_learn, row=2, col=0)
    def got_right(self,):
        self.create_button(name=self.right,file="/home/aleyg/projects/Python/100DaysOfCode/DayThirty/FlashCardApp/images/right.png", run = self.right_button , row= 2, col= 1)