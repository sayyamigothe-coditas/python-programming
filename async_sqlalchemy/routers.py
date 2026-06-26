from fastapi import Depends, FastAPI, HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from main import get_db
from models import User
from shemas import UserCreate, UserResponse

app = FastAPI()


# craete a user with asyncSQLalchamey
@app.post("/users", response_model=UserResponse)
async def createUser(data: UserCreate, db: AsyncSession = Depends(get_db)):

    new_user = User(name=data.name, email=data.email)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user


# get all users
@app.get("/users", response_model=list[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(User))

    users = result.scalars().all()

    return users


# get users by id
@app.get("/users/{user_id}", response_model=UserResponse)
async def getUser_byid(user_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(User).where(User.id == user_id))

    user = result.scalars().first()
    return user

#update user
@app.put('/users/{user_id}')
async def update_user(user_id:int,data:UserCreate,db:AsyncSession=Depends(get_db)):

   
    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user=result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Users not found"
        )
    user.name=data.name
    user.email=data.email

    await db.commit()
    await db.refresh(user)

    return user

#delete the user
@app.delete("/users/{user_id}")
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
):

    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalars().first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    await db.delete(user)

    await db.commit()

    return {
        "message": "User deleted successfully"
    }

#select is sued beacouse it is compactable with both syncronus and asycronous