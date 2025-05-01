from uuid import uuid4
from datetime import datetime
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from utils import AsyncSessionLocal
from models import User
from schemas.users import UserCreate

class UserRepository:
    def __init__(self, session_factory = AsyncSessionLocal):
        self.session_factory = session_factory
        
    
    @asynccontextmanager
    async def session(self):
        session = self.session_factory()
        try:
            yield session
        finally:
            await session.close()
        

    async def create_user(self, user_data: UserCreate) -> User:
        async with self.session() as session:
            new_user = User(
                id=uuid4(),
                username=user_data.username,
                email=user_data.email,
                password_hash=user_data.password,  # temporarily store raw password
                role=user_data.role,
                created_at=datetime.now(),
                is_active=True
            )
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)
            return new_user

    async def get_user_by_id(self, user_id: str) -> User | None:
        async with self.session() as session:
            result = await session.execute(select(User).where(User.id == user_id))
            user = result.scalar_one()
            return user
    
    async def get_all_users(self) -> list[User]:
        async with self.session() as session:
            result = await session.execute(select(User))
            return result.scalars().all()