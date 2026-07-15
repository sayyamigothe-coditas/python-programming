from pydantic import BaseModel

from models import User


class UserCreate(BaseModel):

    name: str
    email: str
    password: str


class UserResponse(BaseModel):

    id: int
    name: str
    email: str
    role: str


def get_user_by_id(db, user_id):

    return db.query(User).filter(User.id == user_id).first()
