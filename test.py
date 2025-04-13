import tkinter as tk
import sqlite3
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()

def fetch_db():
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM products WHERE name='laptop'")
    all_products = c.fetchall()
    print(all_products[0])
    connection.close()

def load_frame2():
    poga.tkraise()
    fetch_db()

poga = tk.Button(text="poga", width=25, height=25, bg='magenta', fg='red', command=lambda:load_frame2())
poga.pack()



tk.mainloop()
