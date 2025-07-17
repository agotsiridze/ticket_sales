from datetime import datetime, timedelta, timezone
import jwt
from jwt import InvalidTokenError
from .auth_config import auth_config
from schemas import auth



class TokenService:
    def __init__(self):
        self.config = auth_config
    
    def create_access_token(self, data: dict) -> auth.Token:
        #TODO: convert datra to schema and use model dump function in leater versions
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + timedelta(minutes=self.config.settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.config.settings.SECRET_KEY, algorithm=self.config.settings.ALGORITHM)
        token = auth.Token(access_token=encoded_jwt, token_type="bearer")
        return token

    

    def decode_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(token, self.config.settings.SECRET_KEY, algorithms=[self.config.settings.ALGORITHM])
            return payload
        except InvalidTokenError:
            raise self.config.credentials_exception
