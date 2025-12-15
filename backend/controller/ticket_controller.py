from uuid import UUID

from schemas import TicketCreate, TicketFilter, TicketRead, TicketUpdate
from services import TicketService


class TicketController:
    def __init__(self) -> None:
        self.service = TicketService()

    async def create(self, event_id: UUID, ticket: TicketCreate) -> TicketRead:
        return await self.service.create(event_id, ticket)

    async def read(self, ticket_id: UUID) -> TicketRead:
        ticket = await self.service.read(ticket_id)
        return ticket

    async def read_many(self, event_id: UUID, ticket_filter: TicketFilter) -> list[TicketRead]:
        return await self.service.read_many(event_id, ticket_filter)

    async def update(self, ticket_id: UUID, ticket_update: TicketUpdate) -> TicketRead:
        updated_ticket = await self.service.update(ticket_id, ticket_update)
        return updated_ticket

    async def delete(self, ticket_id: UUID) -> None:
        await self.service.delete(ticket_id)
