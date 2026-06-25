#create pydantic schema

from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    name: str
    email: str

class UserResponse(User):
    id: int

#read values from object attributes.
    # model_config = ConfigDict(
    #     from_attributes=True
    # )