from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ('Arial', 10, 'normal')
BG = 'white'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for char in range(randint(8,10))]
    pw_symbols = [choice(symbols) for symbol in range(randint(2,4))]
    pw_numbers = [choice(numbers) for num in range(randint(2,4))]

    password_list = pw_letters + pw_symbols + pw_numbers
    shuffle(password_list)
    password = "".join(password_list)
    input_pw.insert(0, password)
    pyperclip.copy(password) # add new password to clipboard
    messagebox.showinfo(title= 'Your password is ready!', message= 'Your new randomly generated password is ready and has been added to the clipboard! You can now paste it.')

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_website = input_website.get()
    new_username = input_username.get()
    new_pw = input_pw.get()
    # alert user if they left something blank, ends function if they did so nothing is saved
    if len(new_website) ==0 or len(new_username)==0 or len(new_pw) == 0:
        messagebox.showinfo(title= 'Forgetting something?', message = 'Whoops looks like you forgot to add some info\nMake sure all fields are filled!')
    else:
        # create a pop-up window and ask user to check info; if they cancel, is_okay is set to False and the function ends
        is_okay = messagebox.askokcancel(title = new_website, message= f"Double check your new credentials:"
                                                             f"\nEmail/Username: {new_username} \nPassword: {new_pw} \nOkay to save?")
        if is_okay:
            with open("data.txt", mode='a') as file:
                file.write(f"{new_website} | {new_username} | {new_pw}\n")
            input_website.delete(0, END)
            #input_username.delete(0, END)
            input_pw.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg = BG)

# title = Label(text= "Timer",bg = YELLOW, fg= GREEN, font=(FONT_NAME, 40, 'bold'))
# title.grid(column=1, row =0)

# canvas w/ logo
canvas = Canvas(width = 200 , height = 200,  bg = BG, highlightthickness=0)
pwm_lock = PhotoImage(file = 'logo.png')
canvas.create_image(100, 95, image= pwm_lock)
# timer_text = canvas.create_text(100, 135, text = "00:00", fill = "white", font=(FONT_NAME, 30, 'bold'))
canvas.grid(column = 1, row = 0)

#labels
website = Label(text='Website:', font = FONT, bg = BG)
website.grid(column = 0, row =1)
username = Label(text='Email/Username:', font = FONT, bg = BG)
username.grid(column = 0, row =2)
password = Label(text='Password:', font = FONT, bg = BG)
password.grid(column = 0, row =3)

#buttons
generate = Button(text = 'Generate Password', command=generate_pw)
generate.grid(column = 2, row = 3)
add = Button(text = 'Add', width = 43, command=save)
add.grid(column = 1, row =4, columnspan = 2 )

#entries
input_website = Entry(width = 50)
input_website.grid(column = 1, row = 1, columnspan =2)
input_website.focus() # method calls the cursor to automatically begin here
input_username = Entry(width= 50)
input_username.grid(column = 1, row = 2, columnspan =2)
input_pw = Entry(width=32)
input_pw.grid(column = 1, row = 3)


window.mainloop()
