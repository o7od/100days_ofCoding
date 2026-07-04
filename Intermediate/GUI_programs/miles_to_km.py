from tkinter import *

ENTRY_BG = "#437a75"


window = Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=300, height=200)


def convert(*args):
    km = args[0] * 1.609
    return round(km, 2)


def user_input():
    miles = int(entry.get())
    entry_result.config(state='normal')
    km = convert(miles)
    # deleting entry from previous trials
    entry_result.delete(0, END)
    entry_result.insert(0, km)
    entry_result.config(state='readonly')


# Label
big_label = Label(text="Miles to KM Converter", font=("Arial", 18, "bold"))
big_label.grid(column=1, row=0)


# Entry for miles
entry = Entry(width=5, bg=ENTRY_BG)
entry.focus()
entry.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Arial", 15, "normal"))
miles_label.grid(column=0, row=2)


# Button to convert
button = Button(text="Convert", command=user_input)
button.grid(column=1, row=1)

# entry widget to display result
entry_result = Entry(state='readonly', width=5, readonlybackground=ENTRY_BG, fg='white')
entry_result.grid(column=2, row=1)

km_label = Label(text="Kilometer", font=("Arial", 15, "normal"))
km_label.grid(column=2, row=2)





window.mainloop()
