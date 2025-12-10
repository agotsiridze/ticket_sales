from uuid import UUID

from schemas import UserCreate, UserFilter, UserResponse, UserUpdate
from services import UserService


class UserController:
    def __init__(self) -> None:
        self.service = UserService()

    async def create(self, user: UserCreate) -> UserResponse:
        return await self.service.create(user)

    async def read(self, user_id: UUID) -> UserResponse:
        user = await self.service.read(user_id)
        return user

    async def read_many(self, filters: UserFilter) -> list[UserResponse]:
        users = await self.service.read_many(filters)
        return users

    async def update(self, user_id: UUID, user_update: UserUpdate) -> UserResponse:
        return await self.service.update(user_id, user_update)

    async def delete(self, user_id: UUID) -> None:
        await self.service.delete(user_id)
