from sqlalchemy.future import select
from sqlalchemy.engine import Row

from models import Event
from schemas import EventCreate
from .base_repository import RepositoryBase



class EventRepository(RepositoryBase):
    stmt = select(
            Event.id,
            Event.created_by,
            Event.created_at,
            Event.title,
            Event.description,
            Event.location,
            Event.start_datetime,
            Event.end_datetime,
            Event.is_ticket_available,
            Event.is_active,
        )
    async def create(self, new_event: EventCreate) -> Event:
        async with self.session() as session:
            session.add(new_event)
            await session.commit()
            await session.refresh(new_event)
            return new_event

    async def read_by_id(self, event_id: str) -> Row:
        stmt = self.stmt.where(Event.id == event_id)
        async with self.session() as session:
            result = await session.execute(stmt)
            event = result.one()
            return event
    
    async def read_all(self) -> list[Row]:
        async with self.session() as session:
            result = await session.execute(self.stmt)
            return result.all()