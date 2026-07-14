from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/sayyami")
def sayyami():
    return {"syyami is my name"}


@app.post("/")
def getMethod():
    return [{"id": 1, "name": "John"}, {"id": 2, "name": "Alice"}]

# path parameters
class User(BaseModel):
    name: str
    email: str

@app.get("/users/{user.id}")
def get_user_byid(user_id: int):
    return {"id": user_id}

@app.post("/users")
def create_user(user: User):
    return {"message": "User Created", "data": user}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"id": user.id, "updated_data": user}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}
