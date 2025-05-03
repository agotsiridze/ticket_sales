from sqlalchemy.future import select
from sqlalchemy.engine import Row

from models import Ticket
from .base_repository import RepositoryBase


class TicketRepository(RepositoryBase):
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

    async def read_by_id(self, event_id: str) -> Row:
        stmt = self.stmt.where(Ticket.id == event_id)
        async with self.session() as session:
            result = await session.execute(stmt)
            user = result.one()
            return user
    
    async def read_all(self) -> list[Row]:
        async with self.session() as session:
            result = await session.execute(self.stmt)
            return result.scalars().all()