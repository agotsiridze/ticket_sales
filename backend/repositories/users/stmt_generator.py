from sqlalchemy import select, update
from models import User
from schemas import UserFilter
from enums import UserRole
from sqlalchemy.sql import Select, Update
from uuid import UUID
from datetime import datetime


class UserSTMTGenerator:
    select_stmt = select(
        User.id, User.username, User.email, User.role, User.created_at, User.is_active
    )
    update_stmt = update(User)

    def read_by_id(self, user_id: str) -> Select[tuple[UUID, str, str, str, datetime, bool]]:
        stmt = self.select_stmt.where(User.id == user_id)
        return stmt

    def read_many(self, filters: UserFilter) -> Select[tuple[UUID, str, str, str, datetime, bool]]:
        stmt = self.select_stmt.where(
            User.is_active == True, User.role != UserRole.admin
        )
        if filters.username:
            stmt = stmt.where(User.username.ilike(f"%{filters.username}%"))
        if filters.email:
            stmt = stmt.where(User.email.ilike(f"%{filters.email}%"))
        return stmt

    def update(self) -> None:
        pass  # TODO: update user details

    def delete(self, user_id: str) -> Update:
        stmt = self.update_stmt.where(User.id == user_id).values(is_active=False)
        return stmt
