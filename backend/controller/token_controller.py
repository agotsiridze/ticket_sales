from services.authentication import TokenService, UserAuthentication, CurrentUser
from schemas import auth


async def create_token(username: str, password: str) -> auth.Token:
    user_auth = UserAuthentication(username)
    user = await user_auth.authenticate_user(password)
    tokenizer = TokenService()
    token = tokenizer.create_access_token({"sub": user.username})
    return token



async def authenticate_user() -> auth.UserInDB:
    user_service = CurrentUser()
    user = await user_service.get_current_user()
    return user