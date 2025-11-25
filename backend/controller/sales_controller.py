from services import SalesService
from models import User
from schemas import TicketRead


sales = SalesService()

async def buy_ticket(ticket_id: str, owner: User) -> TicketRead:
    bought_ticket = await sales.buy_ticket(ticket_id, owner)
    return bought_ticket