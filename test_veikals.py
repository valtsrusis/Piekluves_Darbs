from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
import test_map
import ctypes

def search_records():
    lookup_records = search_entry.get()
    query_database()
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM electronic_products WHERE product_name LIKE ?", (lookup_records,))
    records = c.fetchall()
    for record in records:
        print(record[0], record[1], record[2])
    connection.commit()
    connection.close()

def new_tab():
    global search_entry, root, table
    root = Tk()
    root.title("Ventspils Starptautiska elektronika")
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    root.iconbitmap('Designer.ico')
    root.geometry("900x700")

    greeting_veikals = tk.Label(root, text="Lūdzu, ievadiet savu ievēlēto elektronisko sīkrīku!", fg='blue', font=('Aerial', 20, 'bold'))
    greeting_veikals.pack()

    search_frame = LabelFrame(root, text="Ievades rīks")
    search_frame.pack(padx=10, pady=10)
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)
    search_button = Button(root, text="Meklēt", command=search_records)
    search_button.pack(padx=20, pady=20)

    table = ttk.Treeview(root, columns=('Prece', 'Cena', '€'), show='headings')
    table.heading('Prece', text='Pieejamās preces')
    table.heading('Cena', text='Cena')
    table.heading('€', text='Valūta')
    table.pack(padx=50, pady=50, fill='both', expand=True)

    query_database()

    contact_button = Button(text="Kontakti", height=2, width=20, bd=3, relief="groove", command=lambda:contactProcess())
    contact_button.place(x=700, y=630)

def query_database():
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM electronic_products")
    # c.execute("SELECT rowid, * FROM electronic_products where product_name LIKE '%dato%'")
    records = c.fetchall()
    global count
    count = 0
    for record in records:
        if count % 2 == 0:
            table.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
        else:
            table.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
        count += 1
    connection.commit()
    connection.close()

def remove_all():
    for record in records():
        records.delete(record)

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
    logoff.place(x=400, y=220)
    logoff.bind('<Button-1>', previous_window)

def previous_window(event):
    event.char
    root.destroy()

#query_database()