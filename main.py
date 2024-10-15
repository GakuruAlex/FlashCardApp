from ui import UI
from to_learn import ToLearn
def main():
    ui = UI()
    window = ui.get_window_and_canvas()["window"]
    canvas = ui.get_window_and_canvas()["canvas"]
    to_learn = ToLearn(window=window, canvas=canvas, main_class= True)
    to_learn.timer.timer_ui()
    ui.start()
if __name__ == "__main__":
    main()