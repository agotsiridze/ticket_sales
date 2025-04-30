from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from utils import AsyncSessionLocal
from schemas import UserCreate, UserRead
from services import UserService

async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)) -> UserRead:
    service = UserService(session)
    return await service.create_user(user)

async def get_user(user_id: str, session: AsyncSession = Depends(get_session)) -> UserRead:
    service = UserService(session)
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def list_users(session: AsyncSession = Depends(get_session)) -> list[UserRead]:
    service = UserService(session)
    return await service.list_users()