from fastapi import APIRouter, Depends

from schemas import UserCreate, UserResponse, UserFilter
from controller import UserController


router = APIRouter(prefix="/user", tags=["user"])
controller = UserController()


@router.post("", status_code=201, response_model=UserResponse)
async def register_user(user: UserCreate) -> UserResponse:
    new_user = await controller.create_user(user)
    return new_user


@router.get("/{user_id}", response_model=UserResponse)
async def extract_user(user_id: str) -> UserResponse:
    user = await controller.get_user(user_id)
    return user


@router.get("", response_model=list[UserResponse])
async def get_many_users(filters: UserFilter = Depends()) -> list[UserResponse]:
    users = await controller.read_many(filters)
    return users
