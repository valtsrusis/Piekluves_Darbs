from tkinter import *
import tkinter as tk
import sqlite3
import test_map
from tkinter import messagebox
import ctypes

def search_records():
    lookup_records = search_entry.get()
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM electronic_products WHERE product_name = (?)", (lookup_records,))
    records = c.fetchall()
    for record in records:
        print(record[0], record[1], record[2])
    connection.commit()
    connection.close()

def query_database():
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT rowid, * FROM electronic_products")
    records = c.fetchall()
    for record in records:
        print(record[0], record[1], record[2])
    connection.commit()
    connection.close()

def new_tab():
    global search_entry, root
    root = Tk()
    root.title("Ventspils Starptautiska elektronika")
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    root.iconbitmap('Designer.ico')
    root.geometry("900x400")

    greeting_veikals = tk.Label(root, text="Lūdzu, ievadiet savu ievēlēto elektronisko sīkrīku!", fg='blue', font=('Aerial', 20, 'bold'))
    greeting_veikals.pack()

    search_frame = LabelFrame(root, text="Ievades rīks")
    search_frame.pack(padx=10, pady=10)
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)
    search_button = Button(root, text="Meklēt", command=search_records)
    search_button.pack(padx=20, pady=20)

    contact_button = Button(text="Kontakti", height=2, width=20, bd=3, relief="groove", command=lambda:contactProcess())
    contact_button.place(x=700, y=330)

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

def logoff_tab():
    logoff = tk.Label(root, text="Iziet no kontas", fg="blue", cursor='hand2', font=('underline'))
    logoff.pack(padx=30, pady=80)
    logoff.bind('<Button-1>', COMMAND)

def previous_window():
    root.destroy()
