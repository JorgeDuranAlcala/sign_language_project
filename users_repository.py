import sqlite3


class UsersRepository:
    def __init__(self):
        self.db = sqlite3.connect('users.db')
        self.cursor = self.db.cursor()

    def insert(self, user):
        self.cursor.execute('INSERT INTO users (email, password, ) VALUES (?, ?)', (user['email'], user['password']))
        self.db.commit()

    def find(self, email, password):
        try:
            self.cursor.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email,password))
            user = self.cursor.fetchone()
            if user is None:
                return None
            else:
                return user
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return None

    def close(self):
        self.db.close()