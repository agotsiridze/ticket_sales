from sqlalchemy.future import select
from models import User
from schemas import UserFilter
from enums import UserRole


class UserSTMTGenerator:
    stmt = select(
        User.id, User.username, User.email, User.role, User.created_at, User.is_active
    )

    async def read_by_id(self, user_id: str):
        stmt = self.stmt.where(User.id == user_id)
        return stmt

    async def read_many(self, filters: UserFilter):
        stmt = self.stmt.where(User.is_active == True, User.role != UserRole.admin)
        if filters.username:
            stmt = stmt.where(User.username.ilike(f"%{filters.username}%"))
        if filters.email:
            stmt = stmt.where(User.email.ilike(f"%{filters.email}%"))
        return stmt

    async def update(self):
        pass  # TODO: update user details

    async def delete(self, user_id: str):
        pass  # TODO: deactivate user instead of deleting
