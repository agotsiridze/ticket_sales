from fastapi import Depends

from services.authentication import TokenService, UserAuthentication, CurrentUser
from schemas import auth
from services.authentication import auth_config
from models import User


async def create_token(username: str, password: str) -> auth.Token:
    user_auth = UserAuthentication(username)
    user = await user_auth.authenticate_user(password)
    tokenizer = TokenService()
    token = tokenizer.create_access_token({"sub": user.username})
    return token



async def authenticate_user(token:str = Depends(auth_config.oauth2_scheme)) -> User:
    user_service = CurrentUser(token)
    user = await user_service.get_current_user()
    return user