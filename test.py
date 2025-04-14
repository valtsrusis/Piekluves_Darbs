import tkinter as tk
from tkinter import *
import test_datubaze
import sqlite3
import hashlib
import ctypes

connection = sqlite3.connect('login.db')
c = connection.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS login_information  (
            id integer PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            surname TEXT,
            email TEXT,
            password TEXT
    )""")
connection.commit()
#connection.close() 

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()



root = tk.Tk()
root.title("Ventspils Starptautiskā elektronika")

###Gara līnīju komanda, lai samainītu taskbar ikonu uz izvēlēto ikonas bildi.
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
root.iconbitmap('Designer.ico')
root.geometry("900x600")

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

username = tk.Label(root, text="Vārds: ", font=('Times New Roman', 13))
username.place(x=330, y=100)
surname = tk.Label(root, text="Uzvārds: ", font=('Times New Roman', 13))
surname.place(x=330, y=150)
email = tk.Label(root, text="E-pasts: ", font=('Times New Roman', 13))
email.place(x=330, y=200)
password = tk.Label(root, text="Parole: ", font=('Times New Roman', 13))
password.place(x=330, y=250)

usernamevalue = StringVar
surnamevalue = StringVar
emailvalue = StringVar
passwordvalue = StringVar

username_entry = Entry(root, textvariable=usernamevalue, bd=2, relief="ridge")
username_entry.place(x=430, y=100)
surname_entry = Entry(root, textvariable=surnamevalue, bd=2, relief="ridge")
surname_entry.place(x=430, y=150)
email_entry = Entry(root, textvariable=emailvalue, bd=2, relief="ridge")
email_entry.place(x=430, y=200)
password_entry = Entry(root, textvariable=passwordvalue, bd=2, relief="ridge", show='*')
password_entry.place(x=430, y=250)

contact_button = Button(text="Kontakti", height=2, width=20, bd=3, relief="groove")
contact_button.place(x=700, y=500)

registration_button = Button(text="Piereģistrēties", height=3, width=20, bd=6, relief="raised", command=lambda:registrationProcess())
registration_button.place(x=380, y=350)

def registrationProcess():
    connection = sqlite3.connect('login.db')
    c = connection.cursor()

    insert_user_data = """INSERT INTO login_information(username, surname, email, password)
                        VALUES (?,?,?,?)"""
    
    user_data = (username_entry.get(),
                 surname_entry.get(),
                 email_entry.get(),
                 password_entry.get())
    #register_user(username, password)
    
    c.execute(insert_user_data, user_data)
    connection.commit()
    test_datubaze.show_all()
    connection.close()


#def contactProcess():


tk.mainloop()
