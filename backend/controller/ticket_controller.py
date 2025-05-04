from fastapi import HTTPException
from schemas import TicketCreate
from services import TicketService
from models import Ticket


class TicketController:
    def __init__(self):
        self.service = TicketService()

    async def create(self, ticket: TicketCreate, event_id) -> Ticket:
        return await self.service.create(ticket, event_id)

    async def read_by_id(self, ticket_id: str) -> Ticket:
        user = await self.service.read_by_id(ticket_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    async def read_all(self) -> list[Ticket]:
        return await self.service.read_all()

