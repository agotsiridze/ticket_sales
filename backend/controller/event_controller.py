from uuid import UUID

from fastapi import HTTPException

from schemas import EventCreate, EventFilter, EventRead, EventUpdate
from services import EventService


class EventController:
    def __init__(self) -> None:
        self.service = EventService()

    async def create(self, event: EventCreate) -> EventRead:
        return await self.service.create(event)

    async def read(self, event_id: UUID) -> EventRead:
        event = await self.service.read(event_id)
        if not event:
            raise HTTPException(status_code=404, detail="event not found")
        return event

    async def read_many(self, filter: EventFilter) -> list[EventRead]:
        return await self.service.read_many(filter)

    async def update(self, event_id: UUID, event_update: EventUpdate) -> EventRead:
        event = await self.service.update(event_id, event_update)
        return event

    async def delete(self, event_id: UUID) -> None:
        await self.service.delete(event_id)
