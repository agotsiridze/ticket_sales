from typing import Sequence
from datetime import datetime
from uuid import UUID

from sqlalchemy.engine import Row

from schemas import EventCreate, EventFilter, EventUpdate
from repositories.abstract_repository import Repository
from .stmt_generator import EventSTMTGenerator



class EventRepository(Repository):
    stmt = EventSTMTGenerator()
    async def create(self, new_event: EventCreate) -> EventCreate:
        async with self.uow as session:
            session.add(new_event)
            await session.commit()
            await session.refresh(new_event)
            return new_event

    async def read(self, event_id: UUID) -> Row[tuple[UUID, UUID, datetime, str, str, str, datetime, datetime, bool, bool]]:
        stmt = self.stmt.read(event_id)
        async with self.uow as session:
            result = await session.execute(stmt)
            event = result.one()
            return event

    async def read_many(self, filter: EventFilter) -> Sequence[Row[tuple[UUID, UUID, datetime, str, str, str, datetime, datetime, bool, bool]]]:
        stmt = self.stmt.read_many(filter)
        async with self.uow as session:
            result = await session.execute(stmt)
            event = result.all()
            return event

    async def update(self, event_id: UUID, event_update: EventUpdate) -> Row[tuple[UUID, UUID, datetime, str, str, str, datetime, datetime, bool, bool]]:
        stmt = self.stmt.update(event_id, event_update)
        async with self.uow as session:
            result = await session.execute(stmt)
            result = result.one()
            await session.commit()
            return result

    async def delete(self, event_id: UUID) -> None:
        stmt = self.stmt.delete(event_id)
        async with self.uow as session:
            await session.execute(stmt)
            await session.commit()
