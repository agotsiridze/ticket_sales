from datetime import datetime
from turtle import update
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.sql import Select, Update

from models import Event
from schemas import EventFilter, EventUpdate



class EventSTMTGenerator:
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

    update_stmt = update(Event)

    def read(self, event_id: UUID) -> Select[tuple[UUID, UUID, datetime, str, str, str, datetime, datetime, bool, bool]]:
        stmt = self.stmt.where(Event.id == event_id)
        return stmt

    def read_many(self, filter:EventFilter) -> Select[tuple[UUID, UUID, datetime, str, str, str, datetime, datetime, bool, bool]]:
        stmt = self.stmt.where(Event.is_active == True)

        if filter.title:
            stmt = stmt.where(Event.title.ilike(f"%{filter.title}%"))

        if filter.description:
            stmt = stmt.where(Event.description.ilike(f"%{filter.description}%"))

        if filter.location:
            stmt = stmt.where(Event.location.ilike(f"%{filter.location}%"))

        if filter.start_datetime:
            stmt = stmt.where(Event.start_datetime >= filter.start_datetime)

        if filter.end_datetime:
            stmt = stmt.where(Event.end_datetime <= filter.end_datetime)

        if filter.created_by:
            stmt = stmt.where(Event.created_by == filter.created_by)

        return stmt

    def update(self, event_id: UUID, event_update: EventUpdate) -> Update:
        update_data = event_update.model_dump(exclude_unset=True)
        stmt = self.update_stmt.where(Event.id == event_id).values(**update_data).returning(
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
        return stmt

    def delete(self, event_id: UUID) -> Update:
        stmt = self.update_stmt.where(Event.id == event_id, Event.is_active == True).values(is_active=False)
        return stmt
