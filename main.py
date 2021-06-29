from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data ={
        website:{
            "email":email,
            "password":password,
        }

    }
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Ooops" , message="Please make you haven't left any field empty.")
    else:
        try:
            with open("data.json","r") as data_file:
                #serialize/deserialize
                #write data
                #json.dump(new_data,data_file,indent=4)
                # read data
                #data=json.load(data_file)

                #update data
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
                 #updating old data
                data.update(new_data)
            with open(data,data_file,indent=4):
                 #saving updated data
                data.dump(data,data_file,indent=4
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window  = Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200 , height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#labels

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#Input box(entries)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"abc@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

#buttons

generat_password_button= Button(text="Generate Password",command=generate_password)
generat_password_button.grid(row=3,column=2)
add_button =Button(text="Add", width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
