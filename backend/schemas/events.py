from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime

class EventsBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100,
        description="Title of the event",
        example="Tech Conference 2025",
    )
    description: str | None = Field(
        None,
        description="Detailed description of the event",
        example="Annual technology conference featuring the latest innovations"
    )
    location: str = Field(
        ...,
        description="Location of the event",
        example="123 Tech Lane, Silicon Valley, CA"
    )
    start_datetime: datetime = Field(
        ...,
        description="Start date and time of the event",
        example="2025-05-01T09:00:00Z"
    )
    end_datetime: datetime = Field(
        ...,
        description="End date and time of the event",
        example="2025-05-01T17:00:00Z"
    )
    is_ticket_available: bool = Field(
        ...,
        description="Indicates if tickets are available for the event",
        example=True
    )
    is_active: bool = Field(
        True,
        description="Indicates if the event is active",
        example=True
    )

    class Config:
        from_attributes = True

class EventCreate(EventsBase):
    created_by: UUID = Field(
        ...,
        description="ID of the user who created the event",
        example="123e4567-e89b-12d3-a456-426614174000"
    ) # TODO: Change to current user ID

class EventRead(EventsBase):
    id: UUID = Field(
        ...,
        description="Unique identifier for the event",
        example="123e4567-e89b-12d3-a456-426614174000"
    )
    created_by: UUID = Field(
        ...,
        description="ID of the user who created the event",
        example="123e4567-e89b-12d3-a456-426614174000"  
    )
    created_at: datetime = Field(
        ...,
        description="Date and time when the event was created",
        example="2025-01-01T12:00:00Z"
    )