from tkinter import *

window = Tk()
time = 5

def show_time(time):
    print(f"{time} second")

    if time > 0:
        window.after(1000, show_time, time - 1)


show_time(5)

window.mainloop()