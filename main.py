import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD FINDER / SEARCH BUTTON ------------------------------- #

# except (KeyError, FileNotFoundError): -->  is valid for multiple errors


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            # Checking if the user's text entry matches an item in the json
            data = json.load(file)
        website_data = data[website]
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found.")
    except KeyError:
        messagebox.showinfo("Error", f"No details for {website} exist.")
    else:
        messagebox.showinfo(f"{website}", f"Email: {website_data["username"]}"
                                          f"\nPassword: {website_data["password"]}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += ([choice(letters) for _ in range(randint(8, 10))])
    password_list += ([choice(symbols) for _ in range(randint(2, 4))])
    password_list += ([choice(numbers) for _ in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_username = Label(text="Email/Username:")
label_username.grid(column=0, row=2)

label_password = Label(text="Password")
label_password.grid(column=0, row=3)

# Entries
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = Entry(width=52)
username_entry.insert(END, "joaquinnuc99@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
gen_pass_btn = Button(text="Generate Password", width=15, command=generate_password)
gen_pass_btn.grid(column=2, row=3)

add_password_btn = Button(text="Add", width=44, command=save_data)
add_password_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(column=2, row=1)

window.mainloop()
