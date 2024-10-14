from pandas import DataFrame
from start_timer import Timer
from flash_card import FlashCard
from tkinter import Button, PhotoImage
class ToLearn:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.flashcard = FlashCard(window=self.window, canvas=self.canvas)
        self.timer = Timer(window=self.window, canvas=self.canvas)
        self.words_to_learn = {}
        self.right = "right"
        self.wrong= "wrong"
        self.got_right()
        self.got_wrong()

    def add_words_to_learn(self, new_set)->None:
        self.words_to_learn.update(new_set)
    def save_words_to_learn(self,)->None:
        data = DataFrame({"French": self.words_to_learn.keys(), "English": self.words_to_learn.values()})
        data.to_csv("./data/words_to_learn.csv")
    def pop_recent_word_combo(self):
        word_combo =self.flashcard.cards.pop(self.flashcard.french)
        self.add_words_to_learn(word_combo)

    def create_button(self, file, run, row, col ,name):
        image = PhotoImage(file=file, master=self.window)
        button =Button(self.window,image=image, command=run)
        button.grid(row=row, column=col, )
        button.image = image

        setattr(self, name, button)
    def got_wrong(self,):
        self.create_button(name=self.wrong,file="/home/aleyg/projects/Python/100DaysOfCode/DayThirty/FlashCardApp/images/wrong.png", run= self.pop_recent_word_combo, row=2, col=0)
    def got_right(self,):
        self.create_button(name=self.right,file="/home/aleyg/projects/Python/100DaysOfCode/DayThirty/FlashCardApp/images/right.png", run = self.timer.cancel_current , row= 2, col= 1)