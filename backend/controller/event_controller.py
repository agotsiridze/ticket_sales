from fastapi import HTTPException
from schemas import EventCreate
from services import EventService
from models import Event


class EventController:
    def __init__(self):
        self.service = EventService()

    async def create(self, user: EventCreate) -> Event:
        return await self.service.create(user)

    async def read_by_id(self, user_id: str) -> Event:
        user = await self.service.read_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def read_all(self) -> list[Event]:
        return await self.service.read_all()

