import asyncio

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from models import Base

app = FastAPI()

engine = create_async_engine("sqlite+aiosqlite:///users.db", echo=True)
# the echo=True parameter tells SQLAlchemy to print all SQL
# statements that it executes to the console/logs.

AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
# expire_on_commit=False is commonly used so objects
# remain accessible after commit


# to create tables  this function runs once when the app is started
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

#create get_db(), which FastAPI will use as a dependency to provide a database session for each request.
async def get_db():

    async with AsyncSessionLocal() as session:
        yield session
