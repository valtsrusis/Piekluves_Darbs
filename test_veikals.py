from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox
import ctypes

def search_records():
    loopup_records = search_entry.get()


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

    search_frame = LabelFrame(root, text="Ievadāms rīks")
    search_frame.pack(padx=10, pady=10)
    search_entry = Entry(search_frame, font=("Helvetica", 18))
    search_entry.pack(pady=20, padx=20)
    search_button = Button(root, text="Meklēt", command=search_records)
    search_button.pack(padx=20, pady=20)