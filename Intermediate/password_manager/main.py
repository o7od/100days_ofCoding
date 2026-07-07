from tkinter import *
from tkinter import messagebox
from random_password import PasswordGenerator
WINDOW_COLOR = "#c0fff9"
CANVAS_COLOR = "#70ccc3"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get().split()
    user_name = email_entry.get().split()
    password_name = password_entry.get()

    # checking if any of the entries are empty
    if not website_name or not user_name or not password_name:
        messagebox.showwarning(title="Password Manager", message="Do not leave any spaces blank!")
        return

    is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {user_name}\nPassword: {password_name} \nIs it okay to save?")
    if is_ok:
        # Deleting entry inputs
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        with open("password_data.txt", mode="a") as data_writer:
            data_writer.write("\n" + website_name + " | " + user_name + " | " + password_name)
    

def generate_password():
    password_generator = PasswordGenerator()
    new_password = password_generator.make_password()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg=WINDOW_COLOR, padx=50, pady=50)
frame = Frame(window)
frame.grid(column=1, row=3)


canvas = Canvas(window, width=200, height=200, bg=WINDOW_COLOR, highlightthickness=0, bd=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

######### LABELS  #########
website_label = Label(text="Website:", bg=WINDOW_COLOR, fg="black")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=WINDOW_COLOR, fg="black")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=WINDOW_COLOR, fg="black")
password_label.grid(column=0, row=3)


##### Entries  #####
website_entry = Entry(width=35, bg="white", fg="black", insertbackground="black", highlightthickness=0, bd=1)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35, bg="white", fg="black", insertbackground="black", highlightthickness=0, bd=1)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ozodotammirzayev@gmail.com")

password_entry = Entry(frame, width=17, bg="white", fg="black", highlightbackground=WINDOW_COLOR)
password_entry.grid(column=1, row=3)

# ############ Buttons ############
generate_password_button = Button(frame, text="Generate Password", highlightbackground=WINDOW_COLOR, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=32, highlightbackground=WINDOW_COLOR, highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()