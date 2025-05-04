from datetime import datetime
from uuid import uuid4

from repositories import UserRepository
from schemas import UserCreate, UserResponse
from models import User
from .base_service import ServiceBase


class UserService(ServiceBase):
    def __init__(self):
        self.repo = UserRepository()

    async def create(self, user_data: UserCreate) -> UserResponse:
        _id=uuid4()
        new_user = User(
            id=_id,
            username=user_data.username,
            email=user_data.email,
            password_hash=user_data.password,  # temporarily store raw password
            role=user_data.role,
            created_at=datetime.now(),
            is_active=True
        )
        valid_user = await self.repo.create(new_user)
        created_user = UserResponse.model_validate(valid_user)
        return created_user

    async def read_by_id(self, user_id: str) -> UserResponse:
        found_user = await self.repo.read_by_id(user_id)
        response = UserResponse(**found_user._asdict())
        return response
    
    async def read_all(self) -> list[UserResponse]:
        users = await self.repo.read_all()
        response = [UserResponse(**user._asdict()) for user in users]
        return response