import sqlite3

connection = sqlite3.connect('students.db')

c = connection.cursor()

c.execute("""CREATE TABLE students  (
            name TEXT,
            age INTEGER,
            height REAL
    )""")

connection.commit()
connection.close()
