from sqlalchemy import select, update
from models import User
from schemas import UserFilter, UserUpdate
from enums import UserRole
from sqlalchemy.sql import Select, Update
from uuid import UUID
from datetime import datetime


class UserSTMTGenerator:
    select_stmt = select(
        User.id, User.username, User.email, User.role, User.created_at, User.is_active
    )
    update_stmt = update(User)

    def read_by_id(self, user_id: UUID) -> Select[tuple[UUID, str, str, str, datetime, bool]]:
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

    def update(self, user_id: UUID, user_update: UserUpdate) -> Update:
        update_data = user_update.model_dump(exclude_unset=True)
        stmt = self.update_stmt.where(User.id == user_id).values(**update_data).returning(User.id, User.username, User.email, User.role, User.created_at, User.is_active)
        return stmt

    def delete(self, user_id: UUID) -> Update:
        stmt = self.update_stmt.where(User.id == user_id, User.is_active == True).values(is_active=False)
        return stmt
