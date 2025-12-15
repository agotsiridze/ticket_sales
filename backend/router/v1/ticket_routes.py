from uuid import UUID
from fastapi import APIRouter, Depends

from schemas import TicketCreate, TicketRead, TicketFilter, TicketUpdate
from controller import TicketController


router = APIRouter(prefix="/events/{event_id}/tickets", tags=["tickets"])
controller = TicketController()


@router.post("", response_model=TicketRead, status_code=201)
async def create_ticket(event_id: UUID, ticket: TicketCreate) -> TicketRead:
    """Create a new ticket for an event"""
    new_ticket = await controller.create(event_id, ticket)
    return new_ticket


@router.get("/{ticket_id}", response_model=TicketRead, status_code=200)
async def read_ticket(ticket_id: UUID) -> TicketRead:
    """Get a specific ticket"""
    ticket = await controller.read(ticket_id)
    return ticket


@router.get("", response_model=list[TicketRead], status_code=200)
async def read_many_tickets(
    event_id: UUID,
    filters: TicketFilter = Depends()
) -> list[TicketRead]:
    """Get all tickets for an event with optional filters"""
    tickets = await controller.read_many(event_id, filters)
    return tickets


@router.patch("/{ticket_id}", response_model=TicketRead, status_code=200)
async def update_ticket(
    ticket_id: UUID,
    ticket_update: TicketUpdate
) -> TicketRead:
    updated_ticket = await controller.update(ticket_id, ticket_update)
    return updated_ticket


@router.delete("/{ticket_id}", status_code=204)
async def delete_ticket(ticket_id: UUID) -> None:
    """Delete a ticket (soft delete)"""
    await controller.delete(ticket_id)
