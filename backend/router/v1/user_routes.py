from fastapi import APIRouter

from schemas import UserCreate, UserResponse
from models import User
from controller.user_controller import create_user, get_user, list_users


router = APIRouter(prefix="/user", tags=["user"])



@router.post("", status_code=201, response_model=UserResponse)
async def register_user(user: UserCreate)->User:
    new_user = await create_user(user)
    return new_user

@router.get("/{user_id}", response_model=UserResponse)
async def extract_user(user_id: str)-> UserResponse:
    user = await get_user(user_id)
    return user

@router.get("", response_model=list[UserResponse])
async def get_all_users() -> UserResponse:
    users = await list_users()
    return users