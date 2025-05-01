from fastapi import HTTPException
from schemas import UserCreate, UserResponse
from services import UserService

# async def get_session() -> AsyncSession:
#     async with AsyncSessionLocal() as session:
#         yield session

async def create_user(user: UserCreate) -> UserResponse:
    service = UserService()
    return await service.create_user(user)

async def get_user(user_id: str) -> UserResponse:
    service = UserService()
    user = await service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def list_users() -> list[UserResponse]:
    service = UserService()
    return await service.list_users()