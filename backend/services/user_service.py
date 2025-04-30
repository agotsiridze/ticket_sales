from repositories import UserRepository
from schemas import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    async def create_user(self, user_data: UserCreate):
        return await self.repo.create_user(user_data)

    async def get_user(self, user_id: str):
        return await self.repo.get_user_by_id(user_id)
    
    async def list_users(self):
        return await self.repo.get_all_users()