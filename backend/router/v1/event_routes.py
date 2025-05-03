from fastapi import APIRouter

from schemas import EventCreate, EventRead
from models import Event
from controller import EventController


router = APIRouter(prefix="/event", tags=["event"])
controller = EventController()


@router.post("", status_code=201, response_model=EventRead)
async def create_event(event: EventCreate) -> EventRead:
    new_event = await controller.create(event)
    return new_event


@router.get("/{event_id}", response_model=EventRead)
async def get_event(event_id: str) -> EventRead:
    event = await controller.read_by_id(event_id)
    return event


@router.get("", response_model=list[EventRead])
async def list_events() -> list[EventRead]:
    events = await controller.read_all()
    return events