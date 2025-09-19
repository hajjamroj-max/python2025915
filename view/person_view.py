from tkinter import *
import tkinter.messagebox as msg
from tools.validation import *
from data_access.database_manager import  save_user

def save_click():
    try:
        username_validator(username.get())
        password_validator(password.get())
        nickname_validator(nickname.get())
        save_user(username.get(),password.get(),nickname.get(),lock.get())
        msg.showinfo("Save", "Person saved")
    except Exception as e:
        msg.showerror("Error", f"{e}")


window = Tk()

window.title("user Profile")
window.geometry("270x300")

# Userame
username = StringVar()
Label(window, text="Username").place(x=20, y=20)
Entry(window, textvariable=username).place(x=100, y=20)

# password
password = StringVar()
Label(window, text="Password").place(x=20, y=60)
Entry(window, textvariable=password).place(x=100, y=60)

# nickname
nickname = StringVar()
Label(window, text="nickname").place(x=20, y=100)
Entry(window, textvariable=nickname).place(x=100, y=100)

# lock
lock = BooleanVar(value=True)
Label(window, text="Lock").place(x=20, y=200)
Checkbutton(window, variable=lock).place(x=100, y=200)


Button(window, text="Save", width=15, command=save_click).place(x=70, y=240)

window.mainloop()
