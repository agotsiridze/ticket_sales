from fastapi import APIRouter

from schemas import UserCreate, UserResponse
from controller.user_controller import create_user, get_user, list_users


router = APIRouter(prefix="/user", tags=["user"])



@router.post("", status_code=201, response_model=UserResponse)
def register_user(user: UserCreate)->UserResponse:
    new_user = create_user(user)
    return new_user

@router.get("/{user_id}", response_model=UserResponse)
def extract_user(user_id: str)-> UserResponse:
    user = get_user(user_id)
    return user

@router.get("", response_model=list[UserResponse])
def get_all_users() -> UserResponse:
    users = list_users()
    return users