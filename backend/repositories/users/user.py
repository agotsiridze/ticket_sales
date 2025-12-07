from turtle import st
from typing import Sequence
from sqlalchemy.engine import Row

from models import User
from schemas import UserFilter
from repositories.abstract_repository import Repository
from .stmt_generator import UserSTMTGenerator


class UserRepository(Repository):
    stmt = UserSTMTGenerator()

    async def create(self, new_user: User) -> User:
        async with self.uow as session:
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

    async def read(self, user_id: str) -> Row:
        stmt = self.stmt.read_by_id(user_id)
        async with self.uow as session:
            result = await session.execute(stmt)
            row = result.one()
            return row

    async def read_many(self, filters: UserFilter) -> Sequence[Row]:
        stmt = self.stmt.read_many(filters)
        async with self.uow as session:
            result = await session.execute(stmt)
            rows = result.all()
            return rows

    async def update(self):
        pass  # TODO: update user details

    async def delete(self, user_id: str):
        pass  # TODO: deactivate user instead of deleting
