import re
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from authenticate_module import authenticate

def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_regex, email) is not None

def capture_face():
    print("Captured face!")

def sign_up(email, password):
    if not email or not password:
        messagebox.showwarning("Sign-up Failed", "Email and Password cannot be empty")
        return
    if not is_valid_email(email):
        messagebox.showwarning("Sign-up Failed", "Please enter a valid email")
        return

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sign-up Successful", "Account created successfully")

def login(email, password):
    if not email or not password:
        messagebox.showwarning("Login Failed", "Email and Password cannot be empty")
        return False

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    conn.close()
    return user is not None

def on_login():
    email = email_entry.get()
    password = password_entry.get()

    if login(email, password):
        login_frame.pack_forget()
        auth_frame.pack()
    else:
        messagebox.showwarning("Login Failed", "Incorrect email or password")

def on_sign_up():
    email = email_entry.get()
    password = password_entry.get()
    sign_up(email, password)

# Initialize SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)''')
conn.commit()
conn.close()

# Initialize Tkinter app
root = tk.Tk()
root.title("Face Authentication App")

login_frame = ttk.Frame(root, padding="10")
login_frame.pack()

auth_frame = ttk.Frame(root, padding="10")

# Login form
email_label = ttk.Label(login_frame, text="Email:")
email_label.grid(column=0, row=0)
email_entry = ttk.Entry(login_frame, width=30)
email_entry.grid(column=1, row=0)

password_label = ttk.Label(login_frame, text="Password:")
password_label.grid(column=0, row=1)
password_entry = ttk.Entry(login_frame, show="*", width=30)
password_entry.grid(column=1, row=1)

login_button = ttk.Button(login_frame, text="Login", command=on_login)
login_button.grid(column=1, row=2)

signup_button = ttk.Button(login_frame, text="Sign Up", command=on_sign_up)
signup_button.grid(column=1, row=3)

# Auth frame
auth_button = ttk.Button(auth_frame, text="Authenticate", command=authenticate)
auth_button.pack()

root.mainloop()
