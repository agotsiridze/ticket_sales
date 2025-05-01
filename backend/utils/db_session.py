import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = f"Environment variable '{var_name}' not set."
        raise Exception(error_msg)


# db_host = get_env_variable('POSTGRES_HOST')
db_port = get_env_variable('POSTGRES_PORT')
db_user = get_env_variable('POSTGRES_USER')
db_password = get_env_variable('POSTGRES_PASSWORD')
db_name = get_env_variable('POSTGRES_DB')

DATABASE_URL = URL.create(
    "postgresql+asyncpg",
    username=db_user,
    password=db_password,
    host="db",
    port=db_port,
    database=db_name,
)


engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)