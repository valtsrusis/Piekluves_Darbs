import sqlite3


#Query the DB and return all records
def show_all():
    connection = sqlite3.connect('login.db')

    c = connection.cursor()

    c.execute("SELECT * FROM login_information")
    items = c.fetchall()

    for item in items:
        print(item)
    
    connection.commit()

    connection.close()


def add_one(id,first,last,email,password):
    connection = sqlite3.connect('login.db')
    c = connection.cursor()
    c.execute("INSERT INTO login_information VALUES (?,?,?,?,?)", (id,first,last,email,password))
    connection.commit()
    connection.close()


def delet_one(id):
    connection = sqlite3.connect('login.db')
    c = connection.cursor()
    c.execute("DELETE from login_information WHERE id = (?)", id)
    connection.commit()
    connection.close()


"""Lai sqlite_sequence neatkārto iepriekš izdzēstiem informāciju komanda formiem"""

#connection = sqlite3.connect('login.db')
#c = connection.cursor()
#c.execute("DELETE from login_information WHERE id = (26)")
#c.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'login_information'")
#connection.commit()
#connection.close()


#c.execute("""CREATE TABLE IF NOT EXISTS login_information  (
#            id integer PRIMARY KEY AUTOINCREMENT,
#            username TEXT UNIQUE,
#            surname TEXT,
#            email TEXT,
#            password TEXT
#    )""")
#
#connection.commit()
#connection.close()

#c.execute("INSERT INTO login_information VALUES ('1', 'Jānis', 'Bulgerts', 'janis.bulgerts@gmail.com', 'lielais')")
#c.execute("INSERT INTO login_information VALUES ('2', 'Jēkabs', 'Origs', 'jekabs.origs@gmail.com', 'lielie')")
