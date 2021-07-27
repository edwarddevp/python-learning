import sqlite3


def connect():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (\
            id INTEGER PRIMARY KEY AUTOINCREMENT,\
            title TEXT,\
            author TEXT,\
            year INTEGER,\
            isbn TEXT\
        )")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("INSERT into book (title, author, year, isbn) VALUES (?,?,?,?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("Select * from book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("Select * from book where title = ? or author = ? or year = ? or isbn = ?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("DELETE from book where id = ?", (id))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("bookstore.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? where id = ?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()
# insert("The Water", "jack Tablet", 1922, 123456789)
# update("3", "The Sun", "Jimmy Tablet", 1950, 987654321)
# delete("2")
# print(view())
# print(search(title="The Water", year=1920))
