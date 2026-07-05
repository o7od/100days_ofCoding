from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BUTTON_COLOR = "#F99D38"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
XCOR = 150
YCOR = 125


# ---------------------------- TIMER RESET ------------------------------- # 
def reset(canvas):
    canvas.itemconfig(prev_time, text="00:00") 
    stop_event()
    

def stop_event():
    global timer_id
    if timer_id is not None:
        window.after_cancel(timer_id)

def start_event():
    stop_event()
    canvas.itemconfig(prev_time, text="00:00") 
    session_period()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(minutes, seconds):
    global timer_id, time_status, session_count, checkmarks
    #Displaying the time
    current_time = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(prev_time, text=current_time)

    # this is when the time ends
    if minutes == 0 and seconds == 0:
        if time_status == "work":
            session_period()
        elif time_status == "break":
            session_count -= 1
            break_period()
            checkmarks += "✔"
            check_mark.config(text=checkmarks)
        elif time_status == "longer_break":
            long_break_period()
        else:
            stop_event()
        return
    # decreasing the seconds
    elif seconds > 0:
        timer_id = window.after(1000, count_down, minutes, seconds - 1)
    # decreasing when the seconds finish
    elif seconds == 0 and minutes != 0:
        seconds = 59
        minutes -= 1
        timer_id = window.after(1000, count_down, minutes, seconds)


## session_specific time
def session_period():
    global time_status
    headline_label.config(text="Work")
    count_down(WORK_MIN, 0)
    time_status = "break"


## short break time
def break_period():
    global session_count, time_status
    headline_label.config(text="Break", fg=PINK)
    if session_count > 0:
        time_status = "work"
    else:
        time_status = "longer_break"
    print(session_count, time_status)
    count_down(SHORT_BREAK_MIN, 0)



## long break time
def long_break_period():
    global time_status
    headline_label.config(text="Long Break", fg=RED)
    count_down(LONG_BREAK_MIN, 0)
    time_status = "over"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.minsize(width=600, height=500)
window.config(bg=YELLOW)

# this variable controls the window events
timer_id = None
session_count = 5
time_status = None
checkmarks = ""



# HEADLINE Label
headline_label= Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
headline_label.place(relx=0.5, rely=0.15, anchor="center")


# Loading the image
canvas = Canvas(window, width=300, height=250, bg=YELLOW, bd=0, highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor="center")
photo = PhotoImage(file="tomato.png")
canvas.create_image(XCOR, YCOR, anchor="center", image=photo)
prev_time = canvas.create_text(XCOR, YCOR, text=f"{WORK_MIN}:00", font=(FONT_NAME, 50, "bold"), fill="white")

# START button
start_button = Button(text="Start", bg="lightblue", highlightbackground=YELLOW, command=start_event)
start_button.place(relx=0.2, rely=0.8, anchor="w")

# Reset Button
reset_button = Button(text="Reset", bg="lightblue", highlightbackground=YELLOW, command=lambda: reset(canvas))
reset_button.place(relx=0.8, rely=0.8, anchor="e")

# Checkmark
check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.place(relx=0.4, rely=0.8)
# check_mark.config(text="✔")


window.mainloop()
