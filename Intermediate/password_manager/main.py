from tkinter import *
from tkinter import messagebox
from random_password import PasswordGenerator
import pyperclip
import json
WINDOW_COLOR = "#c0fff9"
CANVAS_COLOR = "#70ccc3"


# ---------------------------- SAVE PASSWORD ------------------------------- #
def show_warning():
    messagebox.showwarning(title="Password Manager", message="Do not leave any spaces blank!")

def save_password():
    website_name = website_entry.get()
    user_name = email_entry.get()
    password_name = password_entry.get()

    new_data = {
        website_name: {
            "email": user_name,
            "password": password_name,
        }
    }

    # checking if any of the entries are empty
    if len(website_name) == 0 or  len(password_name) == 0 or len(user_name) == 0:
        show_warning()
        return
    # double-checking to ensure everything is correct
    is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {user_name}\nPassword: {password_name} \nIs it okay to save?")

    if is_ok:
        try: # Handling the FileNotFoundError
            with open("password_data.json", "r") as data_file:
                # Read the data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("password_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update the data
            data.update(new_data)
            with open("password_data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            # Deleting entry inputs
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        

def search_website():
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0:
        show_warning()
        return
    # if there is a website to search for, we get the email and website entered
    website = website_entry.get()
    email = email_entry.get()
    try:
        with open("password_data.json", "r") as data_file:
            # Read the data
            content = json.load(data_file)
    except FileNotFoundError:
        print("There is no record of your password saved")
    except KeyError:
        messagebox.showinfo(title=website, message=f"No information found under this email or website!")
    else:
        correct_email = content[website]["email"]
        if email == correct_email:
            password = content[website]["password"]
            text = f"Here is your password for {website}: \n{email}\n{password}"
            messagebox.showinfo(title=website, message=text)
        else:
            messagebox.showinfo(title=website, message=f"No information found under this email or website!")



def generate_password():
    password_generator = PasswordGenerator()
    new_password = password_generator.make_password()
    password_entry.delete(0, END)
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

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
website_entry = Entry(bg="white", fg="black", insertbackground="black", highlightthickness=0, bd=1)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="e")

email_entry = Entry(width=35, bg="white", fg="black", insertbackground="black", highlightthickness=0, bd=1)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "ozodotammirzayev@gmail.com")

password_entry = Entry(bg="white", fg="black", insertbackground="black", highlightthickness=0, bd=1)
password_entry.grid(column=1, row=3, sticky="e")

# ############ Buttons ############
generate_password_button = Button(text="Generate Password", highlightbackground=WINDOW_COLOR, highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="n")

add_button = Button(text="Add", width=33, highlightbackground=WINDOW_COLOR, highlightthickness=0, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", highlightbackground=WINDOW_COLOR, width=10, command=search_website)
search_button.grid(column=2, row=1, sticky="w")



window.mainloop()