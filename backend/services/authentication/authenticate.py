from services import UserService, BCryptPasswordEncode
from schemas import auth
from .auth_config import auth_config

class UserAuthentication:
    user_service = UserService()
    pw_encoder = BCryptPasswordEncode()

    def __init__(self, username):
        self.username = username

    async def authenticate_user(self, password: str) -> auth.UserInDB:
        user = await self.user_service.read_by_username(self.username)
        if user is not None and user.is_active and self.pw_encoder.verify_password(password, user.password_hash):
            return user
        raise auth_config.credentials_exception
