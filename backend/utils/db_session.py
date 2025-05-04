from settings import postgres_settings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker


DATABASE_URL = URL.create(
    "postgresql+asyncpg",
    username=postgres_settings.POSTGRES_USER,
    password=postgres_settings.POSTGRES_PASSWORD,
    host=postgres_settings.POSTGRES_HOST,
    port=postgres_settings.POSTGRES_PORT,
    database=postgres_settings.POSTGRES_DB,
)

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)