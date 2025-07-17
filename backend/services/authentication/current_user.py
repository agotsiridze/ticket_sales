from fastapi import Depends

from .auth_config import auth_config
from .tokenization import TokenService
from services import UserService
from schemas import auth


class CurrentUser:
    user_service = UserService()
    def __init__(self, token: str = Depends(auth_config.oauth2_scheme)):
        self.token = token
        

    async def get_current_user(self) -> auth.UserInDB:
        token_service = TokenService()
        payload = token_service.decode_token(self.token)
        username = payload.get("sub")
        if username is None:
            raise auth_config.credentials_exception
        
        try:
            user = await self.user_service.read_by_username(username)
        except:
            raise auth_config.credentials_exception
        
        return user
    
