import tkinter as tk
from tkinter import messagebox
from tkinter import *
import test_datubaze
import test_map
import sqlite3
import hashlib
import ctypes

connection = sqlite3.connect('login.db')
c = connection.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS login_information  (
            id integer PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
    )""")
connection.commit()
#connection.close()    

root = tk.Tk()
root.title("Ventspils Starptautiska elektronika")

###Gara līnīju komanda, lai samainītu taskbar ikonu uz izvēlēto ikonas bildi.
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.iconbitmap('Designer.ico')
root.geometry("900x400")

greeting = tk.Label(root, text="Laipni lūdzam uz Ventspils Starptautiskā elektronikas veikalu!", fg='blue', font=('Aerial', 20, 'bold'))
greeting.pack()



"""
def fetch_db():
    connection = sqlite3.connect('login.db')
    c = connection.cursor()
    c.execute("SELECT * FROM products WHERE name='laptop'")
    all_products = c.fetchall()
    print(all_products[0])
    connection.close()
"""

username = tk.Label(root, text="Lietotājvārdu: ", font=('Times New Roman', 13))
username.place(x=310, y=100)
password = tk.Label(root, text="Parole: ", font=('Times New Roman', 13))
password.place(x=330, y=150)

usernamevalue = StringVar
passwordvalue = StringVar

username_entry = Entry(root, textvariable=usernamevalue, bd=2, relief="ridge")
username_entry.place(x=410, y=100)
password_entry = Entry(root, textvariable=passwordvalue, bd=2, relief="ridge", show='*')
password_entry.place(x=410, y=150)

contact_button = Button(text="Kontakti", height=2, width=20, bd=3, relief="groove", command=lambda:contactProcess())
contact_button.place(x=700, y=330)

registration_button = Button(text="Piereģistrēties", height=3, width=20, bd=6, relief="raised", command=lambda:registrationProcess())
registration_button.place(x=280, y=250)

registration_button = Button(text="Ielogoties", height=3, width=20, bd=6, relief="raised", command=lambda:loginProcess())
registration_button.place(x=460, y=250)

def registrationProcess():
    username = username_entry.get()
    password = password_entry.get()
    register_user(username, password)

def loginProcess():
    username = username_entry.get()
    password = password_entry.get()
    login_user(username, password)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user(username, password):
    hashed_password = hash_password(password)
    c.execute("SELECT * FROM login_information WHERE username = ? AND password = ?",
              (username, hashed_password))
    user = c.fetchone()
    if user:
        messagebox.showinfo("Veiksme", "Veiksmīga logošana!")
        test_datubaze.show_all()
        root.destroy()
    else:
        messagebox.showerror("Kļūda", "Nepareizi ievadīta lietotājvārds vai parole!")

def register_user(username, password):
    try:
        hashed_password = hash_password(password)
        c.execute("INSERT INTO login_information (username, password) VALUES (?,?)",
              (username, hashed_password))
        connection.commit()
        messagebox.showinfo("Veiksme", "Veiksmīga reģistrācija!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Kļūda", "Šis lietotājvārds ir jau izmantots!") 


def contactProcess():
    top = tk.Toplevel()
    top.geometry("900x600")
    top.title("Ventspils Starptautiska elektronika")
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    top.iconbitmap('Designer.ico')
    topButton = Button(top, text="CLOSE", command = top.destroy)
    topButton.pack()
    test_map.maps_function()

tk.mainloop()
