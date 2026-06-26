from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User


class UserRepository:

    # constructor
    def __init__(self, db: AsyncSession):
        self.db = db

        # create user

    async def create(self, data):
        user = User(name=data.name, email=data.email)

        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

        return user

    # get all users
    async def get_all(self):

        result = await self.db.execute(select(User))
        user = result.scalars().all()

        return user

    # get user by id
    async def get_user_byid(self, user_id: int):

        result = await self.db.execute(select(User).where(User.id == user_id))

        user = result.scalars().first()
        return user

    # update user
    async def update(self, user_id: int, data):

        result = await self.db.execute(select(User).where(User.id == user_id))

        user = result.scalars().first()

        if not user:

            return None

        user.name = data.name
        user.email = data.email

        await self.db.commit()
        await self.db.refresh(user)

        return user

    # delete user
    async def delete(self, user_id: int):

        result = await self.db.execute(select(User).where(User.id == user_id))

        user = result.scalars().first()

        if not user:
            return False

        await self.db.delete(user)
        await self.db.commit()

        return True
