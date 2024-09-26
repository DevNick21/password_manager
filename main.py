from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)
    messagebox.showinfo(title="Copied to clipboard",
                        message="Your password has been copied to the clipboard")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_data = website_entry.get().title()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showwarning(
            title="Oops", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading Old data
                data = json.load(data_file)
        except FileNotFoundError:
            pass
        else:
            # Updating old data with new data
            data.update(new_data)
        finally:
            with open("data.json", mode="w") as data_file:
                # saving updated data
                json.dump(new_data, data_file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website_data = website_entry.get().title()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(
            title="No Data file", message="No Data File Found⚠️\nPlease add details before you search")
    else:
        # try:
        #     data[website_data]
        # except KeyError:
        #     messagebox.showerror(
        #         title="Not Found⚠️", message="Website not found in database, Try again")
        # else:
        #     messagebox.showinfo(
        #         title=f"{website_data} Details", message=f"Your {website_data} details are: \nEmail: {data[website_data]['email']}\nPassword: {data[website_data]['password']}")
        if website_data in data:
            messagebox.showinfo(
                title=f"{website_data} Details", message=f"Your {website_data} details are: \nEmail: {data[website_data]['email']}\nPassword: {data[website_data]['password']}")
        else:
            messagebox.showerror(
                title="Not Found⚠️", message="Website not found in database, Try again")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text="Search", width=14, border=1,
                       borderwidth=0.5, command=find_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "iheanacho.ekene@hotmail.com")


password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)


generate_button = Button(text="Generate Password",
                         width=14, command=generate_password, border=1, borderwidth=0.5)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, command=save,
                    border=1, borderwidth=0.5)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
