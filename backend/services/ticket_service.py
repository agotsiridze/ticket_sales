from datetime import datetime
from uuid import uuid4, UUID

from repositories import TicketRepository
from schemas import TicketCreate, TicketRead, TicketFilter, TicketUpdate
from models import Ticket


class TicketService:
    def __init__(self) -> None:
        self.repo = TicketRepository()

    async def create(self, event_id: UUID, ticket_data: TicketCreate) -> TicketRead:
        _id = uuid4()
        new_ticket = Ticket(
                id=_id,
                event_id=event_id,
                price = ticket_data.price,
                access_level= ticket_data.access_level,
                seat=ticket_data.seat,
                room=ticket_data.room,
                created_at=datetime.now(),
                expiry_datetime = ticket_data.expiry_datetime,
            )
        valid_ticket = await self.repo.create(new_ticket)
        created_ticket = TicketRead.model_validate(valid_ticket)
        return created_ticket

    async def read(self, ticket_id: UUID) -> TicketRead:
        ticket_row = await self.repo.read(ticket_id)
        ticket_res = TicketRead.model_validate(ticket_row)
        return ticket_res

    async def read_many(self, event_id: UUID, ticket_filter: TicketFilter) -> list[TicketRead]:
        tickets = await self.repo.read_many(event_id, ticket_filter)
        response = [TicketRead.model_validate(ticket) for ticket in tickets]
        return response

    async def update(self, ticket_id: UUID, ticket_update: TicketUpdate) -> TicketRead:
        updated_row = await self.repo.update(ticket_id, ticket_update)
        updated_ticket = TicketRead.model_validate(updated_row)
        return updated_ticket

    async def delete(self, ticket_id: UUID) -> None:
        await self.repo.delete(ticket_id)
