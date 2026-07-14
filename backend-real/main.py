from fastapi import FastAPI
import sqlite3
from pydantic import BaseModel

app = FastAPI()

connection = sqlite3.connect("users.db", check_same_thread=False)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

connection.commit()


@app.get("/")
def home():
    return "fast api started"


# like interface
class User(BaseModel):
    name: str
    email: str


@app.post("/users")
def create_user(user: User):
    cursor.execute("insert into users(name,email) values(?,?)", (user.name, user.email))
    connection.commit()
    return {"message": "created successfully"}


# get all users
@app.get("/users")
def getAllUsers():
    cursor.execute("select * from users")
    users = cursor.fetchall()
    connection.commit()

    return users


# get user by id
@app.get("/users/{user_id}")
def get_user(user_id: int):

    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))

    user = cursor.fetchone()

    return user


# update user
@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str):

    cursor.execute(
        """
        UPDATE users
        SET name = ?, email = ?
        WHERE id = ?
        """,
        (name, email, user_id),
    )

    connection.commit()

    return {"message": "User Updated Successfully"}


# delte the users
@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

    connection.commit()

    return {"message": "User Deleted Successfully"}
