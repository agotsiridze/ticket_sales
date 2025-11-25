from fastapi import APIRouter, Depends

from controller import authenticate_user, buy_ticket
from schemas import TicketRead

router = APIRouter(prefix="/sales", tags=["sales"])

@router.post("/{ticket_id}", response_model=TicketRead)
async def purchase_ticket(ticket_id: str, current_user=Depends(authenticate_user)) -> TicketRead:
    purchased_ticket = await buy_ticket(ticket_id, current_user)
    return purchased_ticket