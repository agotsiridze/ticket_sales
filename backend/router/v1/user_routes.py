from fastapi import APIRouter

from schemas import UserCreate, UserResponse
from controller import UserController


router = APIRouter(prefix="/user", tags=["user"])
controller = UserController()



@router.post("", status_code=201, response_model=UserResponse)
async def register_user(user: UserCreate) -> UserResponse:
    new_user = await controller.create_user(user)
    return new_user

@router.get("/{user_id}", response_model=UserResponse)
async def extract_user(user_id: str)-> UserResponse:
    user = await controller.get_user(user_id)
    return user

@router.get("", response_model=list[UserResponse])
async def get_all_users() -> UserResponse:
    users = await controller.read_all()
    return users