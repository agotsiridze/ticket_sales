from pydantic_settings import BaseSettings


class TokenSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    
token_settings = TokenSettings()