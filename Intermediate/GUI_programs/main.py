import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#Button clicked function
def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


#Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=40, pady=40)

# Button 
button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


# New Button
button = tkinter.Button(text="New Button")
button.grid(column=2, row=0)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)






window.mainloop()

