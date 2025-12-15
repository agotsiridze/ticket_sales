from uuid import UUID
from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.sql import Select, Update

from models import Ticket
from schemas import TicketFilter, TicketUpdate
from enums import TicketStatus


class TicketSTMTGenerator:
    stmt = select(
        Ticket.id,
        Ticket.created_at,
        Ticket.event_id,
        Ticket.owner_id,
        Ticket.status,
        Ticket.price,
        Ticket.access_level,
        Ticket.seat,
        Ticket.room,
        Ticket.expiry_datetime,
    )
    update_stmt = update(Ticket)

    def read(self, ticket_id: UUID) -> Select[tuple[UUID, datetime, UUID, UUID | None, TicketStatus, int, str | None, str | None, str | None, datetime]]:
        stmt = self.stmt.where(Ticket.id == ticket_id)
        return stmt # type: ignore

    def read_many(self, event_id: UUID, filters: TicketFilter) -> Select[tuple[UUID, datetime, UUID, UUID | None, TicketStatus, int, str | None, str | None, str | None, datetime]]:
        now = datetime.now()
        stmt = self.stmt.where(Ticket.event_id == event_id, Ticket.expiry_datetime > now)

        if filters.status:
            stmt = stmt.where(Ticket.status == filters.status)
        if filters.owner_id:
            stmt = stmt.where(Ticket.owner_id == filters.owner_id)
        if filters.access_level:
            stmt = stmt.where(Ticket.access_level == filters.access_level)
        if filters.room:
            stmt = stmt.where(Ticket.room == filters.room)

        return stmt # type: ignore

    def update(self, Ticket_id: UUID, Ticket_update: TicketUpdate) -> Update:
        update_data = Ticket_update.model_dump(exclude_unset=True)
        stmt = self.update_stmt.where(Ticket.id == Ticket_id).values(**update_data).returning(
            Ticket.id,
            Ticket.created_at,
            Ticket.event_id,
            Ticket.owner_id,
            Ticket.status,
            Ticket.price,
            Ticket.access_level,
            Ticket.seat,
            Ticket.room,
            Ticket.expiry_datetime,
        )
        return stmt

    def delete(self, Ticket_id: UUID) -> Update:
        stmt = self.update_stmt.where(Ticket.id == Ticket_id, Ticket.status != TicketStatus.cancelled).values(status = TicketStatus.cancelled)
        return stmt
