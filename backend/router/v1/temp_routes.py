from typing import Annotated
from datetime import timedelta

from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from schemas import auth
from services import authentication


router = APIRouter(prefix="/temp", tags=["temp"])


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> auth.Token:
    user = authentication.authenticate_user(authentication.fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=authentication.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = authentication.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return auth.Token(access_token=access_token, token_type="bearer")



@router.get("/users/me/", response_model=auth.User)
async def read_users_me(
    current_user: Annotated[auth.User, Depends(authentication.get_current_active_user)],
):
    return current_user



@router.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[auth.User, Depends(authentication.get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]