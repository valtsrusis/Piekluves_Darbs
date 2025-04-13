import sqlite3

connection = sqlite3.connect('products.db')

c = connection.cursor()

#c.execute("""CREATE TABLE products  (
#            name TEXT,
#            price REAL
#    )""")

#c.execute("INSERT INTO products VALUES ('mouse', 60)")

#all_products = [('monitor  $', 90.99), ('laptop', 800.01), ('personal computer', 1000)]

#c.executemany("INSERT INTO products VALUES (?, ?)", all_products)

#connection.commit()
#connection.close()
