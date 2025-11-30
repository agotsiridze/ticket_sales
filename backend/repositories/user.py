from typing import Sequence
from sqlalchemy.future import select
from sqlalchemy.engine import Row

from models import User
from .abstract_repository import Repositories


class UserRepository(Repositories):
    stmt = select(
                User.id,
                User.username,
                User.email,
                User.role,
                User.created_at,
                User.is_active
            )
    
    async def create(self, new_user: User) -> User:
        async with self.uow as session:
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

    async def read_by_id(self, user_id: str) -> Row:
        stmt = self.stmt.where(User.id == user_id)
        async with self.uow as session:
            result = await session.execute(stmt)
            row = result.one()
            
            return row

    async def read_by_username(self, username: str) -> User:
        stmt = select(User).where(User.username == username)
        async with self.uow as session:
            result = await session.execute(stmt)
            row = result.scalar_one()
            return row
    
    async def read_all(self) -> Sequence[Row]:
        async with self.uow as session:
            result = await session.execute(self.stmt)
            rows = result.all()
            return rows