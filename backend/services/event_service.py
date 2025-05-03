from datetime import datetime
from uuid import uuid4

from repositories import EventRepository
from schemas import EventCreate, EventRead
from models import Event
from .base_service import ServiceBase


class EventService(ServiceBase):
    def __init__(self):
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
            created_by=uuid4(), #TODO: take user_id from token
            is_active=event_data.is_active,
        )
        created_event = await self.repo.create(new_event)
        valid_event = EventRead(created_event)
        return valid_event

    async def read_by_id(self, event_id: str) -> EventRead:
        event = await self.repo.read_by_id(event_id)
        response = EventRead(**event._asdict())
        return response
    
    async def read_all(self) -> list[EventRead]:
        events = await self.repo.read_all()
        response = [EventRead(**event._asdict()) for event in events]
        return response