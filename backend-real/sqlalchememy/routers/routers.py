#craete user

from fastapi import FastAPI, HTTPException
from schemas.schemas import UserResponse,User
from database.database import UserTable
from database.database import SessionLocal

app=FastAPI()


@app.post('/users',response_model=User)
def create_user(user:User):
    
    db=SessionLocal()

    new_user=UserTable(
        name=user.name,
        email=user.email
    )

    #add new user to db
    db.add(new_user)
    #perform the operation
    db.commit()
    #refresh
    db.refresh(new_user)

    return new_user

@app.get('/users/{user_id}',response_model=UserResponse)
def get_user(user_id:int):

    db=SessionLocal()

    user=db.query(UserTable).filter(UserTable.id==user_id).first()

    if not user:
        return HTTPException(
            status_code=404,
            detail='user not found'
        )

    return user

@app.put("/users/{user_id}",response_model=UserResponse)
def update_user(user_id:int,data:User):

    db=SessionLocal()

    updated_user=db.query(UserTable).filter(UserTable.id==user_id).first()

    if not updated_user:
        return HTTPException(status_code=404,detail="User not found")
    
    updated_user.name=data.name
    updated_user.email=data.email

    db.commit()
    db.refresh(updated_user)

    return updated_user

#delete user
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    db=SessionLocal()

    deletedUser=db.query(UserTable).filter(UserTable.id==user_id).first()

    if not deletedUser:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    db.delete(deletedUser)
    db.commit()

    return{
        "message" :"user deleted"
    }