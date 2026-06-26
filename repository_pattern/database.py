# databse .engine,creations

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from models import Base

engine = create_async_engine("sqlite+aiosqlite:///users.db", echo=True)

AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# Question: Why don't we use Base.metadata.create_all() in production?

# Answer:

# create_all() only creates tables that don't already exist. 
# It cannot modify existing tables by adding, removing, renaming,
#  or changing columns. In production, we use Alembic migrations
#  because they provide version-controlled, incremental, and
#  reversible schema changes without losing existing data.
#  During deployment, we run python -m alembic upgrade head 
#  bring the database schema up to date before starting the application.
