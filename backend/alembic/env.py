import asyncio
from logging.config import fileConfig

from sqlalchemy.engine import Connection

from alembic import context

from models import Base
from utils import DATABASE_URL, engine

target_metadata = Base.metadata

def create_offline_config():
    config = context.config
    config.set_main_option("sqlalchemy.url", str(DATABASE_URL))

    if config.config_file_name is not None:
        fileConfig(config.config_file_name)
    return config

def run_migrations_offline() -> None:
    config = create_offline_config()
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    
    async with engine.begin() as conn:
        await conn.run_sync(do_run_migrations)
    await engine.dispose()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
