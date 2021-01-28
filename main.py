import random
from tkinter import *
from tkinter import messagebox
import json
import pyperclip as pc

# ---------------------------- Tool Kits ------------------------------- #

# Colors
GREY = "grey15"
ORANGE = "orange"
DARK_GREY = "grey30"
WHITE = "white"

# Font
FONT_TITLE = "Lobster"
FONTS = "Sen"
clicked = False

# ---------------------------- Password generator ------------------------------- #


def generate_password():
    clicked = True
    if clicked:
        generate_button.config(state="disabled")
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    global password
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password = "".join(password_list)
    password_field.insert(0, password)
    pc.copy(password)


# ---------------------------- Save Mechanism ------------------------------- #

def save_data():
    website_data = web_input.get()
    mail_id = mail_input.get()
    password_data = password_field.get()

    # Creating json data framework
    new_data = {
        website_data: {
            "mail_id": mail_id,
            "password": password_data
        }
    }

    if (len(website_data) == 0) or (len(mail_id) == 0) or (len(password_data) == 0):
        messagebox.showwarning(title="Blank Fields",
                               message="Please don't leave any fields blank")
    else:
        try:
            with open("Encro Password Manager\\Data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Encro Password Manager\\Data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("Encro Password Manager\\Data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            is_ok = messagebox.askokcancel(
                title=website_data, message=f"Details Entered \nMail_Id: {mail_id}\nPassword: {password_data}\nIs it ok to save?")
            if is_ok:
                web_input.delete(0, END)
                password_field.delete(0, END)
                generate_button.config(state="normal")
                messagebox.showinfo(title="Success", message="Password Saved")

# ---------------------------- Search Mechanism ------------------------------- #
# ? Creating Search Mechanism


def search_field():
    website_data = web_input.get()
    try:
        with open("Encro Password Manager\\Data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(
            title="error", message="File doesn't exist please add some data.....!")
    else:
        if website_data in data:
            search_data = data[website_data]
            search_mail = search_data['mail_id']
            search_password = search_data['password']
            messagebox.showinfo(
                title=f"{website_data}", message=f"Saved Data Is:\nMail_id: {search_mail}\nPassword: {search_password}")
        else:
            messagebox.showerror(
                title="error", message="Data Doesn't Exists Please Add One")


# ---------------------------- UI setup ------------------------------- #
# ? Creating a window
window = Tk()
window.title("Encro")
window.resizable(width=False, height=False)
window.config(padx=40, pady=40, bg=GREY)

# Creating the canvas
canvas = Canvas(width=200, height=100, bg=GREY, highlightthickness=0)

# get the image
logo_img = PhotoImage(file="Encro Password Manager\\Logo.png")

#  render the image
canvas.create_image(105, 50, image=logo_img)
canvas.grid(row=0, column=1)

# Button Border
# button_border = Frame(Tk, bd=0, highlightbackground=ORANGE,
#                       highlightcolor=ORANGE, highlightthickness=4)


# get the website
web_title = Label(text="Website:", bg=GREY, font=(FONTS, 12), fg=WHITE)
web_title.grid(row=1, column=0)
web_input = Entry(width=35, font=(FONTS, 8))
web_input.focus()
web_input.config(bg="grey20", fg=ORANGE, border=0,
                 highlightthickness=1, highlightbackground=DARK_GREY, highlightcolor=ORANGE, insertbackground=ORANGE, justify="center")
web_input.grid(row=1, column=1)
search_button = Button(text="Search", font=(FONTS, 8))
search_button.config(bg=GREY, fg=ORANGE,
                     activebackground=DARK_GREY, activeforeground=ORANGE, command=search_field)
search_button.grid(row=1, column=2)

# Email ID
mail_title = Label(text="Email ID:", bg=GREY, font=(FONTS, 12), fg=WHITE)
mail_title.grid(row=2, column=0)
mail_input = Entry(width=45, font=(FONTS, 8))
mail_input.insert(0, "your_id@gmail.com")
mail_input.config(bg="grey20", fg=ORANGE, border=0,
                  highlightthickness=1, highlightbackground=DARK_GREY, highlightcolor=ORANGE, insertbackground=ORANGE, justify="center")
mail_input.grid(row=2, column=1, columnspan=2)

# Password Inputs
password_title = Label(text="Password:", bg=GREY, fg=WHITE, font=(FONTS, 12))
password_title.grid(row=3, column=0)
password_field = Entry(width=33, font=(FONTS, 8))
password_field.config(bg="grey20", fg=ORANGE, border=0,
                      highlightthickness=1, highlightbackground=DARK_GREY, highlightcolor=ORANGE, insertbackground=ORANGE, justify="center")
password_field.grid(row=3, column=1)
generate_button = Button(text="Generate", font=(FONTS, 8))
generate_button.config(bg=GREY, fg=ORANGE,
                       activebackground=DARK_GREY, activeforeground=ORANGE, command=generate_password)
generate_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", font=(FONTS, 8))
add_button.config(width=37,  bg=GREY, fg=ORANGE,
                  activebackground=DARK_GREY, activeforeground=ORANGE, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
