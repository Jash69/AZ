import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image
from DB import connection
import customtkinter as ctk
from customtkinter import *
from PIL import ImageTk, Image
from DB import connection
from tkinter import messagebox
from DBfuntions import add_user
import subprocess
import os
import bcrypt


login = CTk()
login.title("Login Page")
login.geometry("1300x700")
loginbg = ctk.CTkImage(Image.open("image2.png"), size=(1300, 700))
bg_label = ctk.CTkLabel(login, text="", corner_radius=5, image=loginbg)
bg_label.place(x=0, y=0)
login.resizable(False, False)




def authenticate(username, password):
    # Search for the user in the collection
    db = connection()
    Users = db["Users@aarogyazen"]
    user = Users.find_one({"username": username})

    if user:
        # Hash the provided password with the stored salt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), user['salt'])

        # Check if the hashed password matches the stored hashed password
        if hashed_password == user['hashed_password']:
            messagebox.showinfo("Success","Authentication successful")
           
            # login.destroy()
            # os.system('python test.py')
            return True
    messagebox.showerror("Error","Authentication unsuccessful")
    return False

def submit():
    username = username_txt.get()
    password = password_txt.get()

    authenticate(username, password)





username_txt = ctk.CTkEntry(login, border_width=1.5,
                            border_color="#94a8fe",
                            placeholder_text="Username", width=315, height=48, corner_radius=30,
                            bg_color="#ffffff", )
username_txt.place(x=135, y=205)


password_txt = ctk.CTkEntry(login, border_width=1.5, border_color="#94a8fe",
                            placeholder_text="Password", width=315, height=48, corner_radius=30,
                            bg_color="#ffffff", show='*')
password_txt.place(x=135, y=315)



nextbtn = ctk.CTkButton(login, border_width=1.5, border_color="#94a8fe", text="Login", width=100, height=30, corner_radius=30, bg_color="#ffffff", command=submit)
nextbtn.place(x=225, y=400)



login.mainloop()