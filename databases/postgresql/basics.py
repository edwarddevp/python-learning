import psycopg2


def connect_db():
    return psycopg2.connect(
        "dbname='python-test-db' user='postgres' password='123' host='localhost' port='5432'")


def create_table():
    connection = connect_db()
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (\
            id serial PRIMARY KEY, \
            item TEXT,\
            quantity INTEGER,\
            price REAL \
        )")
    connection.commit()
    connection.close()


def insert(item, quantity, price):
    connection = connect_db()
    cur = connection.cursor()
    # cur.execute(
    #     "INSERT INTO store (item, quantity, price) VALUES ('%s','%s','%s')" % (item, quantity, price)) not recommendable
    cur.execute(
        "INSERT INTO store (item, quantity, price) VALUES (%s,%s,%s)", (item, quantity, price))
    connection.commit()
    connection.close()


def view():
    connection = connect_db()
    cur = connection.cursor()
    cur.execute(
        "SELECT * FROM store")
    rows = cur.fetchall()
    connection.close()
    return rows


def delete(id):
    connection = connect_db()
    cur = connection.cursor()
    cur.execute(
        "DELETE FROM store where id = %s ", (id))
    connection.commit()
    connection.close()


def update(id, item, quantity, price=5):
    connection = connect_db()
    cur = connection.cursor()
    cur.execute(
        "UPDATE store set quantity = %s, price = %s, item = %s where id = %s", (quantity, price, item, id))
    connection.commit()
    connection.close()


create_table()
# insert("cookies", 55, 9.4)
delete("2")
# update(1, "Mouse", 50, 10.9)
print(view())
