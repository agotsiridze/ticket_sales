from fastapi import APIRouter

from schemas import TicketCreate, TicketRead
from controller import TicketController


router = APIRouter(prefix="/ticket", tags=["ticket"])
controller = TicketController()


@router.post("/event/{event_id}", status_code=201, response_model=TicketRead)
async def create_ticket(event_id, ticket: TicketCreate) -> TicketRead:
    new_ticket = await controller.create(ticket, event_id)
    return new_ticket


@router.get("/{ticket_id}", response_model=TicketRead)
async def get_event(ticket_id: str) -> TicketRead:
    event = await controller.read_by_id(ticket_id)
    return event


@router.get("", response_model=list[TicketRead])
async def list_events() -> list[TicketRead]:
    events = await controller.read_all()
    return events