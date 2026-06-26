from fastapi import Depends, FastAPI


from database import get_db
from repository.user_repository import UserRepository
from schemas import UserCreate, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


# create user
@app.post("/users")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):

    repository = UserRepository(db)
    return await repository.create(user)


# get all
@app.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):

    repository = UserRepository(db)

    return await repository.get_all()


@app.get("/users/{id}")
async def get_user(id: int, db: AsyncSession = Depends(get_db)):

    repository = UserRepository(db)

    return await repository.get_user_byid(id)


@app.put("/users/{id}")
async def update_user(id: int, data: UserCreate, db: AsyncSession = Depends(get_db)):

    repository = UserRepository(db)

    return await repository.update(id, data)


@app.delete("/users/{id}")
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):

    repository = UserRepository(db)

    return await repository.delete(id)
