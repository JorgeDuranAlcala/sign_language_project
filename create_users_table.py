import sqlite3

conn = sqlite3.connect('users.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS users (email TEXT,  password TEXT) ")
    conn.commit()
    c.close()
    conn.close()

create_table()