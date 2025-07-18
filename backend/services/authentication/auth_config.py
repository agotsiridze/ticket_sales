from settings import token_settings
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer

class AuthConfig:
    def __init__(self, token_url: str = "api/v1/authorization/token"):
        self.settings = token_settings
        self.token_url = token_url
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl=token_url)
        self.credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


auth_config = AuthConfig()