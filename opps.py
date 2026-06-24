import sqlite3


class UserService:

    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()

    def create_user(self, name, email):

        self.cursor.execute(
            "INSERT INTO users(name,email) VALUES (?,?)",
            (name, email)
        )

        self.conn.commit()

    def get_users(self):

        self.cursor.execute(
            "SELECT * FROM users"
        )

        return self.cursor.fetchall()

    def update_user(self, id, email):

        self.cursor.execute(
            "UPDATE users SET email=? WHERE id=?",
            (email, id)
        )

        self.conn.commit()

    def delete_user(self, id):

        self.cursor.execute(
            "DELETE FROM users WHERE id=?",
            (id,)
        )

        self.conn.commit()