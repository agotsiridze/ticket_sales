from datetime import datetime
from uuid import uuid4

from repositories import TicketRepository
from schemas import TicketCreate, TicketRead
from models import Ticket
from .base_service import ServiceBase


class TicketService(ServiceBase):
    def __init__(self):
        self.repo = TicketRepository()

    async def create(self, ticket_data: TicketCreate, event_id) -> Ticket:
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

    async def read_by_id(self, ticket_id: str) -> TicketRead:
        ticket_row = await self.repo.read_by_id(ticket_id)
        ticket_res = TicketRead(**ticket_row._asdict())
        return ticket_res
    
    async def read_all(self) -> list[Ticket]:
        tickets = await self.repo.read_all()
        response = [TicketRead(**ticket._asdict()) for ticket in tickets]
        return response