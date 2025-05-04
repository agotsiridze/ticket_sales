from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

from models import TicketStatus




class TicketBase(BaseModel):
    price: int

    access_level: str | None = None
    seat: str | None = None
    room: str | None = None
    expiry_datetime: datetime | None = None

    class Config:
        from_attributes = True


class TicketCreate(TicketBase):
    pass


class TicketRead(TicketBase):
    status: TicketStatus = TicketStatus.available
    owner_id: UUID | None = None
    event_id: UUID
    id: UUID
    created_at: datetime