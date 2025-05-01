from fastapi import APIRouter

from schemas import UserCreate
from models import User
from controller.user_controller import create_user, get_user, list_users


router = APIRouter(prefix="/user", tags=["user"])



@router.post("", status_code=201, response_model=User)
async def register_user(user: UserCreate)->User:
    new_user = await create_user(user)
    return new_user

@router.get("/{user_id}", response_model=User)
async def extract_user(user_id: str)-> User:
    user = await get_user(user_id)
    return user

@router.get("", response_model=list[User])
async def get_all_users() -> list[User]:
    users = await list_users()
    return users