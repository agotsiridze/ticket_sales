from repositories import TicketRepository
from models import User
from schemas import TicketRead

class SalesService:
    def __init__(self) -> None:
        self.ticket_repo = TicketRepository()
        
    async def buy_ticket(self, ticket_id: str, owner: User) -> TicketRead:
        updated_ticket = await self.ticket_repo.update_owner(ticket_id, owner)
        TicketRead.model_validate(updated_ticket)
        return updated_ticket