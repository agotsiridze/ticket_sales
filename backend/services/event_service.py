from datetime import datetime
from uuid import uuid4, UUID

from repositories import EventRepository
from schemas import EventCreate, EventRead, EventFilter, EventUpdate
from models import Event


class EventService:
    def __init__(self) -> None:
        self.repo = EventRepository()

    async def create(self, event_data: EventCreate) -> EventRead:
        _id=uuid4()
        new_event = Event(
            id=_id,
            title=event_data.title,
            description=event_data.description,
            location=event_data.location,
            start_datetime=event_data.start_datetime,
            end_datetime=event_data.end_datetime,
            is_ticket_available=event_data.is_ticket_available,
            created_by=event_data.created_by, #TODO: take user_id from token
            created_at=datetime.now(),
            is_active=event_data.is_active,
        )
        created_event = await self.repo.create(new_event)
        valid_event = EventRead.model_validate(created_event)
        return valid_event

    async def read(self, event_id: UUID) -> EventRead:
        event = await self.repo.read(event_id)
        res = EventRead.model_validate(event)
        return res

    async def read_many(self, filter: EventFilter) -> list[EventRead]:
        events = await self.repo.read_many(filter)
        response = [EventRead.model_validate(event) for event in events]
        return response

    async def update(self, event_id: UUID, event_update: EventUpdate) -> EventRead:
        event = await self.repo.update(event_id, event_update)
        response = EventRead.model_validate(event)
        return response

    async def delete(self, event_id: UUID) -> None:
        await self.repo.delete(event_id)
