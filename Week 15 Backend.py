import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS book (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                year INTEGER,
                isbn INTEGER
                genre TEXT
                )
            """)
    conn.commit()
    conn.close()

def insert(title, author, year, isbn, genre):
    conn = sqlite3.connect("books.db)")
    cur = conn.cursor()
    cur.execute("INSETS INTO book VALUES (NULL,?,?,?,?,?)", (title, author, year, isbn, genre))
    conn.commit()
    conn.close()

def view(): 
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn="", genre=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? OR genre=?",
                (title, author, year, isbn, genre))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn, genre):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=?, genre=? WHERE ID=?",
                (title, author, year, isbn, genre, id))
    conn.commit()
    conn.close()

connect()