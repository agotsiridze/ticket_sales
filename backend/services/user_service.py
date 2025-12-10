from datetime import datetime
from uuid import uuid4, UUID


from .password_hash import BCryptPasswordEncode
from repositories import UserRepository
from schemas import UserCreate, UserResponse, UserFilter, UserUpdate
from models import User


class UserService:#temp - removed base class
    encoder = BCryptPasswordEncode()

    def __init__(self) -> None:
        self.repo = UserRepository()

    async def create(self, user_data: UserCreate) -> UserResponse:
        _id = uuid4()
        new_user = User(
            id=_id,
            username=user_data.username,
            email=user_data.email,
            password_hash=self.encoder.hash_password(
                user_data.password
            ),  # hash the password
            role=user_data.role,
            created_at=datetime.now(),
            is_active=True,
        )
        valid_user = await self.repo.create(new_user)
        created_user = UserResponse.model_validate(valid_user)
        return created_user


    async def read(self, user_id: UUID) -> UserResponse:
        found_user = await self.repo.read(user_id)
        response = UserResponse.model_validate(found_user)
        return response


    async def read_many(self, filters: UserFilter) -> list[UserResponse]:
        users = await self.repo.read_many(filters)
        response = [UserResponse.model_validate(user) for user in users]
        return response

    async def update(self, user_id: UUID, user_update: UserUpdate) -> UserResponse:
        updated_user = await self.repo.update(user_id, user_update)
        response = UserResponse.model_validate(updated_user)
        return response

    async def delete(self, user_id: UUID) -> None:
        await self.repo.delete(user_id)
