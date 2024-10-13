from flash_card import FlashCard
from ui import UI
from start_timer import Timer
def main():
    ui = UI()
    window = ui.get_window_and_canvas()["window"]
    canvas = ui.get_window_and_canvas()["canvas"]
    flashcard = FlashCard(window=window, canvas=canvas)
    timer = Timer(window=window, canvas=canvas)
    timer.timer_ui()
    timer.start_timer()
    ui.start()
if __name__ == "__main__":
    main()