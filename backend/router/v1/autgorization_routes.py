from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from controller import create_token, authenticate_user
from schemas import auth
from models import User


router = APIRouter(prefix="/authorization", tags=["authorization"])


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> auth.Token:
    token = await create_token(form_data.username, form_data.password)
    return token



@router.get("/me/", response_model=auth.User)
async def read_users_me(
    current_user: Annotated[User, Depends(authenticate_user)],
):
    return current_user



