from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class EventsBase(BaseModel):
    title: str
    description: str | None = None
    location: str
    start_datetime: datetime
    end_datetime: datetime
    is_ticket_available: bool = True
    is_active: bool = True

    class Config:
        orm_mode = True

class EventCreate(EventsBase):
    created_by: UUID  # TODO: Change to current user ID
    created_at: datetime = datetime.now()

class EventRead(EventsBase):
    id: UUID
    created_by: UUID
    created_at: datetime