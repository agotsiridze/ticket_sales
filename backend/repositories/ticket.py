from typing import Sequence

from sqlalchemy.future import select
from sqlalchemy.engine import Row

from models import Ticket, User
from .abstract_repository import Repositories



class TicketRepository(Repositories):
    stmt = select(
                Ticket.id,
                Ticket.created_at,
                Ticket.event_id,
                Ticket.owner_id,
                Ticket.created_at,
                Ticket.status,
                Ticket.price,
                Ticket.access_level,
                Ticket.seat,
                Ticket.room,
                Ticket.expiry_datetime,
            )

    
    async def create(self, ticket_data: Ticket) -> Ticket:
        async with self.session() as session:
            session.add(ticket_data)
            await session.commit()
            await session.refresh(ticket_data)
            return ticket_data

    async def create_many(self, tickets_data: list[Ticket]) -> list[Ticket]:
        async with self.session() as session:
            session.add(tickets_data)
            await session.commit()
            await session.refresh(tickets_data)
            return tickets_data

    async def read_by_id(self, event_id: str) -> Row:
        stmt_updated = self.stmt.where(Ticket.id == event_id)
        async with self.session() as session:
            result = await session.execute(stmt_updated)
            user = result.one()
            return user
    
    async def read_all(self) -> Sequence[Row]:
        async with self.session() as session:
            result = await session.execute(self.stmt)
            return result.all()


    async def read_by_event(self, event_id: str) -> Sequence[Row]:
        stmt = self.stmt.where(Ticket.event_id == event_id)
        async with self.session() as session:
            result = await session.execute(stmt)
            return result.all()
    
    async def update_owner(self, ticket_id: str, owner: User) -> Ticket:
        async with self.session() as session:
            stmt = select(Ticket).where(Ticket.id == ticket_id).with_for_update()
            result = await session.execute(stmt)
            ticket = result.scalar_one()
            ticket.owner = owner
            await session.commit()
            await session.refresh(ticket)
            return ticket