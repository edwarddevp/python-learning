import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                title TEXT,\
                author TEXT,\
                year INTEGER,\
                isbn TEXT\
            )")
        self.conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT into book (title, author, year, isbn) VALUES (?,?,?,?)",
                         (title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("Select * from book")
        return self.cur.fetchall()

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("Select * from book where title = ? or author = ? or year = ? or isbn = ?",
                         (title, author, year, isbn))
        return self.cur.fetchall()

    def delete(self, id):
        self.cur.execute("DELETE from book where id = ?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? where id = ?",
                         (title, author, year, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# connect()
# insert("The Water", "jack Tablet", 1922, 123456789)
# update("3", "The Sun", "Jimmy Tablet", 1950, 987654321)
# delete("2")
# print(view())
# print(search(title="The Water", year=1920))
