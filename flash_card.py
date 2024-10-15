from pandas import read_csv
from tkinter import PhotoImage
from random import choice
class FlashCard():
    TITLE_FONT = ("Serif", 40, "bold")
    CONTENT_FONT = ("Serif", 24, "normal")
    def __init__(self, window, canvas, main_class= False ):
        self.main_class = main_class
        self.window = window
        self.canvas = canvas
        self.french= None
        self.english= None
        self.counter = 1
        self.cards = {}
        self.words = {}
        self.length = 0
        self.all_cards =[]
        if self.main_class:
            self.get_data()
    def get_data(self) -> None:
        """_Read data from csv and process it into a dictionary of French , English words_
        """
        try:
                data = read_csv("./data/words_to_learn.csv")
        except FileNotFoundError:
                data = read_csv("./data/french_words.csv")
        finally:
                self.cards = {row.French : row.English for index, row in data.iterrows()}
    def get_card(self) -> dict:
        """_From the Cards dictionary, select a French word and the English counterpart and save the French word in a list to ensure the same word isn't drawn twice_

        Returns:
            dict: _A dictionary of French , English key-value pair of the current card being displayed_
        """
        self.french = choice(list(self.cards.keys()))
        if self.french in self.all_cards:
            self.get_card()
        else:
            self.all_cards.append(self.french)
        self.english = self.cards[self.french]
        return {self.french:self.english}

    def display_front_card(self)->None:
        """_Display the front card bearing the French word and increase counter by one_
        """
        self.counter += 1
        self.create_card(file="./images/card_front.png", location=(400, 100), text="FRENCH", text_content=self.french)
    def display_back_card(self):
        """_Display the back card rendering the English translation of the French word_
        """
        self.create_card(file= "./images/card_back.png",location=(400, 100),text="ENGLISH", text_content=self.english )
    def create_card(self, file,location, text, text_content)->None:
        """_Create a card_

        Args:
            file (_str_): _path of the image _
            location (_tuple_): _Where to place the image_
            text (_str_): _The text to display on card, whether a card shows the French word or English word_
            text_content (_str_): _The word to show on card, either French or English one_
        """
        self.canvas.delete("all")
        self.image = PhotoImage(file=file, master=self.canvas)
        x_cor, y_cor = location
        image_adjust = 180
        second_text_adjust= 100
        self.canvas.create_image(x_cor, y_cor + image_adjust, image= self.image)
        self.canvas.create_text(x_cor, y_cor, text=text, font=self.TITLE_FONT )
        self.canvas.create_text(x_cor, y_cor + second_text_adjust, text= text_content, font=self.CONTENT_FONT)
    def check_for_cards(self)->bool:
        """_Check whether there are more cards to display  and also get the length of the cards dict_

        Returns:
            _bool_: _True if there are more cards remaining else False_
        """
        self.length = len(self.cards)
        return self.length >= self.counter


