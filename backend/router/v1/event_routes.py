from uuid import UUID

from fastapi import APIRouter, Depends

from schemas import EventCreate, EventRead, EventFilter, EventUpdate
from controller import EventController


router = APIRouter(prefix="/event", tags=["event"])
controller = EventController()


@router.post("", response_model=EventRead, status_code=201)
async def create_event(event: EventCreate) -> EventRead:
    new_event = await controller.create(event)
    return new_event


@router.get("/{event_id}", response_model=EventRead)
async def read_event(event_id: UUID) -> EventRead:
    event = await controller.read(event_id)
    return event


@router.get("", response_model=list[EventRead])
async def read_many_events(filter: EventFilter = Depends()) -> list[EventRead]:
    events = await controller.read_many(filter)
    return events



@router.patch("/{event_id}", response_model=EventRead, status_code=200)
async def update_event(event_id: UUID, event_update: EventUpdate) -> EventRead:
    updated_event = await controller.update(event_id, event_update)
    return updated_event

@router.delete("/{event_id}", status_code=204)
async def delete_event(event_id: UUID) -> None:
    await controller.delete(event_id)
