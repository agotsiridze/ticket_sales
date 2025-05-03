from fastapi import HTTPException
from schemas import UserCreate
from services import UserService
from models import User


class UserController:
    def __init__(self):
        self.service = UserService()

    async def create_user(self, user: UserCreate) -> User:
        return await self.service.create_user(user)

    async def get_user(self, user_id: str) -> User:
        user = await self.service.get_user(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def list_users(self) -> list[User]:
        return await self.service.list_users()

