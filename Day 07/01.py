import sqlite3

conn = sqlite3.connect('OnlineBookstore.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE authors (
        author_id INTEGER PRIMARY KEY,
        author_name TEXT NOT NULL,
        country TEXT NOT NULL
    )
''')

c.execute('''
    CREATE TABLE books (
        book_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author_id INTEGER,
        price REAL NOT NULL,
        publication_year INTEGER NOT NULL,
        FOREIGN KEY(author_id) REFERENCES authors(author_id)
    )
''')

c.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        book_id INTEGER,
        customer_name TEXT NOT NULL,
        order_date TEXT NOT NULL,
        FOREIGN KEY(book_id) REFERENCES books(book_id)
    )
''')


c.execute("INSERT INTO authors VALUES (1, 'Author Name', 'Country')")
c.execute("INSERT INTO books VALUES (1, 'Book Title', 1, 19.99, 2023)")
c.execute("INSERT INTO orders VALUES (1, 1, 'Customer Name', '2023-12-10')")

conn.commit()

c.execute("SELECT * FROM authors")
print(c.fetchall())

c.execute("SELECT * FROM books")
print(c.fetchall())

c.execute("SELECT * FROM orders")
print(c.fetchall())

c.execute("ALTER TABLE books ADD COLUMN genre TEXT")
c.execute("ALTER TABLE orders ADD COLUMN quantity INTEGER")

c.execute('''
    SELECT books.title, authors.author_name
    FROM books
    INNER JOIN authors ON books.author_id = authors.author_id
''')
print(c.fetchall())

c.execute('''
    SELECT orders.order_id, books.title, orders.customer_name
    FROM orders
    INNER JOIN books ON orders.book_id = books.book_id
''')
print(c.fetchall())

conn.close()
