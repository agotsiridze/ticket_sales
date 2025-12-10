from uuid import UUID

from fastapi import APIRouter, Depends

from schemas import UserCreate, UserResponse, UserFilter, UserUpdate
from controller import UserController


router = APIRouter(prefix="/user", tags=["user"])
controller = UserController()


@router.post("", response_model=UserResponse, status_code=201)
async def register_user(user: UserCreate) -> UserResponse:
    new_user = await controller.create(user)
    return new_user


@router.get("/{user_id}", response_model=UserResponse, status_code=200)
async def read_user(user_id: UUID) -> UserResponse:
    user = await controller.read(user_id)
    return user


@router.get("", response_model=list[UserResponse], status_code=200)
async def get_many_users(filters: UserFilter = Depends()) -> list[UserResponse]:
    users = await controller.read_many(filters)
    return users

@router.patch("/{user_id}", response_model=UserResponse, status_code=200)
async def update_user(user_id: UUID, user_update: UserUpdate) -> UserResponse:
    updated_user = await controller.update(user_id, user_update)
    return updated_user


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: UUID) -> None:
    await controller.delete(user_id)

