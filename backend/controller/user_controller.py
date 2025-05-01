from fastapi import HTTPException
from schemas import UserCreate
from services import UserService
from models import User


async def create_user(user: UserCreate) -> User:
    service = UserService()
    return await service.create_user(user)

async def get_user(user_id: str) -> User:
    service = UserService()
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def list_users() -> list[User]:
    service = UserService()
    return await service.list_users()