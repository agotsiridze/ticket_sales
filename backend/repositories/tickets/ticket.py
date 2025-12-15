from datetime import datetime
from typing import Sequence
from uuid import UUID

from sqlalchemy.engine import Row

from models import Ticket
from ..abstract_repository import Repository
from enums import TicketStatus
from schemas import TicketFilter, TicketUpdate
from .stmt_generator import TicketSTMTGenerator




class TicketRepository(Repository):

    stmt = TicketSTMTGenerator()

    async def create(self, ticket_data: Ticket) -> Ticket:
        async with self.uow as session:
            session.add(ticket_data)
            await session.commit()
            await session.refresh(ticket_data)
            return ticket_data

    # async def create_many(self, tickets_data: list[Ticket]) -> list[Ticket]:
    #     async with self.uow as session:
    #         session.add(tickets_data)
    #         await session.commit()
    #         await session.refresh(tickets_data)
    #         return tickets_data

    async def read(self, ticket_id: UUID) -> Row[tuple[UUID, datetime, UUID, UUID | None, TicketStatus, int, str | None, str | None, str | None, datetime]]:
        stmt = self.stmt.read(ticket_id)
        async with self.uow as session:
            result = await session.execute(stmt)
            ticket = result.one()
            return ticket # type: ignore

    async def read_many(self, event_id: UUID, ticket_filter: TicketFilter) -> Sequence[Row[tuple[UUID, datetime, UUID, UUID | None, TicketStatus, int, str | None, str | None, str | None, datetime]]]:
        stmt = self.stmt.read_many(event_id, ticket_filter)
        async with self.uow as session:
            result = await session.execute(stmt)
            return result.all() # type: ignore


    async def update(self, ticket_id: UUID, ticket_update: TicketUpdate) -> Row[tuple[UUID, datetime, UUID, UUID | None, TicketStatus, int, str | None, str | None, str | None, datetime]]:
        stmt = self.stmt.update(ticket_id, ticket_update)
        async with self.uow as session:
            result = await session.execute(stmt)
            await session.commit()
            updated_ticket = result.one()
            return updated_ticket # type: ignore


    async def delete(self, ticket_id: UUID) -> None:
        stmt = self.stmt.delete(ticket_id)
        async with self.uow as session:
            await session.execute(stmt)
            await session.commit()
