from repositories import UserRepository
from schemas import UserCreate
from models import User

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    async def create_user(self, user_data: UserCreate) -> User:
        return await self.repo.create_user(user_data)

    async def get_user(self, user_id: str) -> User:
        return await self.repo.get_user_by_id(user_id)
    
    async def list_users(self) -> User:
        return await self.repo.get_all_users()