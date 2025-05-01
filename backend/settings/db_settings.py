from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    
    
postgres_settings = DBSettings()