from pandas import DataFrame
from start_timer import Timer
from flash_card import FlashCard
from tkinter import Button
class ToLearn:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.flashcard = FlashCard(window=self.window, canvas=self.canvas)
        self.timer = Timer(window=self.window, canvas=self.canvas)
        self.words_to_learn = {}

    def add_words_to_learn(self, new_set)->None:
        self.words_to_learn.update(new_set)
    def save_words_to_learn(self,)->None:
        data = DataFrame({"French": self.words_to_learn.keys(), "English": self.words_to_learn.values()})
        data.to_csv("./data/words_to_learn.csv")
