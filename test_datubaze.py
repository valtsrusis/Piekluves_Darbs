import sqlite3


#Query the DB and return all records
def show_all():
    connection = sqlite3.connect('login.db')

    c = connection.cursor()

    c.execute("SELECT * FROM login_information")
    items = c.fetchall()

    for item in items:
        print(item[0], item[1], item[2])
    
    connection.commit()

    connection.close()


def add_one(id,username,password):
    connection = sqlite3.connect('login.db')
    c = connection.cursor()
    c.execute("INSERT INTO login_information VALUES (?,?)", (id,username,password))
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
#c.execute("UPDATE sqlite_sequence SET seq = 0 WHERE username = 'login_information'")
#connection.commit()
#connection.close()


#c.execute("""CREATE TABLE IF NOT EXISTS login_information  (
#            id integer PRIMARY KEY AUTOINCREMENT,
#            username TEXT UNIQUE,
#            password TEXT
#    )""")
#
#connection.commit()
#connection.close()

#c.execute("INSERT INTO login_information VALUES ('1', 'Jānis', 'Bulgerts', 'janis.bulgerts@gmail.com', 'lielais')")
#c.execute("INSERT INTO login_information VALUES ('2', 'Jēkabs', 'Origs', 'jekabs.origs@gmail.com', 'lielie')")





connection = sqlite3.connect('products.db')
c = connection.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS electronic_products  (
            product_name TEXT,
            price REAL,
            currency TEXT
    )""")

#data = [['Datoru pele', '50.99', '€'], ['Monitors', '100', '€'], ['Tastatūra', '59.99', '€'], ['Video karte', '340.99', '€'], ['Personālais dators', '1240.99', '€']]

'''
for record in data:
    c.execute("INSERT INTO electronic_products VALUES (:product_name, :price, :currency)", 
        {
        'product_name': record[0],
        'price': record[1],
        'currency': record[2]
        }      
              
        )

connection.commit()
connection.close()

'''
'''
def query_database():
    connection = sqlite3.connect('products.db')
    c = connection.cursor()
    c.execute("SELECT * FROM electronic_products")
    # c.execute("SELECT rowid, * FROM electronic_products where product_name LIKE '%dato%'")
    records = c.fetchall()
    print(records)
    connection.commit()
    connection.close()

'''
#query_database()

#c.execute("INSERT INTO electronic_products VALUES ('Datoru pele', '50.99', '€')")
#c.execute("INSERT INTO electronic_products VALUES ('Monitors', '100', '€')")
#c.execute("INSERT INTO electronic_products VALUES ('Tastatūra', '59.99', '€')")
#c.execute("INSERT INTO electronic_products VALUES ('Video karte', '340.99', '€')")
#c.execute("INSERT INTO electronic_products VALUES ('Personālais dators', '1240.99', '€')")

#c.execute("SELECT * FROM electronic_products")
#products = c.fetchall()
#for item in products:
#    print(item[0], item[1], item[2])

#connection.commit()
#connection.close()

def convert_image():
    filename = "pele_1.png"
    with open(filename, 'rb') as file:
        photo = file.read()
    return photo
