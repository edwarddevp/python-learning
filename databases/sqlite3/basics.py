import sqlite3


def create_table():
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (\
            id INTEGER PRIMARY KEY AUTOINCREMENT, \
            item TEXT,\
            quantity INTEGER,\
            price REAL \
        )")
    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute(
        "INSERT INTO store (item, quantity, price) VALUES (?,?,?)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM store")
    rows = cur.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute(
        "DELETE FROM store where id = ? ", (id))
    connection.commit()
    connection.close()


def update(id, item, quantity, price=5):
    connection = sqlite3.connect('lite.db')
    cur = connection.cursor()
    cur.execute(
        "UPDATE store set quantity = ?, price = ?, item = ? where id = ?", (quantity, price, item, id))
    connection.commit()
    connection.close()


create_table()
insert("Tomato", 20, 3.6)
# delete("1")
update(1, "Tomato", 50, 10.9)
print(view())
