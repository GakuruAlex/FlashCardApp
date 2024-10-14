from flash_card import FlashCard
from ui import UI
from start_timer import Timer
from to_learn import ToLearn
def main():
    ui = UI()
    window = ui.get_window_and_canvas()["window"]
    canvas = ui.get_window_and_canvas()["canvas"]
    flashcard = FlashCard(window=window, canvas=canvas)
    timer = Timer(window=window, canvas=canvas)
    to_learn = ToLearn(window=window, canvas=canvas)
    ui.start()
if __name__ == "__main__":
    main()