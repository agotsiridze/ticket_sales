from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User
from schemas.users import UserCreate
from uuid import uuid4

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user_data: UserCreate) -> User:
        new_user = User(id=uuid4(), **user_data.model_dump())
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user

    async def get_user_by_id(self, user_id: str) -> User | None:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    
    async def get_all_users(self) -> list[User]:
        result = await self.session.execute(select(User))
        return result.scalars().all()